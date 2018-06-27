---
id: 243
title: Build a Highly Interactive Web Application in No Time
date: 2008-09-09T10:00:54+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=243
permalink: /build-an-highly-interactive-web-application-in-no-time/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20.png
dsq_thread_id:
  - "5437989"
image: /wp-content/uploads/2008/09/recipebook20.png
categories:
  - Java and JavaScript
---
Do you want to learn how to go from a web 2.0 idea to a concept that can be sold to friends and and venture capitalists alike? Just follow along.

In this post I will show you the thoughtproces that was behind the Recipebook 2.0 prototype I showed you in <a title="free clipart for your site" href="http://www.streamhead.com/?p=133" target="_blank">earlier</a> <a title="Recipebook 2.0 prototype" href="http://www.streamhead.com/?p=120" target="_blank">posts</a>. And the debugging done after <a title="del.icio.us bookmarks for the web" href="http://delicious.com/" target="_blank">Del.icio.us</a> changed their site design and API. So it will show you a bit of both theory and practice. Perfect, not?

Because the art of visual thinking really is an art, I&#8217;ll be adding a lot of visual graphics and sketches to my posts. So have a little patience, they&#8217;ll improve over time. Here&#8217;s the basic concept of Recipebook 2.0 (click for full size).

[<img class="alignnone size-medium wp-image-245" title="Recipebook 2.0  The idea" src="http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20idea-300x142.png" alt="" width="300" height="142" srcset="http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20idea-300x142.png 300w, http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20idea.png 568w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20idea.png)

Basically, I want something that will let me have a list of recipes of what I can make with whatever is in my cupboards. That way I don&#8217;t have to go to the store, I can just start cooking something tasty. The upside of the idea is that is much more versatile than that. You can use it to select your favorite ingredients and get some suggestions for recipes you didn&#8217;t know yet.

This is actually a pretty simple application with just a long list of recipes. For each recipe the usual stuff is stored:

  * A name
  * The ingredients
  * A short description
  * A link (to the full recipe)
  * (possibly) a picture

Also, at some point, it might be interesting to have such a list for every user. Supposedly there will be an overlap between recipe lists and there could be some kind of &#8220;master&#8221; list that holds all recipes in the system.

In most cases, one would design a database schema that can hold this information. Add some kind of web framework to the mix and start coding those pages. Nothing complicated really, but once I started thinking about it, I realized that everything already exists. Just replace &#8220;ingredients&#8221; with &#8220;tags&#8221; and you&#8217;ve got your run of the mill microcontent platform. A user has a bunch of snippets that they can tag and share. No need to start writing fancy <a title="Create, read, update, delete" href="http://en.wikipedia.org/wiki/CRUD_(acronym)" target="_blank">CRUD</a> stuff, search code or user management. It already exists. Del.icio.us immediately sprung to mind. If you don&#8217;t know del.icio.us yet, now is the time to try it out.

The only other thing I needed was some filtering and formating of the tags. I wanted to keep using del.icio.us for my normal bookmarks, so I prefixed all ingredients with &#8220;ingredient.&#8221;. That&#8217;s basically all there is to it. This diagram gives an overview of the architecture (click for full size):

[<img class="alignnone size-medium wp-image-246" title="Recipebook 2.0 - architecture" src="http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20architecture-300x167.png" alt="" width="300" height="167" srcset="http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20architecture-300x167.png 300w, http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20architecture.png 598w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2008/09/recipebook20architecture.png)

If you do this kind of thing, try to use &#8220;official&#8221; API&#8217;s. Del.icio.us has always had <a title="Del.icio.us API" href="http://delicious.com/help/tools" target="_blank">an API</a> to retrieve your links. However, either they didn&#8217;t have anything to retrieve tags, or I missed it. Because I was using Yahoo! Pipes to screen scrape the ingredient tags. This had the unwanted side effect of completely breaking the site when del.icio.us changed their screens. Luckely they have <a title="del.icio.us feeds" href="http://delicious.com/help/feeds" target="_blank">a feed</a> to retrieve all your tags. From there on, it&#8217;s straightforward to filter out only the ingredient tags. Just take a look at <a title="ingredient filtering pipe" href="http://pipes.yahoo.com/streamhead/7Lxs970t3RGOzUHQy6ky6g" target="_blank">the pipe</a> I created. As you will notice, I&#8217;ve also added the possibility to select the del.icio.us username, which will make it possible to change the user (when I add that functionality).

I hope this first part has given you a glimpse at how you might attack your ideas and implement them. Before you program too much, first think about what is out there. Certainly for a first prototype this will do. Now show me those ideas of yours.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->