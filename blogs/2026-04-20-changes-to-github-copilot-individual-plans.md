---
title: "Changes to GitHub Copilot Individual plans"
url: "https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/"
date: "Mon, 20 Apr 2026 18:15:28 +0000"
author: "Joe Binder"
feed_url: "https://github.blog/feed/"
---
<p>Today we&rsquo;re making the following changes to GitHub Copilot&rsquo;s Individual plans to protect the experience for existing customers: pausing new sign-ups, tightening usage limits, and adjusting model availability. We know these changes are disruptive, and we want to be clear about why we&rsquo;re making them and how they will affect you.</p>



<p>Agentic workflows have fundamentally changed Copilot&rsquo;s compute demands. Long-running, parallelized sessions now regularly consume far more resources than the original plan structure was built to support. As Copilot&rsquo;s agentic capabilities have expanded rapidly, agents are doing more work, and more customers are hitting usage limits designed to maintain service reliability. Without further action, service quality degrades for everyone.</p>



<p>We&rsquo;ve heard your frustrations about usage limits and model availability, and we need to do a better job communicating the guardrails we are adding&mdash;here&rsquo;s what&rsquo;s changing and why.</p>



<ol class="wp-block-list">
<li><strong>New sign-ups for GitHub Copilot Pro, Pro+, and Student plans are paused</strong>. Pausing sign-ups allows us to serve existing customers more effectively.</li>



<li><strong>We are tightening usage limits for individual plans</strong>. Pro+ plans offer more than 5X the limits of Pro. Users on the Pro plan who need higher limits can upgrade to Pro+. Usage limits are now displayed in VS Code and Copilot CLI to make it easier for you to avoid hitting these limits.</li>



<li><strong>Opus models are no longer available in Pro plans</strong>. Opus 4.7 remains available in Pro+ plans. As we announced in our <a href="https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available/">changelog</a>, Opus 4.5 and Opus 4.6 will be removed from Pro+.</li>
</ol>



<p>These changes are necessary to ensure we can serve existing customers with a predictable experience. If you hit unexpected limits or these changes just don&rsquo;t work for you, you can cancel your Pro or Pro+ subscription and receive a refund for the time remaining on your current subscription by visiting your <a href="https://github.com/settings/billing/licensing">Billing settings</a> before May 20.</p>



<h2 class="wp-block-heading" id="h-how-usage-limits-work-in-github-copilot">How usage limits work in GitHub Copilot</h2>



<p>GitHub Copilot has two usage limits today: session and weekly (7 day) limits. Both limits depend on two distinct factors&mdash;token consumption and the model&rsquo;s multiplier.</p>



<p>The session limits exist primarily to ensure that the service is not overloaded during periods of peak usage. They&rsquo;re set so most users shouldn&rsquo;t be impacted. Over time, these limits will be adjusted to balance reliability and demand. If you do encounter a session limit, you must wait until the usage window resets to resume using Copilot.</p>



<p>Weekly limits represent a cap on the total number of tokens a user can consume during the week. We introduced weekly limits recently to control for parallelized, long-trajectory requests that often run for extended periods of time and result in prohibitively high costs.</p>



<p>The weekly limits for each plan are also set so that most users will not be impacted. If you hit a weekly limit and have premium requests remaining, you can continue to use Copilot with Auto model selection. Model choice will be reenabled when the weekly period resets. If you are a Pro user, you can upgrade to Pro+ to increase your weekly limits. Pro+ includes over 5X the limits of Pro.</p>



<p>Usage limits are separate from your premium request entitlements. Premium requests determine which models you can access and how many requests you can make. Usage limits, by contrast, are token-based guardrails that cap how many tokens you can consume within a given time window. You can have premium requests remaining and still hit a usage limit.</p>



<h2 class="wp-block-heading" id="h-avoiding-surprise-limits-and-improving-our-transparency">Avoiding surprise limits and improving our transparency</h2>



<p>Starting today, VS Code and Copilot CLI both display your available usage when you&rsquo;re approaching a limit. These changes are meant to help you avoid a surprise limit.</p>



<figure class="wp-block-image size-large"><img alt="Screenshot of a usage limit being hit in VS Code. A message appears that says 'You've used over 75% of your weekly usage limit. Your limit resets on Apr 27 at 8:00 PM.'" class="wp-image-95447" height="898" src="https://github.blog/wp-content/uploads/2026/04/Screenshot-2026-04-20-at-2.05.12-PM.png?resize=1024%2C898" width="1024" /><figcaption class="wp-element-caption">Usage limits in VS Code</figcaption></figure>



<figure class="wp-block-image size-large"><img alt="A screenshot of a usage limit being hit in GitHub Copilot CLI. A message appears that says '! You've used over 75% of your weekly usage limit. Your limit resets on Apr 24 at 3 PM.'" class="wp-image-95442" height="662" src="https://github.blog/wp-content/uploads/2026/04/image-20.png?resize=1024%2C662" width="1024" /><figcaption class="wp-element-caption">Usage limits in Copilot CLI</figcaption></figure>



<p>If you are approaching a limit, there are a few things you can do to help reduce the chances of hitting it:</p>



<ul class="wp-block-list">
<li>Use a model with <strong>a smaller multiplier for simpler tasks</strong>. The larger the multiplier, the faster you will hit the limit.</li>



<li>Consider <strong>upgrading to Pro+</strong> if you are on a Pro plan to raise your limit by over 5X.</li>



<li>Use <strong>plan mode</strong> (<a href="https://code.visualstudio.com/docs/copilot/concepts/agents#_planning">VS Code</a>, <a href="https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices#2-plan-before-you-code">Copilot CLI</a>) to improve task efficiency. Plan mode also improves task success.</li>



<li><strong>Reduce parallel workflows</strong>. Tools such as <code>/fleet</code> will result in higher token consumption and should be used sparingly if you are nearing your limits.</li>
</ul>



<h2 class="wp-block-heading" id="h-why-we-re-doing-this">Why we&rsquo;re doing this</h2>



<p>We&rsquo;ve seen usage intensify for <em>all</em> users as they realize the value of agents and subagents in tackling complex coding problems. These long-running, parallelized workflows can yield great value, but they have also challenged our infrastructure and pricing structure: it&rsquo;s now common for a handful of requests to incur costs that exceed the plan price! These are our problems to solve. The actions we are taking today enable us to provide the best possible experience for existing users while we develop a more sustainable solution.</p>



<p><em>Editor&rsquo;s note: Updated April 21, 2026, to clarify the refund policy.</em></p>

<p>The post <a href="https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/">Changes to GitHub Copilot Individual plans</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
