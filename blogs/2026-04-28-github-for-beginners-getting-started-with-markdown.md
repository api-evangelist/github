---
title: "GitHub for Beginners: Getting started with Markdown"
url: "https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-markdown/"
date: "Tue, 28 Apr 2026 18:00:00 +0000"
author: "Kedasha Kerr"
feed_url: "https://github.blog/feed/"
---
<p>Welcome back to GitHub for Beginners. We&rsquo;ve covered a wide range of topics so far this season, including <a href="https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-issues-and-projects/">GitHub Issues and Projects</a>, <a href="https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-actions/">GitHub Actions</a>, <a href="https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-security/">security,</a> and GitHub Pages. Now we&rsquo;re going to teach you everything you need to know to get started with Markdown, the markup language used across GitHub.</p>



<p>Once you learn the basics of how to use Markdown, you&rsquo;ll develop an essential skill that will transform how you write READMEs as well as how to format issues, pull requests, and your agent instruction files. By the end of this post, you&rsquo;ll have the knowledge you need to make your projects and contributions easier for others to explore.</p>



<p>As always, if you prefer to watch the video or want to reference it, we have all of our <a href="https://gh.io/gfb">GitHub for Beginners episodes available on YouTube</a>.</p>



<h2 class="wp-block-heading" id="h-what-is-markdown-and-why-is-it-important">What is Markdown and why is it important?</h2>



<p>Markdown is a lightweight language for formatting plain text. You can use Markdown syntax, along with some additional HTML tags, to format your writing on GitHub. You can do this in repository READMEs, issue and pull request descriptions, and comments on issues and pull requests.</p>



<p>Markdown gives you the ability to create clear, readable documentation. Having a clean README in your project or a well-formatted issue can make a huge difference when someone lands on your content for the first time.</p>



<p>And one of the best parts is that when you get the syntax down, you&rsquo;ll find yourself using it in almost every project you work on!</p>



<h2 class="wp-block-heading" id="h-where-can-i-use-markdown">Where can I use Markdown?</h2>



<p>The most common place where you&rsquo;ll encounter Markdown is in your repository&rsquo;s README file. But you&rsquo;ll also find yourself using it in issues, pull requests, discussions, and even wikis. Any time you write or communicate on GitHub, Markdown is behind the scenes, helping your text look clean and consistent.</p>



<p>Markdown extends beyond GitHub to modern note-taking apps, blog platforms, and documentation tools. It&rsquo;s a widely adopted language used across the technical space, so learning how to use it can benefit you beyond just how you interact with GitHub.</p>



<h2 class="wp-block-heading" id="h-basic-syntax">Basic syntax</h2>



<p>We&rsquo;re going to start with the common features that you&rsquo;ll use the most. While we&rsquo;re going through these, you can try them out to see how they work. The easiest way to do this is by opening a markdown file on your repository.</p>



<ol class="wp-block-list">
<li>Navigate to a repository you own on <a href="https://github.com/">github.com</a>.</li>



<li>Make sure you are on the <strong>Code</strong> tab of your repository.</li>



<li>Click <strong>Add file</strong> near the top of the window and select <strong>Create new file</strong> from the pull-down menu.</li>



<li>In the box at the top of the editor, name your file. Make sure the filename ends in <code>.md</code> (e.g., <code>markdownTestFile.md</code>).</li>



<li>Select the <strong>Edit</strong> button.</li>



<li>Enter any Markdown syntax into the editor window.</li>
</ol>



<p>You can see what the Markdown text you enter will look like by selecting the <strong>Preview</strong> button; there&rsquo;s no need to make a commit unless you want to save your test file. Just select the <strong>Edit</strong> button to go back to editing so you can enter more Markdown text.</p>



