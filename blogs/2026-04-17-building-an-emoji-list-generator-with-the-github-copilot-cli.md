---
title: "Building an emoji list generator with the GitHub Copilot CLI"
url: "https://github.blog/ai-and-ml/github-copilot/building-an-emoji-list-generator-with-the-github-copilot-cli/"
date: "Fri, 17 Apr 2026 18:00:00 +0000"
author: "Cassidy Williams"
feed_url: "https://github.blog/feed/"
---
<p>Every week, the GitHub team runs&nbsp;<a href="https://www.youtube.com/@GitHub/streams">a stream called Rubber Duck Thursdays</a>, where we build projects live, cowork with our community, and answer questions!</p>



<p>This week, we built a very fun project together using the&nbsp;<a href="https://github.com/features/copilot/cli?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">GitHub Copilot CLI</a>! Let me tell you about it.</p>



<p>&#128161;&nbsp;<em>New to GitHub Copilot CLI?&nbsp;<a href="https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-getting-started-with-github-copilot-cli/">Here&rsquo;s how to get started.</a></em></p>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">

</div></figure>



<h2 class="wp-block-heading" id="what-is-it">What is it?</h2>



<p>In a lot of social media tweets and launches, you often see accounts post things like:</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>We shipped the most amazing emoji list generator ever. It:

&#128187; Works in the CLI
&#129302; Uses the Copilot SDK to intelligently convert your bullet points to relevent emoji
&#128203; Copies the result to the clipboard</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>It&rsquo;s beautiful. But coming up with the perfect emoji is far too slow for me in this &ldquo;move fast and break things&rdquo; world. I have projects to build! Repos to vibe! Pull requests to merge! I can&rsquo;t be thinking about emojis!</p>



<p>And thus, on the stream, we build an emoji list generator (very descriptively called Emoji List Generator) that:</p>



<p>&#128421;&#65039; Runs in the terminal<br />&#128203; You paste or write a list<br />&#9000;&#65039; You hit Ctrl + S<br />&#128206; You get the list on your clipboard</p>



<p>(Can you tell I&rsquo;m dogfooding the product here?)</p>



<h2 class="wp-block-heading" id="how-we-built-it">How we built it</h2>



<p>We used a few cool technologies for this project:</p>



<p>&#128421;&#65039;&nbsp;<code>@opentui/core</code>for the terminal UI<br />&#129302;&nbsp;<code>@github/copilot-sdk</code>for the AI brain<br />&#128203;&nbsp;<code>clipboardy</code>for clipboard access</p>



<p>To start the project off, we opened up the GitHub Copilot CLI.</p>



<p>In plan mode using Claude Sonnet 4.6, we wrote:</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>I want to create an AI-powered markdown emoji list generator. Where, in this CLI app, if I paste in or write in some bullet points, it will replace those bullet points with relevant emojis to the given point in that list, and copies it to my clipboard. I'd like it to use GitHub Copilot SDK for the AI juiciness.</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>Copilot asked me a bunch of clarifying questions, for example around the tech stack and what libraries we should use (shoutout to&nbsp;<a href="https://javorszky.co.uk/">Gabor</a>&nbsp;in the chat for suggesting&nbsp;<a href="https://opentui.com/">OpenTUI</a>), and from there, we had a fully thought-out&nbsp;<code>plan.md</code>file for me to review and use!</p>



<p>We implemented the plan using Claude Opus 4.7 (which was&nbsp;<a href="https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available/">recently released</a>!) and a few minutes later, voil&agrave;, we had a fun little terminal UI to work with!</p>



<figure class="wp-block-image size-full"><img alt="Screenshot of the 'Emoji List Generator.' Paste or type your bullet points below. Press CTRL + S to generate, CTRL + C to quit.

Your bullet points
- Is there a ghost here?
- Ducks quack a lot
- I would like to have a word with the moon
- Mechanical keyboards are cool
- We just launched a sick new feature
- I'd like to squish some slime

Followed by the same list, with appropriate emojis." class="wp-image-95404" height="1944" src="https://github.blog/wp-content/uploads/2026/04/list.png?resize=1869%2C1944" width="1869" /></figure>



<p>The project was small but mighty. In the CLI, we used some really cool tools all together:</p>



<p>&#128203;&nbsp;<a href="https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026#plan-mode">Plan mode</a><br />&#129302;&nbsp;<a href="https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">Autopilot mode</a><br />&#128256;&nbsp;<a href="https://docs.github.com/copilot/reference/ai-models/supported-models?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">Multi-model</a>&nbsp;workflow<br />&#128681;&nbsp;<a href="https://docs.github.com/copilot/how-tos/copilot-cli/allowing-tools#permissive-options?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">The&nbsp;<code>allow-all</code>tools flag</a><br />&#128025; The&nbsp;<a href="https://github.com/github/github-mcp-server?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">GitHub MCP server</a></p>



<p>If you&rsquo;d like to build a project like this yourself, you can check out the docs for&nbsp;<a href="https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">the GitHub Copilot CLI</a>&nbsp;and the&nbsp;<a href="https://docs.github.com/copilot/how-tos/copilot-sdk/sdk-getting-started?utm_source=blog-rdt-emoji-list-cta&amp;utm_medium=blog&amp;utm_campaign=dev-pod-copilot-cli-2026">GitHub Copilot SDK</a>&nbsp;today!</p>



<p>The&nbsp;<a href="https://github.com/cassidoo/emoji-list-generator">emoji list generator is free and open source</a>, just for you.</p>



<p>Happy building!</p>

<p>The post <a href="https://github.blog/ai-and-ml/github-copilot/building-an-emoji-list-generator-with-the-github-copilot-cli/">Building an emoji list generator with the GitHub Copilot CLI</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
