---
id: 3329
title: Permanent Redirect Non-WWW to WWW in Node.JS on Heroku
date: 2011-11-04T14:00:41+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3329
permalink: /nodejs-permanent-redirect/
amazon_post_template:
  - ""
categories:
  - Java and JavaScript
---
For SEO reasons it&#8217;s important to make sure that users only visit your site through a single domain name. Either www.example.com or example.com, but not both. In most cases a .htaccess change is the easiest fix. But not when you&#8217;re deploying to an environment that doesn&#8217;t have Apache, like Heroku. Here&#8217;s a quick way to get this functionality using Express on Node.JS

<!--more-->Since you probably only want to do this in a production environment, I suggest you place this in 

[that configure block](http://expressjs.com/guide.html#configuration "Express configuration").

Before you add any middleware add the following route:

<pre lang="JavaScript">app.get('*', function(req, res, next) {
  if (req.headers.host.slice(0, 3) != 'www') {
    res.redirect('http://www.' + req.headers.host + req.url, 301);
  } else {
    next();
  }
});</pre>

That&#8217;s really all there is to it. Since most frameworks have similar routing options, you should be able to adapt this to other frameworks, such as Geddy.

BTW I&#8217;m planning to launch a Node.JS app in November as part of [Hacker News&#8217; Launch an App Month](http://news.ycombinator.com/item?id=3180321 "Launch an app month").

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->