---
id: 3827
title: 'Learning Scala, Analyzing Bank Statements (make #1)'
date: 2016-01-09T17:45:46+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3827
permalink: /learning-scala-analyzing-bank-statements-make-1/
pdrp_attributionLocation:
  - tag
image: /wp-content/uploads/2016/01/i-should-cat.jpg
categories:
  - Java and JavaScript
tags:
  - 2016 Maker Challenge
---
Last year, I followed the [Functional Programming course on Coursera by Martin Odersky](https://www.coursera.org/course/progfun). It was a thorough introduction to Scala. Right now I&#8217;m reading [Pragmatic Scala by Venkat Subramaniam](http://amzn.to/1RrS8nK). So it was about time for some actual Scala code.

<!--more-->

This is the first &#8220;make&#8221; I do this year. I&#8217;m joining [Justin Jackson&#8217;s maker challenge](http://megamaker.co/challenge/). While Justin is planning out his challenge, I&#8217;m just going to see where it takes me. I think I can probably make about 12 things this year. The only promise I make, is that I&#8217;m going to write about them. Even if they are very basic in slightly embarrassing.

## Expense Tracking

So back to the project at hand. As an entrepreneur, I&#8217;ve long been interested in figuring out how much I&#8217;m spending and how much of that is really essential. This will allow me to judge when one of my project is [&#8220;ramen profitable&#8221;](http://www.paulgraham.com/ramenprofitable.html).

Over the years, I&#8217;ve tried quite a few ways to track my expenses. Mint didn&#8217;t really work for non-Americans and it has a lot of features I don&#8217;t need and that are just trying to sell me more stuff.

I tried to create a manual option. Make it as easy as possible to enter expenses. That worked up to a point, but having to enter every expense manually was ok for a month or two. After that it got tedious.

## Automated Expense Tracking

So I&#8217;m back to trying to automate it. Seems like a great project for a new programming language.

Based on the bank statements that I can download from my online banking app (in CSV format), the program should categorize expenses.

Important are good and flexible matching rules.

[The current version is not very flexible](https://github.com/pbackx/myexpenses) and certainly not perfect. But it already shows how powerful Scala is. With only a few lines of code, the result is already useful.

There are the two main features I still want to implement:

  * More powerful matching rules (based on Scala&#8217;s powerful pattern matching)
  * Incrementally import new bank statements

[In any case, you can already check it out. Feel free to comment and extend](https://github.com/pbackx/myexpenses).

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->