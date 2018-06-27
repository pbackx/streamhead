---
id: 3670
title: 'Upgrading to Java 7 on Google&#8217;s AppEngine'
date: 2014-01-07T10:00:33+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3670
permalink: /upgrading-java-7-googles-appengine/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2013/12/yak_shaving-672x372.jpg
categories:
  - Java and JavaScript
---
If you are still running a Java 6 application on Google AppEngine, you&#8217;re about to get into serious trouble. Any moment now, the AppEngine team is going to release version 1.8.9, which will no longer support deployment of Java 6 applications.

Existing applications will keep on running. But you should probably upgrade your application with the necessary urgency, as you will no longer be able to fix bugs.

<!--more-->

## More Maintenance

Most PaaS providers will very regularly update their platform to keep up with the latest security fixes and to add on new services and APIs. In this regard AppEngine takes a pretty radical approach. They do not wait for their customers when they think removing old code is the right thing to do.

These updates will usually be backwards compatible, but, given enough time, there will be updates that break old code. Java 7 is backwards compatible with Java 6. But some libraries are not.

## A Good Thing?

I try to see this maintenance work as a good thing. It forces you to keep up with the latest technology, which, as far as I&#8217;m concerned, is mostly important from a security standpoint.

## Upgrading to Java 7 on Google&#8217;s AppEngine

So lets get into the details. In most cases, this upgrade will be as simple as changing the JDK that you use to build and deploy to AppEngine. In my case, it wasn&#8217;t.

The major problem was that some part of the JDO/DataNucleus/AppEngine combination I was using, did not work with Java 7. According to all of their respective pages, this should not be problem, but it just didn&#8217;t work with runtime errors that indicated incompatible versions.

I had been wanting to **upgrade DataNucleus** anyway, so I thought &#8220;Why not?&#8221; It turned into a prolonged session of [yak shaving](http://en.wiktionary.org/wiki/yak_shaving).

First, **upgrade appengine-datanucleus**, the integration library between AppEngine and DataNucleus. [There are currently 3 versions](http://code.google.com/p/datanucleus-appengine/wiki/Compatibility). Only the latest version is using non-deprecated code. Sadly, this version is (as far as I know) not officially release yet. So after much  consideration, I ended up picking version 2.1 (I hope to get rid of JDO in favor of Objectify this year)

<span style="line-height: 1.5;">Next I found out that this also means I need to <strong>migrate the datastore content</strong>. <a href="http://code.google.com/p/datanucleus-appengine/wiki/DataMigrationProcess_for_Version2">This is not very well documented at all</a>. Even if you manage to find that wiki article, it&#8217;s using old libraries. I was unable to get this working on my project and didn&#8217;t have the time nor willpower to figure out the new mapreduce framework for AppEngine.</span>

Eventually I created a small task queue that could perform the upgrade. Luckily the number of entities was small enough that this worked. If you have a larger dataset, you will probably already know how to use mapreduce anyway.

With that out of the way, there were still a few small bugs popping up.  All of them were caught by my unit tests. For instance, it turns out that **loading an empty collection from the datastore may now return null instead of an empty collection**. Small thing to fix, but it would be nice if this was documented somewhere.

## Conclusion

Make sure you take your time to do the Java 6 to 7 upgrade on AppEngine. It&#8217;s probably going to be transparent for you, but what if it isn&#8217;t?

([photo credit](http://www.flickr.com/photos/mylesdgrant/2696313749))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->