<p>Now that you know how to try it out, let&rsquo;s get started with the syntax. First up are headers. These are your title and section names. You create them by adding pound signs (<code>#</code>), also known as hashtags, in front of your text. One pound sign indicates a header, two will create a subheader, and so on.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code># GitHub for Beginners 

 

## Basic Markdown syntax 

 

### Headers </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>If you want to emphasize your text, you can use bold and italic fonts. You create these by using either asterisks (<code>*</code>) or underscores (<code>_</code>). Either of these symbols work in the same way, you just have to make sure to pair them up appropriately. A single character makes text italic, a double character makes text bold, and a triple character makes it both bold and italic. You can emphasize characters within a string or multiple strings within a line of text.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>Here is some *italic text* 

Here is some **bold text** 

___Here is both bold and italic text 

Over multiple lines___</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>Sometimes you may want to quote important text. To do this, add the greater than (<code>&gt;</code>) symbol as the first character in a line of text. If you would like to quote something that spans multiple lines, you need to add the greater than symbol at the start of each individual line.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>&gt; No design skills required. 

&gt; 

&gt; No overthinking allowed. 
&gt; 

&gt; Just ship your work.</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<h2 class="wp-block-heading" id="h-lists">Lists</h2>



<p>Now let&rsquo;s get into something a little more involved: lists.</p>



<p>Lists are a common way to express your steps and procedures in an ordered and unordered manner. To create an ordered list, number each element in the list (i.e. <code>1.</code>, <code>2.</code>, <code>3.</code>, etc.).</p>



<p>While this can be clear to read, what if you want to add an element between two consecutive numbers? The good news is that you don&rsquo;t need to renumber the entire list. Markdown interpreters allow you to order your items with any number, and they automatically interpret it as an ordered list from first to last.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>1. Click the "Use this template&rdquo; button at the top of this repo. 

1. Name your new repository (e.g., my-portfolio). 

1. Clone your new repo and start customizing!</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>For an unordered list, start a line with either a hyphen (<code>-</code>), asterisk (<code>*</code>), or a plus sign (<code>+</code>). Markdown will render any of these characters as the start of an unordered list.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>* Click the "Use this template&rdquo; button at the top of this repo. 

* Name your new repository (e.g., my-portfolio). 

* Clone your new repo and start customizing!</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>If you would like to create nested lists, indent four spaces to start a new indented list. You can do this with both ordered and unordered list items.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>1. Click the "Use this template&rdquo; button. 

    - Located at the top of the repo. 

    - This will create a new repository using this template. 

1. Name your new repository. 

    - e.g., my-portfolio 

    - This can be created under your personal GitHub account. 

1. Clone your new repo and start customizing!</code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>When you&rsquo;re done with your list, hit <strong>Enter</strong> twice to go back to plain text.</p>



<aside class="wp-block-group post-aside--large p-4 p-md-6 is-style-light-dimmed has-global-padding is-layout-constrained wp-block-group-is-layout-constrained is-style-light-dimmed--1" style="border-top-width: 4px;">
<h3 class="wp-block-heading h5-mktg gh-aside-title is-typography-preset-h5" id="h-additional-resources" style="margin-top: 0;">Additional resources</h3>



<p>Check out the GitHub docs for <a href="https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">a cheat sheet on formatting Markdown</a>.</p>



<p>You can also start practicing your Markdown skills today by visiting the <a href="https://github.com/skills/communicate-using-markdown">communicate-using-markdown skills repository</a>. You&rsquo;ll learn how to use Markdown to add lists, images, and links in a GitHub comment or text file.</p>
</aside>



<h2 class="wp-block-heading" id="h-code">Code</h2>



<p>Sometimes you may want to display a snippet of code in your Markdown as an example. This could be for steps in a procedure or as part of your project&rsquo;s installation process. Many Markdown interpreters render code snippets with formatting and syntax highlighting. You can denote code in Markdown by surrounding it with a backtick (<code>`</code>) character.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>`git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git` </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>If you have code that spans multiple lines, you can use three backtick characters to create a code block. Any characters between these triple backticks, including spaces and new lines, will render as code.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code language-plaintext"><code>```bash 

# Clone the repository 

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git 

cd YOUR_REPO_NAME 

 

# Install dependencies 

npm install 

 

# Start the development server 

npm run dev 

``` </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<h2 class="wp-block-heading" id="h-links-and-images">Links and images</h2>



<p>Now let&rsquo;s learn how to spice up our Markdown files. We&rsquo;ll start with links. Links allow you to point people to helpful resources, documentation, or other pages in your project. They&rsquo;re written using brackets (<code>[]</code>) and parentheses (<code>()</code>). Place the text you want to display in the brackets, followed immediately by the URL in parentheses, with no space between the two. This keeps your writing clean and easy to follow.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>Open [your local host](http://localhost:3000) to see your portfolio. </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>Images work in almost the same way, but with one small difference: you need to add an exclamation point (<code>!</code>) at the beginning. This is perfect for adding screenshots, diagrams, or even a project logo to your README.</p>


<div class="wp-block-code-wrapper">
<pre class="wp-block-code"><code>![Mona](https://avatars.githubusercontent.com/u/92997159?v=4) </code></pre>
<svg class="octicon octicon-copy js-clipboard-copy-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg><svg class="octicon octicon-check js-clipboard-check-icon" height="16" version="1.1" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg></div>


<p>To make things even easier, on GitHub, you can just drag-and-drop an image into an issue or pull request, and it automatically generates the right Markdown for you.</p>



<p>Whether you&rsquo;re linking out to a tutorial or showing off a screenshot, links and images help you add that extra bit of personality and clarity to your Markdown.</p>



<h2 class="wp-block-heading" id="h-what-s-next">What&rsquo;s next?</h2>



<p>You now know the basics of Markdown, including what it is, why it matters, where you can use it, and how to start writing it with confidence. With just a few techniques, you can create clean, readable documentation that makes your GitHub projects stand out.</p>



<p>Whether you&rsquo;re building a README, opening an issue, or writing project notes, Markdown is going to be one of the tools you use the most.</p>



<p>If you want to learn more about Markdown, here are some good places to get started:</p>



<ul class="wp-block-list">
<li><a href="https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">Basic formatting syntax</a></li>



<li><a href="https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks">Creating and highlighting code blocks</a></li>



<li><a href="https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github">Quickstart for writing at GitHub</a></li>
</ul>



<p>Happy coding!</p>

<p>The post <a href="https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-markdown/">GitHub for Beginners: Getting started with Markdown</a> appeared first on <a href="https://github.blog">The GitHub Blog</a>.</p>
