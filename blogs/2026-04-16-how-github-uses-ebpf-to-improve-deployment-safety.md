---
title: "How GitHub uses eBPF to improve deployment safety"
url: "https://github.blog/engineering/infrastructure/how-github-uses-ebpf-to-improve-deployment-safety/"
date: "Thu, 16 Apr 2026 16:00:00 +0000"
author: "Lawrence Gripper"
feed_url: "https://github.blog/feed/"
---
<p>Did you know that, at GitHub, we host all of our own source code on <a href="http://github.com">github.com</a>? We do this because we&rsquo;re our own biggest customer&mdash;testing out changes internally before they go to users. However, there&rsquo;s one downside: If github.com were ever to go down, we wouldn&rsquo;t be able to access our own source code.</p>



<p>This is what you&rsquo;d call a very simple circular dependency: to deploy GitHub, we needed GitHub. If GitHub is down, then we wouldn&rsquo;t be able to deploy something to fix it. We mitigate this by maintaining a mirror of our code for fixing forward and built assets for rolling back.</p>



<p>So we&rsquo;re done, right? Problem solved? Nope, there are more circular dependencies to consider. For example, how do you stop a deployment script introducing a circular dependency of its own on an internal service or downloading a binary from GitHub?</p>



<p>When we started to design our new host-based deployment system, we evaluated some new approaches to prevent deployment code from creating circular dependencies. We found that using eBPF, we could selectively monitor and block those calls. In this blog post, we&rsquo;ll take you through our findings and show how you can get started writing your own eBPF programs.</p>



<h2 class="wp-block-heading" id="h-types-of-circular-dependencies">Types of circular dependencies</h2>



<p>Let&rsquo;s start by looking at the types of circular dependencies through a hypothetical scenario.</p>



<p>Suppose a MySQL outage occurs, which causes GitHub to be unable to serve <code>release</code> data from repositories. To resolve the incident, we need to roll out a configuration change to the stateful MySQL nodes that are impacted. This configuration change is applied by executing a deploy script on each node.</p>



<p>Now, let&rsquo;s look at the different types of circular dependencies that could impact GitHub during this scenario.</p>



<ol class="wp-block-list" start="1">
<li><strong>Direct dependency</strong>: The MySQL deploy script attempts to pull the latest release of an&nbsp;open source&nbsp;tool from GitHub. Since GitHub&nbsp;can&rsquo;t&nbsp;serve the release data (due to the outage), the script&nbsp;can&rsquo;t&nbsp;complete.&nbsp;&nbsp;</li>
</ol>



<figure class="wp-block-image size-full"><img alt="Diagram showing a MySQL deploy script fails after attempting to pull the latest release of an&nbsp;open&nbsp;source&nbsp;tool from GitHub." class="wp-image-95085" height="194" src="https://github.blog/wp-content/uploads/2026/04/Screenshot-2026-04-06-at-6.36.24-PM.png?resize=1433%2C194" width="1433" /></figure>



<ol class="wp-block-list" start="2">
<li><strong>Hidden dependencies</strong>: The MySQL deploy script uses a servicing tool that is already present on the machine&rsquo;s disk. However, when the tool runs, it checks GitHub to see if an update is available. If it&rsquo;s unable to contact GitHub (due to the outage), the script may fail or hang, depending on how the tool handles the error when checking for updates.</li>
</ol>



<figure class="wp-block-image size-full"><img alt="Diagram showing a script failing after being unable to contact GitHub (due to the outage)." class="wp-image-95086" height="363" src="https://github.blog/wp-content/uploads/2026/04/Screenshot-2026-04-06-at-6.36.34-PM.png?resize=1439%2C363" width="1439" /></figure>



<ol class="wp-block-list" start="3">
<li><strong>Transient dependencies</strong>: The MySQL deploy script calls, via an API, another internal service (for example, a migrations service), which in turn attempts to fetch the latest release of an open source tool from GitHub to use the new binary. The failure propagates back to the deploy script.</li>
</ol>



