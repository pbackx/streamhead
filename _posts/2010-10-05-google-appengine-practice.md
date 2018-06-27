---
id: 2704
title: Google AppEngine in Practice
date: 2010-10-05T10:00:45+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2704
permalink: /google-appengine-practice/
dsq_thread_id:
  - "154501459"
categories:
  - Java and JavaScript
---
It&#8217;s now been about a month since I initially launched <a title="launching my first vaadin appengine project" href="http://www.streamhead.com/launching-my-first-vaadin-appengine-project/" target="_blank">my project build on Vaadin, Spring and Google AppEngine</a>. I&#8217;m currently trying to create monthly releases where I fix a few bugs and add on some functionality. I&#8217;ve also gotten a little more experience with what works and what doesn&#8217;t, so here&#8217;s a short overview of things to keep in mind when (considering) developing for Google AppEngine. It&#8217;s mostly about the Datastore.
  
<!--more-->

## The Datastore

Like me, you probably come from a background of relational databases. You&#8217;re probably using JPA, most likely with Hibernate. And you might have Spring configured to deal with the transaction handling.

No matter what you might think: **Google&#8217;s Datastore is completely different**.

At first glance, the <a title="The Datastore Java API - Google App Engine" href="http://code.google.com/appengine/docs/java/datastore/" target="_blank">Google AppEngine&#8217;s datastore documents</a> make it look like this is just your normal database. It is not.

If you dive deeper into the documents, you&#8217;ll begin to notice the differences, but because you started of optimistic, it&#8217;s going to hurt. As soon as you run into a thing called &#8220;entity groups&#8221; and are creating your indexes, you&#8217;ll know what I mean. And trust me, you don&#8217;t want to run into entity groups when you think you&#8217;re almost done.

I&#8217;ve found that Spring&#8217;s transaction handling is of little use. If you&#8217;re updating multiple entities from different groups inside the same transaction, you&#8217;re toast. It might be possible to configure it correctly, but I doubt it and I&#8217;ve given up anyway.

I also decided to use JDO because that seems what Google likes. I&#8217;m not sure if this was a good decision, because it looks like, but is not quite JPA.

## App Engine Versioning

I love the way Google AppEngine does versioning. I don&#8217;t think it&#8217;s documented anywhere, but it is as easy as it can get. It works very well though. You can deploy a new version and test it on the AppEngine servers and your users won&#8217;t know a thing.

If you&#8217;re happy, you just flip the switch and you&#8217;re done.

One thing to watch out for is (again) the datastore. It is shared between versions. So you need to make sure you can handle old dataformats in the new version. I haven&#8217;t really looked into this yet, but I don&#8217;t think it&#8217;s possible to execute an &#8220;upgrade&#8221; script. I also don&#8217;t know how that would work with older versions that are still running.

## Developer Tools

I&#8217;ve decided to throw out Spring in the fairly short run and most likely Maven in the longer run. Maintaining their respective configurations is such a pain that I don&#8217;t want to bother with them anymore.

I can&#8217;t seem to configure Spring&#8217;s annotation driven configuration in Eclipse correctly. From time to time it just stops injecting the dependencies for no good reason. The only way out is a complete rebuild of the project, which takes time. And, as mentioned above, I no longer use Spring&#8217;s transaction handling.

The only thing I might keep using is Spring security. I haven&#8217;t really decided on that one yet.

As far as Maven is concerned, I&#8217;m really growing tired of Maven&#8217;s xml syntax. But most importantly, none of Google&#8217;s tools properly support Maven and it appears this isn&#8217;t going to change. I&#8217;ve started developing custom GWT widgets and the GWT Eclipse plugin has even more issues with Maven than the AppEngine plugin did.

So, right now it looks like it&#8217;s byebye Maven and I might try a &#8220;lighter&#8221; dependency management approach.

## Conclusion

You might get the impression Google App Engine is a lot of work. And it is, but not more than most other application servers. There is one advantage to Google App Engine I haven&#8217;t mentioned and it&#8217;s a major one. The hosting is pain free. It just works. No need to watch uptimes or fear traffic spikes. No messing around with Apache config files, Linux config files, etc. And it&#8217;s free to get started.

I&#8217;d love to hear other Google App Engine experiences, that&#8217;s why I have comments enabled 🙂

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->