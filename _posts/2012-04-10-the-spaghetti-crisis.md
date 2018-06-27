---
id: 3428
title: Taking over the Codebase, Solving the Spaghetti Crisis
date: 2012-04-10T16:00:47+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3428
permalink: /the-spaghetti-crisis/
image: /wp-content/uploads/2012/04/spaghetti.png
categories:
  - PHP
---
We&#8217;ve all been there. Somebody asks if you can take a look at their website that has been stagnant for a while. Something small needs to be changed. You feel up for a challenge, so you dive in. What you find is a mess. It&#8217;s really nobody&#8217;s fault. Things evolved over time, different developers and designers have done their thing at various times. Nobody meant any ill will, everybody just did their best. But here you are.

<!--more-->

Those problems come in many forms, but the one that pops up the most is the shared server that&#8217;s running a website for that shop next door. Over the years the owner became more and more reliant on the site. Maybe it contains his master inventory, maybe his contact database. It started out as nice novelty that nobody depended on, but now it&#8217;s quickly becoming mission critical.

So there you are, you&#8217;ve just opened the public HTML folder in your FTP client and you&#8217;ve got PHPMyAdmin opened in the browser.

This is my current action plan, feel free to add and suggest tools.

## Backup the entire site

**For the love of god, make a backup now!** Chances are good that you are looking at **the only copy of the site in existence**. If anything happens with the server, if you mess up something small, you&#8217;re going to be very very sorry.

Both cPanel and Plesk, the most popular domain control panels offer backup solutions out of the box. They are not perfect, but they allow you to create a full dump of the entire site. If you can schedule a daily backup, that&#8217;s a plus. If you can send the backup somewhere off site, another plus.

If you have shell access to the server, there are a whole slew of other tools available that may or may not be easier to use than the above.

Whatever you do, also check the backup. Does it contain a database dump? Does it contain all files? If you&#8217;re going to be messing with DNS and e-mail, you may want to check if that&#8217;s backed up too.

You&#8217;re now at a point where you can start developing/debugging with some confidence. It&#8217;s not perfect, but at least you have something to fall back on. I&#8217;d take it at least one step further.

## Get the files under version control

If you&#8217;re going to be making multiple changes for multiple different tasks, you&#8217;re going to want to have all the code under version control. The easiest way: just put the entire public HTML folder under version control. You may be versioning too many files there, but at least you&#8217;re not missing anything.

One typical issue that pops up is the fact that not every one is going to be using version control. For instance, even the simplest WordPress blog can cause issues, because it is possible to edit some of the files from within the administration console.

If you have shell access, you could install and use version control on the server itself. But that doesn&#8217;t work for shared hosting.

I haven&#8217;t found the perfect, automated, solution but there are a few tools out there that allow you to view the difference between an FTP directory and a local on. Beyond Compare 3 is a pretty good one, once you get past its archaic interface.

You&#8217;re now at a pretty good place. Major disasters will be solved by the backup and smaller issues can be resolved by rolling back the change that caused them.

There&#8217;s still one wildcard: the database. Especially if your work involves structural changes to the database, you may want to look into &#8230;

## Version control for the database

Few people do database version control and when it happens, it doesn&#8217;t always work quite right. But if you want to feel save doing that normalization operation on a few tables, there&#8217;s no way around it. You have to get the database in your version control system.

[Start here](http://www.codinghorror.com/blog/2008/02/get-your-database-under-version-control.html "Get your database under version control") and if you want to take it further, there have been many tools written since that post that will make your life easier.

## (Unit) Test the code

Depending on the language of the application, you may just automatically be writing tests, even before you considered creating a backup. If it&#8217;s a PHP site however, chances are nobody has thought of this before.

You may think testing isn&#8217;t important for your particular application, but do me a favor: get at least one test in there, so that you&#8217;ve got the structure set up. If you ever add new code, you will be much more likely to add more tests.

[tweetherder]Start the test suite with a single test and let it grow from there.[/tweetherder]

## Integration/GUI testing & Continuous integration

If you get through the previous steps, you&#8217;re doing better than most. Automated GUI testing, a continuous integration server or even a continuous deployment environment, etc. it&#8217;s all icing on the cake. But if you&#8217;ve got the time and budget to set this up, you&#8217;re going to be a very happy developer down the road.

## Conclusion

Many sites out there are still alive only by the mere fact that nothing bad ever happened until now. If you&#8217;re going to be updating such a site, chances are good that you will be held responsible if anything goes wrong. Even if it is completely beyond your control. The above steps will make sure that you are prepared and that you can start refactoring the code without worrying.

This is an evolving article, I will be updating it as I go along. Tips are more than welcome.

([image credit](http://www.flickr.com/photos/avlxyz/5996764291/))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->