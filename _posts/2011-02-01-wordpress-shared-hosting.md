---
id: 3015
title: Optimizing WordPress for Shared Hosting
date: 2011-02-01T16:00:57+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3015
permalink: /wordpress-shared-hosting/
dsq_thread_id:
  - "220265490"
categories:
  - On Streamhead
---
If you run a blog and want it to be read, you need a site that&#8217;s up and running as much as possible. WordPress will keep you away from many of the nasty site hosting details, but you can be sure that you will run into performance issues at some point. WordPress will help you with a number of useful plugins and options. This post lists 3 easily implemented strategies that should give you some extra mileage before you upgrade your hosting plan.

<!--more-->Shared web hosting is a mixed blessing. On the one hand, you get an extremely affordable website, on the other hand, most providers try to host an incredible amount of sites on one server so they struggle to make true on their promises of unlimited bandwidth and other resources. If you&#8217;ve visited the site during the last weeks, you might have noticed that Streamhead is struggling too.

Very long loading times seemed to indicate database problems, but after some back-and-forth with the web hosting helpdesk, it turns out I&#8217;m being throttled due to too heavy load on the server. I don&#8217;t hold a grudge against <a title="Lunarpages hosting (affiliate link)" href="http://www.lunarpages.com/id/pbackx" target="_blank">Lunarpages </a>at all, I&#8217;m still happy with their support and hosting. It&#8217;s just that an increased number of visitors is pushing the shared hosting plan to its limits.

I&#8217;ve now taken a number of precautions to hopefully stay a little longer on my current hosting plan until I figure out a way to earn some money for better hosting. <a title="Contact Peter" href="http://www.streamhead.com/contact/" target="_blank">Donations and consulting work are always welcomed</a>, btw 😉

Here&#8217;s what I did.

## Caching

This is the single most important step you absolutely have to take if you are running WordPress. Install either <a title="WP Super Cache" href="http://wordpress.org/extend/plugins/wp-super-cache/" target="_blank">WP Super Cache</a> or <a title="W3 Total Cache" href="http://wordpress.org/extend/plugins/w3-total-cache/" target="_blank">W3 Total Cache</a>. It doesn&#8217;t matter too much which one you take. Their features are very comparable.

I was already running WP Super Cache, but I&#8217;ve tweaked the settings a little. I&#8217;m now using &#8220;mod_rewrite&#8221; based caching (in the advanced options), which means there&#8217;s no need at all to invoke any php script for cached pages. I have also increased the cache expiry time so pages stay in the cache for a day (unless they are updated of course)

## Plugin Tweaking

Chances are good that you have a big number of plugins installed. If you have performance issues, take a very good look at the list and try to remove as many plugins as possible. Also experiment to figure out if any one plugin is causing excessive load.

The &#8220;top posts&#8221; plugin is currently disabled to see how the resource usage changes.

## Database Optimizing

The WordPress database tends to get cluttered after some time with old post revisions and other unused data. Sadly, it appears WordPress does not, by default, offer tools to solve this.

Luckily, there&#8217;s <a title="WP-Optimize WordPress plugin" href="http://wordpress.org/extend/plugins/wp-optimize/" target="_blank">the WP-Optimize plugin</a> which allows you to clear out unnecessary data. With the plugin, I was able to clean up 2/3 of my database. I had collected over 2000 old post revisions over the years.

The plugin also offers an option to optimize the MySQL database. You can do this just as well via phpMyAdmin, but it&#8217;s easy to have the option in your WordPress admin interface.

## Further Optimization

If that still isn&#8217;t enough, <a title="Optimizing WordPress performance" href="http://codex.wordpress.org/WordPress_Optimization/WordPress_Performance" target="_blank">the WordPress site offers a number of additional useful tips</a> that will allow you to reduce the load on your site even more. They&#8217;re a bit more advanced, but might be worth your while.

If you have more tips, feel free to share them in the comments.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->