---
title: "Securing the git push pipeline: Responding to a critical remote code execution vulnerability"
url: "https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/"
date: "Tue, 28 Apr 2026 15:30:00 +0000"
author: "Alexis Wales"
feed_url: "https://github.blog/feed/"
---
<p>On March 4, 2026, we received a vulnerability report through our <a href="https://bounty.github.com">Bug Bounty program</a> from researchers at Wiz describing a critical remote code execution vulnerability affecting github.com, GitHub Enterprise Cloud, GitHub Enterprise Cloud with Data Residency, GitHub Enterprise Cloud with Enterprise Managed Users, and GitHub Enterprise Server.</p>



<p>In less than two hours we had validated the finding, deployed a fix to github.com, and begun a forensic investigation that concluded <strong>there was no exploitation</strong>.</p>



<p>In this post, we want to share what happened, how we responded, and what we are doing to prevent similar issues in the future.</p>



<h2 class="wp-block-heading" id="h-receiving-the-bug-bounty-report">Receiving the bug bounty report</h2>



<p>The bug bounty report described a way for any user with push access to a repository, including a repository they created themselves, to achieve arbitrary command execution on the GitHub server handling their <code>git push</code> operation. The attack required only a single command: <code>git push</code> with a crafted push option that leveraged an unsanitized character.</p>



<p>Our security team immediately began validating the bug bounty report. Within 40 minutes, we had reproduced the vulnerability internally and confirmed the severity. This was a critical issue that required immediate action.</p>



<h2 class="wp-block-heading" id="h-understanding-the-vulnerability">Understanding the vulnerability</h2>



<p>When a user pushes code to GitHub, the operation passes through multiple internal services. As part of this process, metadata about the push, such as the repository type and the environment it should be processed in, is passed between services using an internal protocol.</p>



<p>The vulnerability leveraged how user-supplied <a href="https://git-scm.com/docs/git-push#Documentation/git-push.txt---push-option">git push options</a> were handled within this metadata. Push options are an intentional feature of git that allow clients to send key-value strings to the server during a push. However, the values provided by the user were incorporated into the internal metadata without sufficient sanitization. Because the internal metadata format used a delimiter character that could also appear in user input, an attacker could inject additional fields that the downstream service would interpret as trusted internal values.</p>



<p>By chaining several injected values together, the researchers demonstrated that an attacker could override the environment the push was processed in, bypass sandboxing protections that normally constrain hook execution, and ultimately execute arbitrary commands on the server.</p>



<h2 class="wp-block-heading" id="h-responding-to-the-vulnerability">Responding to the vulnerability</h2>



<p>With the root cause identified on March, 4, 2026, at 5:45 p.m. UTC, our engineering team developed and deployed a fix to github.com at 7:00 p.m. UTC that same day. The fix ensures that user-supplied push option values are properly sanitized and can no longer influence internal metadata fields.</p>



<p>For GitHub Enterprise Server, we prepared patches across all supported releases (3.14.25, 3.15.20, 3.16.16, 3.17.13, 3.18.7, 3.19.4, 3.20.0, or later) and published <a href="https://www.cve.org/cverecord?id=CVE-2026-3854">CVE-2026-3854</a>. These are available today and we strongly recommend that all GHES customers upgrade immediately.</p>



<h2 class="wp-block-heading" id="investigating-for-exploitation">Investigating for exploitation</h2>



<p>With the immediate fix in place on github.com, we moved to the pressing question of whether anyone else found and exploited this vulnerability before the researchers reported it.</p>



<p>A key property of this vulnerability gave us confidence in our ability to answer that question. The exploit forces the server to take a code path that is never used during normal operations on github.com. This is not something an attacker can avoid or suppress, as it is an inherent consequence of how the injection works.</p>



<p>We logged this path and queried our telemetry for any instance of this anomalous code path being executed. The results were clear:</p>



<ul class="wp-block-list">
<li>Every occurrence mapped to the Wiz researchers&rsquo; own testing activity.</li>



<li>No other users or accounts triggered this code path.</li>



<li>No customer data was accessed, modified, or exfiltrated as a result of this vulnerability.</li>
</ul>



<p>For GHES customers, exploitation would require an authenticated user with push access on your instance. We recommend reviewing your access logs out of an abundance of caution.</p>



<h2 class="wp-block-heading" id="defense-in-depth">Defense in depth</h2>



<p>Beyond fixing the immediate input sanitization issue, our investigation surfaced an additional finding worth sharing.</p>



<p>The exploit worked in part because the server had access to a code path that was not intended for the environment it was running in. This code path existed on disk as part of the server&rsquo;s container image, even though it was only meant to be used in a different product configuration. An older deployment method had correctly excluded this code, but when the deployment model changed, the exclusion was not carried forward.</p>



<p>This is a useful reminder that defense in depth matters. The input sanitization fix is the primary remediation, but we have also removed the unnecessary code path from environments where it should not exist. Even if a similar injection vulnerability were discovered in the future, this additional hardening would limit what an attacker could do with it.</p>



<h2 class="wp-block-heading" id="what-you-should-do">What you should do</h2>



<p><strong>GitHub Enterprise Cloud</strong>, <strong>GitHub Enterprise Cloud with Enterprise Managed Users</strong>, <strong>GitHub Enterprise Cloud with Data Residency</strong>, and <strong>github.com</strong> were patched on March 4, 2026. No action is required from users of any of these.</p>



<p>As mentioned previously, exploitation on <strong>GitHub Enterprise Server</strong> requires an authenticated user with push access on your instance. We recommend that you review <code>/var/log/github-audit.log</code> for push operations containing <code>;</code> in push options. Updates are available in the following releases:</p>



<ul class="wp-block-list">
<li>GitHub Enterprise Server 3.14.25 or later</li>



<li>GitHub Enterprise Server 3.15.20 or later</li>



<li>GitHub Enterprise Server 3.16.16 or later</li>



<li>GitHub Enterprise Server 3.17.13 or later</li>



<li>GitHub Enterprise Server 3.18.7 or later</li>



<li>GitHub Enterprise Server 3.19.4 or later</li>



<li>GitHub Enterprise Server 3.20.0 or later</li>
</ul>



<p>We strongly recommend upgrading to the latest patch release as soon as possible. See the <a href="https://docs.github.com/en/enterprise-server/admin/release-notes">GHES release notes</a> for details.</p>



<p>This vulnerability has been assigned <a href="https://www.cve.org/cverecord?id=CVE-2026-3854">CVE-2026-3854</a>.</p>



<h2 class="wp-block-heading" id="acknowledgments">Acknowledgments</h2>



<p>This vulnerability was discovered and responsibly disclosed by researchers at <a href="https://www.wiz.io">Wiz</a>. Their report was thorough, clearly demonstrated the impact, and enabled us to move quickly from validation to remediation. This finding will receive one of the highest rewards in the history of our <a href="https://bounty.github.com/">Bug Bounty program</a>, which has been a cornerstone of our security program for over a decade.</p>

<p>The post <a href="https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/">Securing the git push pipeline: Responding to a critical remote code execution vulnerability</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