<figure class="wp-block-image size-full"><img alt="Diagram showing a MySQL deploy script calling, via an API, another internal service, which in turn attempts to fetch the latest release of an open source tool from GitHub to use the new binary. The failure propagates back to the deploy script." class="wp-image-95088" height="202" src="https://github.blog/wp-content/uploads/2026/04/Screenshot-2026-04-06-at-6.36.41-PM.png?resize=1450%2C202" width="1450" /></figure>



<h2 class="wp-block-heading" id="h-how-do-you-solve-these-circular-dependencies">How do you solve these circular dependencies?</h2>



<p>Until recently, the onus has been on every team who that owns stateful hosts to review their deployment scripts and identify circular dependencies.</p>



<p>In practice, however, many dependencies aren&rsquo;t identified until an incident occurs, which can delay recovery.</p>



<p>The obvious route would be to block access to github.com from the machines to validate that the system can deploy without it. But these hosts are stateful and serve customer traffic even during rolling deploys, drains, or restarts. Blocking github.com entirely would impact their ability to handle production requests.</p>



<p>This is where we started to look at eBPF, which lets you load custom programs into the Linux kernel and hook into core system primitives like networking.</p>



<p>We were particularly interested in the <a href="https://docs.ebpf.io/linux/program-type/BPF_PROG_TYPE_CGROUP_SKB/"><code>BPF_PROG_TYPE_CGROUP_SKB</code> program type</a> because it lets you hook network egress from a particular cGroup.</p>



<p>A <a href="https://en.wikipedia.org/wiki/Cgroups">cGroup</a> is a Linux primitive (used heavily by Docker but not limited to it) that enforces resource limits and isolation for sets of processes. You can create a cGroup, configure it, and move processes into it&mdash;no Docker required.</p>



<p>This started to look very promising. Could we create a cGroup, place only the deployment script inside it, and then limit the outbound network access of only that script? It certainly looked possible, so we started to build a proof of concept.</p>



<h2 class="wp-block-heading" id="h-building-out-per-process-conditional-network-filtering-with-ebpf">Building out per-process conditional network filtering with eBPF</h2>



<p>We started on a proof of concept in <code>go</code> that used the <code><a href="https://github.com/cilium/ebpf">cilium/ebpf</a></code> library.</p>



<p>ebpf-go is a pure-Go library to read, modify, and load eBPF programs and attach them to various hooks in the Linux kernel.</p>



<p>It massively simplifies the process of authoring, building, and running programs that use eBPF. For example, to hook the <a href="https://docs.ebpf.io/linux/program-type/BPF_PROG_TYPE_CGROUP_SKB/"><code>BPF_PROG_TYPE_CGROUP_SKB</code> program type</a>, we can do this as follows: &#128071;</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>//go:generate go tool bpf2go -tags linux bpf cgroup_skb.c -- -I../headers 

 

func main() { 

   // Load pre-compiled programs and maps into the kernel. 

   objs := bpfObjects{} 

   if err := loadBpfObjects(&amp;objs, nil); err != nil { 

       log.Fatalf("loading objects: %v", err) 

   } 

   defer objs.Close() 

 

   // Link the count_egress_packets program to the cgroup. 

   l, err := link.AttachCgroup(link.CgroupOptions{ 

       Path:    "/sys/fs/cgroup/system.slice", 

       Attach:  ebpf.AttachCGroupInetEgress, 

       Program: objs.CountEgressPackets, 

   }) 

   if err != nil { 

       log.Fatal(err) 

   } 

   defer l.Close() 

 

   log.Println("Counting packets...") 

 

   // Read loop reporting the total amount of times the kernel 

   // function was entered, once per second. 

   ticker := time.NewTicker(1 * time.Second) 

   defer ticker.Stop() 

 

   for range ticker.C { 

       var value uint64 

       if err := objs.PktCount.Lookup(uint32(0), &amp;value); err != nil { 

           log.Fatalf("reading map: %v", err) 

       } 

       log.Printf("number of packets: %d\n", value) 

   } 

} </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>With the eBPF program:</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>//go:build ignore 

 

#include "common.h" 

 

char __license[] SEC("license") = "Dual MIT/GPL"; 

 

