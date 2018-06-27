---
id: 3784
title: 'Static Site Generator Shootout &#8211; JBake vs Jekyll'
date: 2015-10-23T20:24:57+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3784
permalink: /static-site-generator-shootout-jbake-vs-jekyll/
pdrp_attributionLocation:
  - tag
image: /wp-content/uploads/2015/10/13861341694_1d3dbe016f_z.jpg
categories:
  - Java and JavaScript
---
Earlier this year, I&#8217;ve been experimenting with static site generators. My eventual goal is to move this blog and a few more into static sites. After some experimentation, my conclusions are pretty predictable.

<!--more-->

Ask any one what software to use if you want to run a blog. Most people will suggest **WordPress** right away.

For the longest time, I&#8217;ve also done so. It has a huge community with a plugin for everything you can think of. I run four sites on WordPress. Some popular, some not so much.

Last year I started to change my mind about WordPress as the default choice. If any of my sites gets the least bit of traffic, my host will start to complain because of **excessive resource usage**. Shared hosts are notoriously aggressive in shutting down sites that demand too many of their servers, but they have a point.<figure id="attachment_3792" style="width: 300px" class="wp-caption alignright">

<img class="size-medium wp-image-3792" src="http://www.streamhead.com/wp-content/uploads/2015/10/explosion-300x69.jpg" alt="Explosion" width="300" height="69" srcset="http://www.streamhead.com/wp-content/uploads/2015/10/explosion-300x69.jpg 300w, http://www.streamhead.com/wp-content/uploads/2015/10/explosion.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" /><figcaption class="wp-caption-text">Small impression of my shared host&#8217;s server whenever I publish something popular.</figcaption></figure> 

WordPress is not designed to serve a lot of traffic. Out-of-the-box, WordPress is a fully dynamic site and requires a lot of tweaking to perform acceptable.

On top of that, WordPress is a prime target for all kinds of attacks by script kiddies who just want to have fun. Not only do you need to update ASAP if a **security** patch comes out, but there are numerous ways some one can launch a successful denial-of-service attack on your site.

There is a much simpler solution: don&#8217;t use any dynamic code that requires server resources. Create all your HTML pages offline and don&#8217;t run any code to serve them to your customers.

Enter: **static site generators**.

A static site generator takes a general site layout and plain text content and merges everything into a nice package of static JavaScript, CSS and HTML pages. No need to have anything running on the server, except for the bare minimal highly optimized web server.

I&#8217;ve taken a look at two static site generators:

  * [Jekyll](http://jekyllrb.com/). It&#8217;s the one every one is using.
  * [JBake](http://jbake.org/). It wants to be Jekyll, but written in Java.

## 5 reasons to use JBake<figure id="attachment_3799" style="width: 225px" class="wp-caption alignleft">

<img class="wp-image-3799 size-medium" src="http://www.streamhead.com/wp-content/uploads/2015/10/2751922013_1e7e7f7088_z-225x300.jpg" alt="Forest View Bakery" width="225" height="300" srcset="http://www.streamhead.com/wp-content/uploads/2015/10/2751922013_1e7e7f7088_z-225x300.jpg 225w, http://www.streamhead.com/wp-content/uploads/2015/10/2751922013_1e7e7f7088_z.jpg 480w" sizes="(max-width: 225px) 100vw, 225px" /><figcaption class="wp-caption-text">Bake your site with JBake</figcaption></figure> 

I&#8217;ve used JBake to create and host a small personal site. The site has been running for half a year without issue. It responds about a 100 times quicker then any of my WordPress sites. It hasn&#8217;t received too many content updates, because I haven&#8217;t configured a good automated deployment process.

It was easy to get started, but it does require a bit of work to get everything going.

Most importantly, there are no themes available, so you&#8217;re on your own. [At least, you were, here&#8217;s one that I made and that you can use](https://github.com/pbackx/startbootstrap-clean-blog).

Reasons why I&#8217;d use JBake again:

  1. It&#8217;s written in Java. If Java is your primary programming language, this is going to be the main reason for using JBake
  2. It doesn&#8217;t have any bells and whistles, but it does everything you need.
  3. The code is minimal and readable, so you can extend it easily.
  4. If you like the underdog, JBake is perfect.
  5. Euhm&#8230; Did I already say it&#8217;s written in Java?

## 5 reasons to use Jekyll

<img class="alignright size-medium wp-image-3800" src="http://www.streamhead.com/wp-content/uploads/2015/10/jekyll-logo-300x139.png" alt="Jekyll logo" width="300" height="139" srcset="http://www.streamhead.com/wp-content/uploads/2015/10/jekyll-logo-300x139.png 300w, http://www.streamhead.com/wp-content/uploads/2015/10/jekyll-logo.png 498w" sizes="(max-width: 300px) 100vw, 300px" />I haven&#8217;t deployed any sites with Jekyll yet, but I&#8217;m working on converting this site.

Reasons why I&#8217;m using it:

  1. Every one uses it. The documentation is clear, but even if you have an issue, you can just Google it.
  2. There are a lot of premade themes available.
  3. If you want extra functionality, there&#8217;s probably already a plugin for that.
  4. You can host it on GitHub for free (with some limitations)
  5. There are many ways to easily deploy your site to various other hosting options.
  6. Ok, one more: You can automatically convert existing WordPress sites.

## Conclusion

<p style="text-align: left;">
  I see no reason why you would make your life difficult. Just go with Jekyll. Unless you really, really want to know the ins and outs of a site generator and you only know Java and don&#8217;t want to learn the slightest bit of Ruby.
</p>

&nbsp;

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->