---
id: 3496
title: Meteor JavaScript Web App Platform Lunch Hour Impressions
date: 2012-07-02T15:00:31+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3496
permalink: /meteor-javascript-web-app-platform-lunch-hour-impressions/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2012/06/meteor_full_stack_javascript_framework.png
categories:
  - Java and JavaScript
---
In this second installment in the series, I&#8217;m using my lunch hour to take a look at Meteor. It&#8217;s another box filled with all kind of delicious candy that any web app developer will love to use. But is it worth your time?

<!--more-->

This article is going to sound a lot like a comparison with [the previously reviewed Opa platform](http://www.streamhead.com/opa-web-application-platform-lunch-hour-experiment/ "Opa Web Application Platform First Look"). And there&#8217;s good reason for that. Meteor is a full stack web application framework. Just as Opa, it comes as a standalone package. Just as Opa, it blurs the distinction between client and server.

Major differences with Opa include: Meteor is absolutely not production ready and Meteor uses JavaScript.

## First Impressions

I tried Meteor on a [VirtualBox](http://www.streamhead.com/virtualbox/ "VirtualBox power tool for developers") Ubuntu installation. Given the way it is installed, it looks very unlikely that Meteor will run on Windows without a lot of hacking, so I didn&#8217;t even bother.

[The Meteor site blurs the lines between download and examples](http://meteor.com/examples/leaderboard). By the time you have installed Meteor, you also have an example app. This feels a little strange at first, &#8220;where&#8217;s that download link?&#8221;, but it&#8217;s a pretty good idea to get you started right away.

The examples are good, yet they couldn&#8217;t help but implement another multiuser live-update system (not a chat this time, though). Again, I think this is a use case that only a very small percentage of developers will encounter in their lives.

## JavaScript All the Way Down<figure id="attachment_3505" style="width: 225px" class="wp-caption alignleft">

<img class="size-medium wp-image-3505" title="It's Turtles All The Way Down" src="http://www.streamhead.com/wp-content/uploads/2012/07/its_turtles_all_the_way_down-225x300.jpg" alt="It's Turtles All The Way Down" width="225" height="300" srcset="http://www.streamhead.com/wp-content/uploads/2012/07/its_turtles_all_the_way_down-225x300.jpg 225w, http://www.streamhead.com/wp-content/uploads/2012/07/its_turtles_all_the_way_down.jpg 768w" sizes="(max-width: 225px) 100vw, 225px" /><figcaption class="wp-caption-text">No, not turtles, to develop in Meteor, you&#8217;ll only need to know JavaScript.</figcaption></figure> 

[tweetherder]Unlike Opa, Meteor uses the familiar JavaScript language[/tweetherder]. Just as Opa, it mixes both server-side and client-side code in the same files. The distinction between client and server is made through a simple &#8220;if&#8221; test. Meteor.is\_client and Meteor.is\_server tell you where the code is running.

As far as I understand, most existing JavaScript libraries are re-usable straight away. So while the standard API may be pretty limited, your options will be endless. There are about 10 popular web libraries included by default, Bootstrap and Underscore are a few that I will find useful.

It wasn&#8217;t immediately clear from the web pages, but Meteor is build on Node.JS.

## Deploying to the Cloud

The built-in examples are a great way to get started right away. However, going over them, I&#8217;m a little confused how security works. You can just deploy to any servername you like, so I guess any one can overwrite this &#8220;live&#8221; version of the program. It&#8217;s neat to be able to get started right away, however if you happen to cross paths with some one else using the same name, it&#8217;s probably not so much fun.

Reading further it appears it is possible to set a password for the server, but by default there is none. It&#8217;s also possible to create a self-contained package that can be deployed to Heroku. Which is nice, although I&#8217;m going to need a little more explanation than provided before I can actually deploy it.

## Storing and Viewing Data<figure id="attachment_3507" style="width: 300px" class="wp-caption alignright">

<img class="size-medium wp-image-3507" title="MongoDB cup & cards" src="http://www.streamhead.com/wp-content/uploads/2012/07/mongodb-300x199.jpg" alt="MongoDB cup & cards" width="300" height="199" srcset="http://www.streamhead.com/wp-content/uploads/2012/07/mongodb-300x199.jpg 300w, http://www.streamhead.com/wp-content/uploads/2012/07/mongodb.jpg 500w" sizes="(max-width: 300px) 100vw, 300px" /><figcaption class="wp-caption-text">If you&#8217;re used to SQL, you&#8217;ll find MongoDB&#8217;s API very refreshing.</figcaption></figure> 

Meteor&#8217;s default datastore is MongoDB and as far as I can see, it directly exposes MongoDB&#8217;s JavaScript API. Mongo uses a fairly intuitive interface, so even without experience, you&#8217;ll be able to write a simple CRUD application quickly.

Since there&#8217;s a lot client/server communications build into the API, it looks like it would be fairly difficult to replace MongoDB with your own choice.

On the view side, Meteor comes with Handlebars built in. It has a neat and very clean way of using helper functions to connect the template variables and events to the controller code. You can replace Handlebars with your choice of templating framework, but I see very little reason to.

## Wrapping Up

Just shooting from the hip here while I wrap up my hour:

As far as I can see, there&#8217;s no dependency management. I&#8217;m not sure why they didn&#8217;t re-use what Node and NPM already offer.

Development is as &#8220;live&#8221; as it will get. You don&#8217;t need to even reload your browser. This all happens behind the scenes for you. An impressive productivity feat.

Meteor seems to use long polling client/server communication similar to Opa.

The documentation is clear and also give a good insight into how the magic works, which is important for an analytical guy like me.

## Why Would You Use Meteor

[tweetherder]With Meteor, your development time will be spent almost 100% doing actual development work[/tweetherder]. No time lost compiling, deploying or restarting.

[tweetherder]Meteor is 100% JavaScript, a language pretty much any developer on the planet knows[/tweetherder]. You can be productive almost immediately.

## Why Would You Not Use Meteor

Meteor is still extremely experimental. As far as I know, there are no production level apps online. It&#8217;s probably going to be at least a year before you will be able to deploy Meteor apps and sleep at night.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->