struct { 

   __uint(type, BPF_MAP_TYPE_ARRAY); 

   __type(key, u32); 

   __type(value, u64); 

   __uint(max_entries, 1); 

} pkt_count SEC(".maps"); 

 

SEC("cgroup_skb/egress") 

int count_egress_packets(struct __sk_buff *skb) { 

   u32 key      = 0; 

   u64 init_val = 1; 

 

   u64 *count = bpf_map_lookup_elem(&amp;pkt_count, &amp;key); 

   if (!count) { 

       bpf_map_update_elem(&amp;pkt_count, &amp;key, &amp;init_val, BPF_ANY); 

       return 1; 

   } 

   __sync_fetch_and_add(count, 1); 

 

   return 1; 

} </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>The <code>//go:generate</code> line handles compiling the eBPF C code and auto-generating the <code>bpfObjects</code> struct, which allows us to attach and interact with the program. This means a simple <code>go build</code> is all you need. &#129395;</p>



<p>(<code>cilium/ebpf</code> has a great set of examples to get started. <a href="https://github.com/cilium/ebpf/tree/main/examples/cgroup_skb">Review the full code from above</a>).</p>



<p>There was still a missing piece though: <code>CGROUP_SKB</code> operates on IP addresses. Given the breadth of GitHub&rsquo;s systems and rate of change, keeping an up-to-date block IP list would be very hard.</p>



<p>Could we use more eBPF to create a DNS-based blocked list? Yes, it turns out we could.</p>



<p>An eBPF <a href="https://docs.ebpf.io/linux/program-type/BPF_PROG_TYPE_CGROUP_SOCK_ADDR/">program type of <code>BPF_PROG_TYPE_CGROUP_SOCK_ADDR</code></a> allows you to hook syscalls to create sockets <strong>and change the destination IP</strong>.</p>



<p>Here is a simplified example where we rewrite any <code>connect4</code> syscall targeting DNS (Port 53) to <code>localhost:53</code>.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>cgroupLink, err := link.AttachCgroup(link.CgroupOptions{ 

       Path:    cgroup.Name(), 

       Attach:  ebpf.AttachCGroupInet4Connect, 

       Program: obj.Connect4, 

   }) 

   if err != nil { 

       return nil, fmt.Errorf("attaching eBPF program Connect4 to cgroup: %w", err) 

   } </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>

<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>/* This is the hexadecimal representation of 127.0.0.1 address */ 

const __u32 ADDRESS_LOCALHOST_NETBYTEORDER = bpf_htonl(0x7f000001); 

 

SEC("cgroup/connect4") 

int connect4(struct bpf_sock_addr *ctx) { 

 __be32 original_ip = ctx-&gt;user_ip4; 

 __u16 original_port = bpf_ntohs(ctx-&gt;user_port); 

 

 if (ctx-&gt;user_port == bpf_htons(53)) { 

   /* For DNS Query (*:53) rewire service to backend 

    * 127.0.0.1:const_dns_proxy_port */ 

   ctx-&gt;user_ip4 = const_mitm_proxy_address; 

   ctx-&gt;user_port = bpf_htons(const_dns_proxy_port); 

 } 

 

 return 1; 

} </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>We used this to intercept DNS queries from the cGroup and forward them to a userspace DNS proxy we run.</p>



<p>Now, any DNS queries initiated by the deployment script are routed through our DNS proxy. Our proxy evaluates each requested domain against our block list and uses <a href="https://docs.ebpf.io/linux/concepts/maps/">eBPF Maps</a> to communicate with the <code>CGROUP_SKB</code> program, allowing or denying the request accordingly.</p>



<p>If you&rsquo;d like to dig into the code, here&rsquo;s <a href="https://github.com/lawrencegripper/ebpf-cgroup-firewall/">an early proof of concept</a> we put together. Our current implementation has progressed since then, but this should serve as a good intro.</p>



<p>Like any fun project, the deeper we got, the more we realized we could do.</p>



<p>For example, could we correlate blocked DNS requests back to the specific command or process that triggered them, so teams could more easily debug and fix issues? Yes, we can!</p>



