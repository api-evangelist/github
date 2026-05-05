---
title: "Bringing more transparency to GitHub’s status page"
url: "https://github.blog/news-insights/company-news/bringing-more-transparency-to-githubs-status-page/"
date: "Fri, 17 Apr 2026 16:00:00 +0000"
author: "Jakub Oleksy"
feed_url: "https://github.blog/feed/"
---
<p>GitHub is where millions of developers do their most important work, and that comes with a responsibility we take seriously. Earlier this year, we shared an update on <a href="https://github.blog/news-insights/company-news/addressing-githubs-recent-availability-issues-2/">GitHub&rsquo;s recent availability issues</a> and the work we&rsquo;re doing to address them. Alongside those reliability investments, we have prioritized improving how we communicate during and after incidents, increasing the specificity of the data we provide and giving better insight into the platform&rsquo;s health overall.</p>



<p>Guided by transparency, accuracy, and timeliness, we&rsquo;re rolling out three changes to how we communicate service health&mdash;outlined below.</p>



<ul class="wp-block-list">
<li>A new <strong>&ldquo;Degraded Performance&rdquo;</strong> state for more accurate incident classification</li>



<li><strong>Per-service uptime metrics</strong> published for each service</li>



<li>More granular insights on service disruptions, starting with a dedicated <strong>&ldquo;Copilot AI Model Providers&rdquo;</strong> component for clearer communication around model provider availability</li>
</ul>



<figure class="wp-block-image size-full"><img alt="Image of the updated GitHub status page." class="wp-image-95366" height="1756" src="https://github.blog/wp-content/uploads/2026/04/image-6.png?resize=2084%2C1756" width="2084" /></figure>



<h2 class="wp-block-heading" id="h-improving-accuracy">Improving accuracy</h2>



<p>We&rsquo;re adding a new incident severity level: <strong>Degraded Performance</strong>. This sits alongside our existing Partial Outage and Major Outage states, creating a three-tier system that more accurately reflects the spectrum of issues that can affect GitHub services.</p>



<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>State&nbsp;</th><th>What It Means&nbsp;</th></tr></thead><tbody><tr><td><strong>Degraded Performance</strong>&nbsp;</td><td>The service is operational but impaired. You may experience elevated latency, reduced functionality, or intermittent errors affecting a small percentage of requests.</td></tr><tr><td><strong>Partial Outage</strong>&nbsp;</td><td>A significant portion&nbsp;of the service is unavailable or severely&nbsp;impacted&nbsp;for a meaningful number of users.</td></tr><tr><td><strong>Major Outage</strong>&nbsp;</td><td>The service is broadly unavailable, affecting most or all users.&nbsp;</td></tr></tbody></table></figure>



<p>Previously, even with minimal service disruption, all incidents were classified at least as a partial outage. This did not accurately reflect customer impact and led users to believe a service was unavailable even if it was still functional.</p>



<h2 class="wp-block-heading" id="h-per-service-uptime-on-the-status-page">Per-service uptime on the status page</h2>



<p>We are now publishing <strong>per-service uptime percentages</strong> over the last 90 days directly on our status page, so you can quickly understand each service&rsquo;s recent reliability track record.</p>



<p>These uptime percentages are calculated based on the number of incidents, their severity, and their duration for each individual service. These calculations are based on industry standard status page calculations.</p>



<p>Each severity level carries a specific downtime weight:</p>



<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th><strong>Severity</strong>&nbsp;</th><th><strong>Downtime&nbsp;weight</strong>&nbsp;</th></tr></thead><tbody><tr><td><strong>Major Outage</strong>&nbsp;</td><td>100% &mdash; the full duration counts as downtime&nbsp;</td></tr><tr><td><strong>Partial Outage</strong>&nbsp;</td><td>30% &mdash; reflects significant but not total service loss&nbsp;</td></tr><tr><td><strong>Degraded Performance</strong>&nbsp;</td><td>0% &mdash; does not count as downtime; the service&nbsp;remains&nbsp;functional&nbsp;</td></tr></tbody></table></figure>



<p>For example, if a service experienced a 1-hour Partial Outage over a 90-day period, that would count as 18 minutes of effective downtime in the uptime calculation&mdash;not the full hour. A Degraded Performance incident, by contrast, would not affect the uptime percentage at all.</p>



<h2 class="wp-block-heading" id="h-insights-on-model-provider-service-disruptions">Insights on model provider service disruptions</h2>



<p>We&rsquo;ve added a new component representing Copilot AI model providers.</p>



<p>Previously, when a model provider experienced an outage, we declared an incident against the Copilot service, even when the impact was limited to a single model. That didn&rsquo;t always reflect your experience, because many Copilot features, such as GitHub Copilot Chat and GitHub Copilot cloud agent (formerly coding agent) support multiple models. On those features, if one model is unavailable, you can choose an alternative model or use <a href="https://docs.github.com/en/copilot/concepts/auto-model-selection">auto model selection</a> to have Copilot pick the best available option for you.</p>



<p>Going forward, incidents related to model availability will be reported under the new <strong>&ldquo;Copilot AI Model Providers&rdquo;</strong> component instead of the broader &ldquo;Copilot&rdquo; component. We&rsquo;ll continue to share details, such as which models are affected, through public incident updates.</p>



<h2 class="wp-block-heading" id="h-our-continued-commitment-to-transparency">Our continued commitment to transparency</h2>



<p>We recognize that clear communication and transparency matter most when things go wrong. The <strong>Degraded Performance</strong> state, <strong>per-service uptime percentages</strong>, and dedicated <strong>Copilot AI Model Providers</strong> component are designed to give you the context and details you need to make confident decisions about your operations.</p>



<p>We know GitHub is critical infrastructure for your teams, and we are committed to ensuring our platform is available when and where you need it; and communicating effectively and transparently when it is not.</p>

<p>The post <a href="https://github.blog/news-insights/company-news/bringing-more-transparency-to-githubs-status-page/">Bringing more transparency to GitHub’s status page</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
