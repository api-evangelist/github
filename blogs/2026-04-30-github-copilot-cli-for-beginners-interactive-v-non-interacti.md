---
title: "GitHub Copilot CLI for Beginners: Interactive v. non-interactive mode"
url: "https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-interactive-v-non-interactive-mode/"
date: "Thu, 30 Apr 2026 16:09:02 +0000"
author: "Kayla Cinnamon"
feed_url: "https://github.blog/feed/"
---
<p>Welcome to GitHub Copilot CLI for Beginners! In this series (available in <a href="https://www.youtube.com/playlist?list=PL0lo9MOBetEHvO-spzKBAITkkTqv4RvNl">video</a> and <a href="https://github.blog/tag/github-copilot-cli-for-beginners/">blog</a> format), we&rsquo;ll give you everything you need to get started using <a href="https://github.com/features/copilot/cli?utm_source=blog-cli-beginners-ep2-features-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026" rel="noreferrer noopener" target="_blank">GitHub Copilot CLI</a>, from your first prompt to tips for navigating the command line like a pro!</p>



<p>In this blog, we&rsquo;ll cover the two main modes of the CLI: interactive and non-interactive. You&rsquo;ll learn the differences between the two modes, how to enter them, and what they&rsquo;re most useful for.</p>



<p>Let&rsquo;s dive in!</p>



<h2 class="wp-block-heading" id="h-what-is-github-copilot-cli-interactive-mode">What is GitHub Copilot CLI interactive mode?</h2>



<p>Interactive mode is a back-and-forth, chat-like experience. When you launch Copilot CLI with Copilot, you&rsquo;re already in interactive mode&mdash;that&rsquo;s the default. Non-interactive mode is a separate option for when you want a quick, one-off answer without entering a session. (More on non-interactive mode later!)</p>



<p>In interactive mode, you can ask GitHub Copilot a question, review its response, and then either follow up with questions or another prompt&mdash;all within the same session. This is the mode for those who want to work hands-on with Copilot and iterate as you go.</p>



<p>Here&rsquo;s how to enter interactive mode:</p>



<ul class="wp-block-list">
<li>From the command line, type <code>copilot</code> and hit <kbd>Enter</kbd>.</li>



<li>Copilot may ask you to trust this folder, because it needs permission to read and modify files.</li>



<li>Ask Copilot a question, like &ldquo;How do I run this project locally?&rdquo;</li>



<li>Copilot will give you instructions, which you can do on your own. But if you want to work collaboratively, you can ask Copilot: &ldquo;Can you run it for me?&rdquo;</li>



<li>Copilot will analyze your project and then start the server.</li>



<li>We can review our project, decide what changes we want, and continue working with Copilot, all in the same session.</li>
</ul>



<h2 class="wp-block-heading" id="h-what-is-github-copilot-cli-non-interactive-mode">What is GitHub Copilot CLI non-interactive mode?</h2>



<p>On the other hand, non-interactive mode is designed for speed and simplicity. Instead of having to enter a full session, you pass a single prompt right in the command line and get a response almost immediately, without needing to follow up with Copilot.</p>



<p>Designed as an in-line experience, this mode is perfect for quick, one-shot prompts like summarizing a repository, generating code snippets, or plugging Copilot into automated workflows, without leaving your shell context. Once you get an answer, you&rsquo;re right back in your terminal flow.</p>



<p>Here&rsquo;s how to enter non-interactive mode:</p>



<ul class="wp-block-list">
<li>Start at the regular command line (if you&rsquo;re in Copilot, you&rsquo;ll need to exit).</li>



<li>Type <code>copilot -p</code> and prompt the agent with something like &ldquo;Quickly summarize what this repository does and the key folders.&rdquo;</li>



<li>Copilot will sift through your project files to provide an answer. Ta-da! &#10024;</li>
</ul>



<p>Together, these two modes help you tackle all kinds of projects efficiently: interactive for explorative, deeper work, and non-interactive for fast, focused results when you already know exactly what you need.</p>



<h2 class="wp-block-heading" id="how-to-resume-a-previous-copilot-session">How to resume a previous Copilot session</h2>



<p>Sometimes, you may want to pick up right where you left off in a previous Copilot session, while retaining all the context from that conversation.</p>



<p>If you&rsquo;re in interactive mode, you can type <code>/resume</code> into the command line and Copilot will let you choose a previous session from a list. If you want to launch directly into the previous session picker from non-interactive mode, use <code>copilot --resume</code>.</p>



<p>It only takes one command to pick back up with Copilot, which is super useful if you already know what session you want to work in.</p>



<p>Take this with you GitHub Copilot CLI interactive and non-interactive modes are the fastest ways to prompt Copilot directly from your terminal. Having the option to pick between back-and-forth coding and quick prompting means you can work with Copilot, the way you want.</p>



<p>Keep an eye out for more videos in the GitHub Copilot CLI for Beginners series, where we&rsquo;ll explore:</p>



<ul class="wp-block-list">
<li>Copilot CLI slash commands</li>



<li>Using MCP servers with Copilot CLI</li>



<li>And more!</li>
</ul>



<p>Happy coding!</p>



<div class="wp-block-group post-content-cta has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<p><strong>Looking to try GitHub Copilot CLI?</strong> <a href="https://docs.github.com/copilot/concepts/agents/about-copilot-cli?utm_source=blog-cli-beginners-ep2-features-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026" rel="noreferrer noopener" target="_blank">Read the Docs</a> and <a href="https://github.com/features/copilot/cli?utm_source=blog-cli-beginners-ep2-features-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026" rel="noreferrer noopener" target="_blank">get started</a> today.</p>
</div>



<h3 class="wp-block-heading" id="h-more-resources-to-explore">More resources to explore:</h3>



<ul class="wp-block-list">
<li><a href="https://www.youtube.com/playlist?list=PL0lo9MOBetEHvO-spzKBAITkkTqv4RvNl">GitHub Copilot CLI for Beginners video series</a></li>



<li><a href="https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-getting-started-with-github-copilot-cli/">GitHub Copilot CLI for Beginners: Getting started with GitHub Copilot CLI</a></li>



<li><a href="https://github.blog/ai-and-ml/github-copilot-cli-101-how-to-use-github-copilot-from-the-command-line/?utm_source=blog-announcement-cli-tutorial&amp;utm_medium=blog&amp;utm_campaign=universe25post">GitHub Copilot CLI 101: how to use GitHub Copilot from the command line</a></li>



<li><a href="https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices?utm_campaign=copilot-brand&amp;utm_medium=sem&amp;utm_source=google&amp;ocid=AIDcmmh2h80ugd_SEM__k_CjwKCAjw-dfOBhAjEiwAq0RwI0TIeyL9bjDmXlY26JKPbDvHGzBcaZUa4LR8u8SJuGbIke6e7U2YXRoCzGQQAvD_BwE_k_cli?utm_source=blog-cli-beginners-ep2-features-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026" rel="noreferrer noopener" target="_blank">Best practices for GitHub Copilot CLI</a></li>
</ul>

<p>The post <a href="https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-interactive-v-non-interactive-mode/">GitHub Copilot CLI for Beginners: Interactive v. non-interactive mode</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
