---
id: 3343
title: ExpensesSpreadsheet.net, Rapid Web App Development with Node.js
date: 2011-11-23T16:00:46+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3343
permalink: /expensesspreadsheet-net-node-js/
amazon_post_template:
  - ""
categories:
  - Java and JavaScript
---
My latest project is [ExpensesSpreadsheet.NET](http://www.expensesspreadsheet.net "Track your expenses the smart way"). It is the simplest and easiest solution I could come up with to track and categorize expenses &#8230; in a spreadsheet. Let&#8217;s call it a niche web application, so it&#8217;s probably not for every one, but it should fit some extremely well. It runs on Heroku&#8217;s Node.js stack.

<!--more-->Over the last month or two, I&#8217;ve been very busy with a few projects. And it was about time to present some. I have many more ideas on how to extend 

**[ExpensesSpreadsheet](http://www.expensesspreadsheet.net "Track your expenses the smart way")**, but I thought it wise to first gauge the reaction of people.

It uses the following technology:

  * **Node.js**, the JavaScript event machine that is all the rage now.
  * **RailwayJS**, a Rails-like web framework.
  * **connect-auth** for Facebook integration (and a lot more)
  * **MongoDB** for data storage. Mostly because it was so easy to get started with compared to traditional related databases. But in hindsight, I think it&#8217;s an ok choice. I really don&#8217;t safe any relations anyway.
  * **EJS** JavaScript templates. Although in hindsight, I think I like Jade better.
  * **Heroku**, cloud hosting done right.

This was my first experiment with Node.js and Heroku and it was extremely enlightening. JavaScript is not my favorite programming language, but it certainly has a way of reducing boiler plate code (stuff I&#8217;m really starting to hate in Java). Combined with deployment to Heroku, the time between idea and deployed application is so short, it will make any developer smile.

If your day-to-day life involves lots of Java, you owe it to yourself to try out this stack. It&#8217;s not your average hacked together client side JavaScript. It takes a little time to wrap your head around the Node model, but it&#8217;s all worth it.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->