---
id: 2272
title: WordPress Site Performance Considerations and Tips
date: 2010-05-11T10:00:48+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2272
permalink: /wordpress-site-performance/
dsq_thread_id:
  - "94215776"
image: /wp-content/uploads/2010/05/speed.png
categories:
  - Graphics, Visuals and Texts
---
Website performance has recently been in the spotlight once more. In fact, it should never be out of the spotlight if you want to keep your customers happy. This site is no stranger to bad performance. It&#8217;s a typical WordPress problem. You&#8217;ve got a nice blog and install a few plugins and before you know it, your site needs 20 JavaScript files and even more CSS files. But how to avoid this?

I&#8217;m going to warn you before you read on, this post does not have the definitive answer, just a few ideas that, I hope, will stimulate some needed discussion.

<!--more-->Before you get started, one of the best and also longest running tools to analyze your website is 

<a title="YSlow" href="http://developer.yahoo.com/yslow/" target="_blank">YSlow, a Firebug plugin by Yahoo!</a>. It&#8217;s the tool by the guys who wrote the book on website performance, so they know their stuff.

If you ran a YSlow analysis against a typical WordPress blog, you&#8217;ll probably be very surprised. But not in a good way. While WordPress and its themes are known for performing great on search engine optimization, no one is really working on performance.

A typical WordPress installation with a few plugins installed will almost always perform bad at the most important performance characteristic: make as few HTTP calls as possible. 20 JavaScript files, 25 CSS files, a few Ajax calls for widgets. It gets ugly very quickly.

The most obvious solution is to **combine those files**. <a title="Combine and minify Javascript" href="http://falcon1986.wordpress.com/2010/01/11/combine-and-minify-javascript-reduce-number-of-http-requests/" target="_blank">This document is a great introduction on how you can get started</a>. It&#8217;s focused on JavaScript, but you can do something similar with CSS too. And while you&#8217;re optimizing your CSS, you might give <a title="csscaffold" href="http://wiki.github.com/anthonyshort/csscaffold/" target="_blank">csscaffold</a> a try, it&#8217;s great little library for reducing lines of CSS.

If you want a plugin for that, there actually are two: <a title="WP-JS" href="http://www.halmatferello.com/lab/wp-js/" target="_blank">WP JS</a> and <a title="WP-CSS" href="http://www.halmatferello.com/lab/wp-css/" target="_blank">WP CSS</a>. Both offer an easy way to combine and minify a list of files. Those plugins also allow you to **fine-tune which JS and CSS is included on which page**. This is great if you need specific files only on one or a few posts (for instance Google Maps).

There still is a hole in that theory though. Many WordPress plugins dynamically include their files from within the theme functions. So you can&#8217;t really extract the files and include them in a new one.

I&#8217;ve done a little research, but haven&#8217;t really figured out a solution. The right way to include JS is by using <a title="Loading JavaScripts with WordPress" href="http://www.bloggingtips.com/2008/10/26/loading-javascripts-with-wordpress/" target="_blank">the wp_enqueue_script function</a>. But <a title="Function Reference/wp enqueue script" href="http://codex.wordpress.org/Function_Reference/wp_enqueue_script" target="_blank">the documentation</a> doesn&#8217;t really explain where the JS files are actually outputted to the page. This would be the perfect location to put a  combination function.

To be continued.

(<a title="Speed on Flickr" href="http://www.flickr.com/photos/miroen/3542223130/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->