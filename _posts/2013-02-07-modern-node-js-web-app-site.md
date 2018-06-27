---
id: 3619
title: The Modern Node.js Web App and Site
date: 2013-02-07T17:53:21+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3619
permalink: /modern-node-js-web-app-site/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2013/02/stream_of_consciousness.jpg
categories:
  - Java and JavaScript
---
As projects for the new year have started to roll in, I&#8217;ve noticed some trends in how web sites and applications are built and how they are hosted. <!--more-->

If you&#8217;re a one-man shop or a small company, the single most important change is the advent of cloud platforms. If you haven&#8217;t been paying attention the last few years, it&#8217;s about time. Suddenly, you no longer have to worry about system administration. Platforms such as Heroku and Google&#8217;s AppEngine might not be the cheapest, but they certainly are helpful in alleviating a lot of the pain of hosting your own web applications.

However, with cloud platforms comes a major change in development: **expect failure** of even the smallest component and **prepare for it.**

<div>
  The one cardinal rule that you will ignore at first, but will learn the hard way: [tweetherder]Every component in the system will fail. You better prepare if you don&#8217;t want your users to suffer.[/tweetherder]
</div>

<div>
</div>

<div>
  The good thing is, you&#8217;re site will be better for it.
</div>

With this in mind, I foresee two parallel roads in web development:

  * <span style="line-height: 13px;">Highly dynamic single page apps interfacing with highly distributed stateless JSON REST services. These services scale indefinitely (almost) and are ideal for systems that fail over regularly (remember, no state). Suggested technologies: <a href="http://angularjs.org/"><strong>AngularJS </strong></a>and<a href="http://backbonejs.org/"><strong> Backbone.js</strong></a> on the client. Pretty much any lightweight Node.js framework will do. For instance, <a href="http://expressjs.com/"><strong>Express</strong></a> combined with some <a href="https://www.mongohq.com/"><strong>MongoDB</strong></a> or <strong><a href="http://www.heroku.com/">PostgreSQL</a></strong> host.</span>
  * Static SEO optimized read-only content. Ideally for distribution on CDNs. [Jekyll](http://jekyllrb.com/) is perfect for this. It isn&#8217;t anything new, before WordPress, Movable Type was already generating static sites. It&#8217;s only common sense, really. But Jekyll puts it into a nice, low-friction package. I haven&#8217;t researched the Node options, but [**Blacksmith**](https://github.com/flatiron/blacksmith), **[Wintersmith](https://github.com/jnordberg/wintersmith)** and **[DocPad](http://docpad.org/)** look promising.

There will always be an overlap, where the choice won&#8217;t be clear. For instance, I can imagine a typical forum, that you want indexed by Google, will be an interesting exercise.

I&#8217;d love to learn about your vision for web development in 2013 and beyond. Please join me on [Twitter](https://twitter.com/pbackx) and [Facebook](http://www.facebook.com/streamhead).

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->