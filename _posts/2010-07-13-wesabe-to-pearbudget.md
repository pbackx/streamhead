---
id: 2420
title: How to Move From Wesabe to the PearBudget Spreadsheet
date: 2010-07-13T10:00:38+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2420
permalink: /wesabe-to-pearbudget/
dsq_thread_id:
  - "117319775"
image: /wp-content/uploads/2010/07/budget.png
categories:
  - Graphics, Visuals and Texts
---
Two weeks ago <a title="twitter status update" href="http://twitter.com/pbackx/status/17643323144" target="_blank">I discovered that Wesabe will shut down at the end of July</a>. Wesabe was the tool I used to track and budget my expenses. Without as much as an e-mail, the Wesabe owners decided to give us a one month notice. Some promises for more export tools were made, but have not yet materialized. Considering the value of the data that they kept, I must say I am thoroughly disappointed. Obviously, if you run out of money, there&#8217;s not much you can do, but still, a business plan might have been a wise investment.

Anyway, I&#8217;m not here to discuss the potential pitfalls of cloud services. <a title="how stable are those apis" href="http://www.streamhead.com/beware-web-20-developer-stable-apis/" target="_blank">I&#8217;ve been there</a> and <a title="Fuck the cloud" href="http://ascii.textfiles.com/archives/1717" target="_blank">others have done it better</a>. I&#8217;m here to show you the way out that I took. I exported everything to Excel. I used the PearBudget spreadsheet and used the Excel to set everything up. Sadly I haven&#8217;t yet figured out an easy way to import existing data, but at least I now have a backup of everything that was on Wesabe.

<!--more-->

First things first, PearBudget is now an online tool, but it started as an extremely useful budgeting spreadsheet that can still be downloaded (and is even maintained from time to time). <a title="PearBudget spreadsheet" href="https://www.pearbudget.com/spreadsheet" target="_blank">You can download it from the PearBudget site</a>. All the documentation you need is on the first worksheet.

## Exporting from Wesabe

To get started, I exported all my data from Wesabe to CSV: there&#8217;s a &#8220;download your data&#8221; link on your profile page. Importing in Excel 2007 was a little different than it used to be:

  * Create a new Excel document
  * Click on &#8220;data&#8221; and import &#8220;from text&#8221;
  * In the popup, you can select the file you downloaded from Wesabe
  * Check &#8220;delimited&#8221; and in the second step choose &#8220;comma&#8221; as delimiter
  * Click finish and your data will show up on the worksheet

## Extracting expenses categories

On Wesabe, I used to tag all my expenses with the category to which they belonged. This allowed me to create budget. I don&#8217;t think every one used Wesabe like that, but I presume it was the most popular way of budgeting.

So I wanted to extract the unique tags in order to set up my expense categories:

  * Copy the tags column to a different worksheet
  * Remove the &#8220;Tags&#8221; header
  * Select the column and in &#8220;data&#8221;, I choose &#8220;Advanced filter&#8221;
  * Select the &#8220;Unique records only&#8221; checkbox
  * and you&#8217;ve got a list of unique tags

Those can now be used as a basis for the expense categories. I used this chance to tweak them a little.

## Importing data, todo

I&#8217;m not yet sure if I will be importing the data, because it&#8217;s not always suited for the way PearBudget works. For instance, I couldn&#8217;t import my Visa bills into Wesabe, so I never had any details on those transactions. So it&#8217;s still an open issue how I&#8217;m going to deal with that.

One more thing I&#8217;d like to do is create a program to parse my monthly bank statements to an easy format. Seems like a great way to <a title="Learn Python by Creating Games" href="http://www.streamhead.com/learn-programming-language/" target="_blank">test-drive Python</a>.

(<a title="Travel budget" href="http://www.flickr.com/photos/mynameisharsha/4345641826/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->