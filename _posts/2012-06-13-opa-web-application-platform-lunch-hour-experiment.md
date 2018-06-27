---
id: 3478
title: The Opa Web Application, Lunch Hour Experiments
date: 2012-06-13T16:00:32+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3478
permalink: /opa-web-application-platform-lunch-hour-experiment/
pdrp_attributionLocation:
  - end
categories:
  - Java and JavaScript
---
&#8220;Another day, another framework&#8221;, you might think. And yes, Opa is yet another web framework that is going to revolutionize web development. But don&#8217;t judge it too soon, it has a few tricks up its sleeve that might convince you to try it out. Read on for my first hour of Opa.

<!--more-->

This is a first in what I hope will become a regular feature: I give myself one hour to try out something new and decide whether I will pursue it or not. Feel free to send any suggestions my way.

## First Impressions and How to Deploy

I love to try out new technology for pet projects and one thing I always worry about is small scale, cheap deployment. I could not find anywhere on the site how you&#8217;d deploy Opa. Is there support for PaaS providers like Heroku? It appears not, you need to have access to and full control over your own VPS (there&#8217;s some limited information on AWS)

## OCaml<figure id="attachment_3487" style="width: 300px" class="wp-caption alignright">

<img class="size-medium wp-image-3487" title="opa accordian" src="http://www.streamhead.com/wp-content/uploads/2012/06/opa_accordian-300x196.jpg" alt="" width="300" height="196" srcset="http://www.streamhead.com/wp-content/uploads/2012/06/opa_accordian-300x196.jpg 300w, http://www.streamhead.com/wp-content/uploads/2012/06/opa_accordian.jpg 760w" sizes="(max-width: 300px) 100vw, 300px" /><figcaption class="wp-caption-text">Opa is Dutch for grandfather</figcaption></figure> 

I don&#8217;t understand why the website says the Opa language is JavaScript-like. As soon as you start writing your own thing, you&#8217;ll notice there are some major differences between Opa and JavaScript, so be prepared to learn a new language

Opa is based on OCaml, an objective functional language that has been around for a while and seems to mostly live inside academiccircles.. [I first used it in 2000](http://www.cis.upenn.edu/~dsl/PLAN/), the memories 🙂

## Windows Version

I tried the all-in-one Windows installer.

It automatically installs a plugin for Sublime Text. The plugin itself has a build-in mini tutorial. Which is nice if you&#8217;re a Sublime Text 2 user. Keep in mind that your Opa file must be in the root of the folder tree, otherwise the run command won&#8217;t find the correct file. The plugin also couldn&#8217;t kill the processes it started, which made the build/run integration useless.

Later on, I also discovered that the installer had deleted my path setting. I assume this is a small bug that will be solved in the next release.

## HTML and NoSQL

Opa only supports NoSQL databases and I have a feeling you&#8217;re in for a lot of hurt if you try to connect to a relational one.

HTML doesn&#8217;t need to be quoted and the compiler checks for correctly closed tags. That&#8217;s pretty cool.

## Type System<figure id="attachment_3489" style="width: 300px" class="wp-caption alignleft">

<img class="size-medium wp-image-3489" title="TYPE+" src="http://www.streamhead.com/wp-content/uploads/2012/06/type-300x225.jpg" alt="" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2012/06/type-300x225.jpg 300w, http://www.streamhead.com/wp-content/uploads/2012/06/type.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" /><figcaption class="wp-caption-text">Static typing without the overhead</figcaption></figure> 

Opa uses static typing with type inference which made me think of Scala: it gets out of your way, but it&#8217;s there if you mess up. It&#8217;s probably a great feature if you are used to static typed languages but may be an annoyance if you are not.

## Client/Server

[Running the Hello world counter example](http://hello-opa.tutorials.opalang.org/) and clicking on the header results in 5 POSTS. The last running to closed. Probabfurthers ever push communication. 5 posts just to transmit one number worries me. It&#8217;s also all Ajax, so no SEO here.

I tried to add the &#8220;server&#8221; keyword in front of the &#8220;page&#8221; function, but that did not remove the ajax updates. I suppose it&#8217;s a little too early for that but [the documentation seems to indicate that this forces function to run on the server](http://doc.opalang.org/manual/A-tour-of-Opa/A-single-language).

The first tutorial is a chat application. I can understand that this is a great demonstration of the language and API, but this is an application only 1% (or less) of the developers ever needs to write.

The chat application is concise, yet I can&#8217;t help but ask myself how you&#8217;d ask a web designer to work on this project. You could argue that CSS is all he needs, but in practice it very rarely works like that. Maybe there&#8217;s a way to externalize the HTML in seperate Opa files (like you&#8217;d split a PHP app in a controlling part and a template part, even though both are technically PHP files) Going over the table of contents, I can&#8217;t really see this explained anywhere

## Integration

Going to the wiki example, I learn that aside from Bootstrap, also Markdown is built into the API. This is nice. I&#8217;ve always liked Markdown as a simple language for creating content. This has me [browsing the API documentation](http://doc.opalang.org/api), where I also see support for Google Charts, Canvas, Facebook and Twitter. And I also scroll past a &#8220;template&#8221; package, so my fears from the previous paragraph seem to be unfounded.

## Wrapping Up<figure id="attachment_3491" style="width: 300px" class="wp-caption alignright">

<img class="size-medium wp-image-3491" title="313/365 Wrapping Up" src="http://www.streamhead.com/wp-content/uploads/2012/06/313365_wrapping_up-300x199.jpg" alt="" width="300" height="199" srcset="http://www.streamhead.com/wp-content/uploads/2012/06/313365_wrapping_up-300x199.jpg 300w, http://www.streamhead.com/wp-content/uploads/2012/06/313365_wrapping_up.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" /><figcaption class="wp-caption-text">An hour is too short</figcaption></figure> 

Because I&#8217;m nearing the end of my one hour, I quickly scoop over the rest of the documentation. I do encounter a more detailed explanation of the client/server keywords and their usage. If I pick up Opa for a new project in the future, it will probably be the first thing I&#8217;ll read.

The one thing that keeps bugging me is the absence of any information on deploying. [The Scalability chapter](http://doc.opalang.org/manual/Hello--scalability) touches on this, but it&#8217;s very unclear to me. Probably because I&#8217;m too impatient and I should just try it out. From what I understand the &#8220;opa-cloud&#8221; application will distribute your application over SSH. However, does this also work between operating systems (the command lines presented seem to indicate that it just copies the &#8220;exe&#8221; file that was produced).

Throughout the entire hour, I also can&#8217;t help but think &#8220;Why bother learning Opa, when Node.JS offers a fairly similar model in a language all developers already know&#8221;. [It&#8217;s a valid question and others have looked at it in much more detail](http://www.developer.com/open/node.js-opa-javascript-framework.html). One of the most important things I picked up from that test was how concise Opa applications seem to be. This is probably related to its OCaml heritage.

## Why would you use Opa?

You can write all of the code for your web application in one concise and type-safe language. Out-of-the-box Opa supports an interesting selection of integrations and its first-class language support for HTML and NoSQL databases is top notch.

## Why would you not use Opa?

You just want to get started and don&#8217;t feel like learning a new language. You prefer a large community backing your choice framework.

## More resources

  * [Opa questions at StackOverflow](http://stackoverflow.com/questions/tagged/opa)
  * [The Opa blog](http://blog.opalang.org/ "The Opa blog")
  * [amazon\_link id=&#8221;159059620X&#8221; target=&#8221;\_blank&#8221; container=&#8221;&#8221; container\_class=&#8221;&#8221; ]Practical OCaml, the base for Opa[/amazon\_link]

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->