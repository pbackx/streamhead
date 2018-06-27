---
id: 2226
title: Java Client for Google Data API, One More Step to World Domination
date: 2010-04-27T10:00:28+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2226
permalink: /java-client-google-data/
dsq_thread_id:
  - "90080904"
image: /wp-content/uploads/2010/04/google-monster.png
categories:
  - Java and JavaScript
---
I&#8217;ve featured a number of <a title="Google AppEngine, Vaadin, Spring" href="http://www.streamhead.com/maven-spring-vaadin-appengine/" target="_blank">Google projects</a> before, most of them <a title="Android, No-cost Development Platform" href="http://www.streamhead.com/android-nocost-development-platform/" target="_blank">I liked</a>. <a title="Google Wave" href="http://www.streamhead.com/horizontal-layou/" target="_blank">Some look strange and pointless</a>. But I&#8217;ve always found the documentation to be outstanding. Maybe a little too technical for many, but for some reason, it&#8217;s always just right for me. The Google Data API&#8217;s are just one more example. Currently I&#8217;m learning the <a title="Google Documents List Data API" href="http://code.google.com/apis/documents/overview.html" target="_blank">Google Documents List Data API</a> and it looks like another winner.

<!--more-->I found the Google Documents List Data API through a strange detour. I want to generate PDF files on Google AppEngine, but sadly, 

<a title="iText" href="http://itextpdf.com/" target="_blank">the most popular and advanced Java PDF library, iText</a>, is not (yet?) fully compatible with Google AppEngine. There are some hacks out there to get it working, but I&#8217;m not too much of a fan for starting out with a hacked and unsupported library.

So after some googling (what else?) I stumbled upon the perfect solution: Google Documents can be exported to PDF, they can be used as templates and, best of all, it is possible to use all of that functionality from inside a Java program.

As always, Google has a strong preference for Eclipse. If you go with that flow, they have <a title="Using Eclipse with Google Data APIs" href="http://code.google.com/apis/gdata/articles/eclipse.html" target="_blank">a long and detailed document to get you started</a>. If you want to use other IDEs or continuously integrate, there are ANT build scripts included with the distribution. And if you look around, there will undoubtedly be Maven integration plugins too.

Once that is taken care of, <a title="Java Language Guide - Google Documents List Data API" href="http://code.google.com/apis/documents/docs/3.0/developers_guide_java.html" target="_blank">the Java Language Guide for the Google Documents List Data API</a> is an introduction to pretty much every task you&#8217;ll want to do with the API.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->