<p>Inside the <a href="https://docs.ebpf.io/linux/program-type/BPF_PROG_TYPE_CGROUP_SKB/"><code>BPF_PROG_TYPE_CGROUP_SKB</code> program type</a>, we have <a href="https://docs.ebpf.io/linux/program-context/__sk_buff/">the <code>skb_buff</code></a> from which we can pull the <a href="https://beta.computer-networking.info/syllabus/default/protocols/dns.html">DNS transaction ID</a> and also <a href="https://docs.ebpf.io/linux/helper-function/bpf_get_current_pid_tgid/">capture the Process ID</a> (PID) that initiated the request. We place this information into another eBPF Map tracking <code>DNS Transaction ID -&gt; Process ID</code>.</p>



<p>Here is a simplified version of the eBPF code (see this <a href="https://github.com/lawrencegripper/ebpf-cgroup-firewall/blob/main/pkg/ebpf/bpf.c#L338-L360">PoC code</a> for full example):</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>  __u32 pid = bpf_get_current_pid_tgid() &gt;&gt; 32; 

     __u16 skb_read_offset = sizeof(struct iphdr) + sizeof(struct udphdr); 

     __u16 dns_transaction_id = 

         get_transaction_id_from_dns_header(skb, skb_read_offset); 

 

     if (pid &amp;&amp; dns_transaction_id != 0) { 

       bpf_map_update_elem(&amp;dns_transaction_id_to_pid, &amp;dns_transaction_id, 

                           pid, BPF_ANY); 

     } </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>As we&rsquo;re redirecting all DNS calls to our userspace DNS proxy, we can look at the transaction ID of each request, find the domain being resolved, and lookup in the eBPF Map to see which process made the request. By reading <code>/proc/{PID}/cmdline</code>, we can even extract the full command line that triggered the request.</p>



<p>Then we can output a log line with all the information:</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>&gt; WARN DNS BLOCKED reason=FromDNSRequest blocked=true blockedAt=dns domain=github.com. pid=266767 cmd="curl github.com " firewallMethod=blocklist</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>With that, we&rsquo;re done.</p>



<p>We can now:</p>



<ul class="wp-block-list">
<li>Conditionally block domains that would cause circular dependencies from deployment scripts.</li>



<li>Inform the owning team which command triggered the blocked request.</li>



<li>Provide an audit list of all domains contacted during a deployment.</li>



<li>Use the cGroups to enforce CPU and memory limits on deploy scripts, preventing runaway resource usage from impacting workloads.</li>
</ul>



<h2 class="wp-block-heading" id="h-what-s-next">What&rsquo;s next?</h2>



<p>Our new circular dependency detection process is live after a six-month rollout.</p>



<p>Now, if a team accidentally adds a problematic dependency, or if an existing binary tool we use takes a new dependency, the tooling will detect that problem and flag it to the team.</p>



<p>The net result is a more stable GitHub and faster mean time to recovery during incidents (due to the removal of these circular dependencies).</p>



<p>Are there ways for circular dependencies to still trip things up? You bet&mdash;and we&rsquo;ll look to improve the tool as we discover them.</p>



<h2 class="wp-block-heading" id="h-want-to-dive-in">Want to dive in?</h2>



<p>Has this piqued your interest in what you might be able to do with eBPF?</p>



<p>Get started by having a look through the examples in <a href="https://github.com/cilium/ebpf/tree/main/examples">cilium/ebpf</a> and the great documentation on the <a href="http://docs.ebpf.io">docs.ebpf.io</a> site.</p>



<p>If you&rsquo;re not quite ready to start writing your own eBPF tools, try open source tools powered by eBPF, like <a href="https://bpftrace.org/tutorial-one-liners#lesson-3-file-opens">bpftrace for deep tracing</a> or <a href="https://github.com/mozillazg/ptcpdump">ptcpdump to get TCP dumps</a> with container-level metadata.</p>

<p>The post <a href="https://github.blog/engineering/infrastructure/how-github-uses-ebpf-to-improve-deployment-safety/">How GitHub uses eBPF to improve deployment safety</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
