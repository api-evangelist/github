---
title: "An update on GitHub availability"
url: "https://github.blog/news-insights/company-news/an-update-on-github-availability/"
date: "Tue, 28 Apr 2026 10:01:37 +0000"
author: "Vlad Fedorov"
feed_url: "https://github.blog/feed/"
---
<p>I wanted to give an update on GitHub&rsquo;s availability in light of <a href="#h-recent-incidents">two recent incidents</a>. Both of those incidents are not acceptable, and we are sorry for the impact they had on you. I wanted to share some details on them, as well as explain what we&rsquo;ve done and what we&rsquo;re doing to improve our reliability.</p>



<p>We started executing our plan to increase GitHub&rsquo;s capacity by 10X in October 2025 with a goal of substantially improving reliability and failover. By February 2026, it was clear that we needed to design for a future that requires 30X today&rsquo;s scale.</p>



<p>The main driver is a rapid change in how software is being built. Since the second half of December 2025, agentic development workflows have accelerated sharply. By nearly every measure, the direction is already clear: repository creation, pull request activity, API usage, automation, and large-repository workloads are all growing quickly.</p>



<figure class="wp-block-image size-full"><img alt="Three line graphs showing record acceleration of pull requests merged (peaking at 90M), commits (peaking at 1.4B), and new repos per month (20M)." class="wp-image-95628" height="1080" src="https://github.blog/wp-content/uploads/2026/04/record-accelleration-1920x1080-2.png?resize=1920%2C1080" width="1920" /></figure>



<p>This exponential growth does not stress one system at a time. A pull request can touch Git storage, mergeability checks, branch protection, GitHub Actions, search, notifications, permissions, webhooks, APIs, background jobs, caches, and databases. At high scale, small inefficiencies compound: queues deepen, cache misses become database load, indexes fall behind, retries amplify traffic, and one slow dependency can affect several product experiences.</p>



<p>Our priorities are clear: availability first, then capacity, then new features. We are reducing unnecessary work, improving caching, isolating critical services, removing single points of failure, and moving performance-sensitive paths into systems designed for these workloads. This is distributed systems work: reducing hidden coupling, limiting blast radius, and making GitHub degrade gracefully when one subsystem is under pressure. We&rsquo;re making progress quickly, but these incidents are examples of where there&rsquo;s still work to do.</p>



<h2 class="wp-block-heading" id="h-what-we-re-doing">What we&rsquo;re doing</h2>



<p>Short term, we had to resolve a variety of bottlenecks that appeared faster than expected from moving webhooks to a different backend (out of MySQL), redesigning user session cache to redoing authentication and authorization flows to substantially reduce database load. We also leveraged our migration to Azure to stand up a lot more compute.</p>



<p>Next we focused on isolating critical services like git and GitHub Actions from other workloads and minimizing the blast radius by minimizing single points of failure. This work started with careful analysis of dependencies and different tiers of traffic to understand what needs to be pulled apart and how we can minimize impact on legitimate traffic from various attacks. Then we addressed those in order of risk. Similarly, we accelerated parts of migrating performance or scale sensitive code out of Ruby monolith into Go.</p>



<p>While we were already in progress of migrating out of our smaller custom data centers into public cloud, we started working on path to multi cloud. This longer-term measure is necessary to achieve the level of resilience, low latency, and flexibility that will be needed in the future.</p>



<p>The number of repositories on GitHub is growing faster than ever, but a much harder scaling challenge is the rise of large monorepos. For the last three months, we&rsquo;ve been investing heavily in response to this trend both within git system and in the pull request experience.</p>



<p>We will have a separate blog post soon describing extensive work we&rsquo;ve done and the new upcoming API design for greater efficiency and scale. As part of this work, we have invested in optimizing merge queue operations, since that is key for repos that have many thousands of pull requests a day.</p>



<h2 class="wp-block-heading" id="h-recent-incidents">Recent incidents</h2>



<p>The two recent incidents were different in cause and impact, but both reflect why we are increasing our focus on availability, isolation, and blast-radius reduction.</p>



<h3 class="wp-block-heading" id="h-april-23-merge-queue-incident">April 23 merge queue incident</h3>



<p>On April 23, pull requests experienced a regression affecting merge queue operations.</p>



<p>Pull requests merged through merge queue using the squash merge method produced incorrect merge commits when a merge group contained more than one pull request. In affected cases, changes from previously merged pull requests and prior commits were inadvertently reverted by subsequent merges.</p>



<p>During the impact window, 658 repositories and 2,092 pull requests were affected. We initially shared slightly higher numbers because our first assessment was intentionally conservative. The issue did not affect pull requests merged outside merge queue, nor did it affect merge queue groups using merge or rebase methods.</p>



<p>There was no data loss: all commits remained stored in Git. However, the state of affected default branches was incorrect, and we could not safely repair every repository automatically. More details are available in the incident root cause analysis.</p>



<p>This incident exposed multiple process failures, and we are changing those processes to prevent this class of issue from recurring.</p>



<h3 class="wp-block-heading" id="h-april-27-search-related-incident">April 27 search-related incident</h3>



<p>On April 27, an incident affected our Elasticsearch subsystem, which powers several search-backed experiences across GitHub, including parts of pull requests, issues, and projects.</p>



<p>We are still completing the root cause analysis and will publish it shortly. What we know now is that the cluster became overloaded (likely due to a botnet attack) and stopped returning search results. There was no data loss, and Git operations and APIs were not impacted. However, parts of the UI that depended on search showed no results, which caused a significant disruption.</p>



<p>This is one of the systems we had not yet fully isolated to eliminate as a single point of failure, because other areas had been higher in our risk-prioritized reliability work. That impact is unacceptable, and we are using the same dependency and blast-radius analysis described above to reduce the likelihood and impact of this type of failure in the future.</p>



<h2 class="wp-block-heading" id="h-increasing-transparency">Increasing transparency</h2>



<p>We have also heard clear feedback that customers need greater transparency during incidents.</p>



<p>We recently <a href="https://github.blog/news-insights/company-news/bringing-more-transparency-to-githubs-status-page/">updated</a> the <a href="https://www.githubstatus.com/">GitHub status page</a> to include availability numbers. We have also committed to statusing incidents both large and small, so you do not have to guess whether an issue is on your side or ours.</p>



<p>We are continuing to improve how we categorize incidents so that the scale and scope are easier to understand. We are also working on better ways for customers to report incidents and share signals with us during disruptions.</p>



<h2 class="wp-block-heading" id="h-our-commitment">Our commitment</h2>



<p>GitHub&rsquo;s role has always been to support developers on an open and extensible platform.</p>



<p>The team at GitHub is incredibly passionate about our work. We hear the pain you&rsquo;re experiencing. We read every email, social post, support ticket, and we take it all to heart. We&rsquo;re sorry.</p>



<p>We are committed to improving availability, increasing resilience, scaling for the future of software development, and communicating more transparently along the way.</p>



<p><em>Editor&rsquo;s note: This post was updated on April 28, 2026, to update the number of repos affected during the April 23 incident.</em></p>

<p>The post <a href="https://github.blog/news-insights/company-news/an-update-on-github-availability/">An update on GitHub availability</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
