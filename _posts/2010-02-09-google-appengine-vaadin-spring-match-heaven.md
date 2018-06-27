---
id: 1856
title: Google AppEngine, Vaadin, Spring, a Match Not Made in Heaven
date: 2010-02-09T10:00:36+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1856
permalink: /google-appengine-vaadin-spring-match-heaven/
Image:
  - http://www.streamhead.com/wp-content/uploads/2010/02/broken_heart.png
dsq_thread_id:
  - "65248829"
image: /wp-content/uploads/2010/02/broken_heart.png
categories:
  - Java and JavaScript
---
Over the last month, I&#8217;ve been learning more and more about <a title="Vaadin" href="http://www.streamhead.com/vaadin-promote-great-gwt-toolkit/" target="_blank">Vaadin</a>. I&#8217;ve also become more and more convinced that this could be the future of rich Internet application development for Java. Vaadin is an incredible powerful framework that solves many of the front-end difficulties developers have to deal with.

In this regard, Vaadin is the missing link for Java web application development. My current **favorite technologies** are:

<!--more-->

  * **<a title="Google App Engine" href="http://code.google.com/appengine/" target="_blank">Google App Engine</a>** for hosting. Although calling Google App Engine (GAE) a Java host might be doing it a little disrespect. But until I&#8217;ve really had time to really dive into GAE, that&#8217;s exactly what it is for me: a cheap, reliable and scalable place to put Java web applications (with some limitations).
  * **<a title="Spring framework" href="http://www.springsource.org/" target="_blank">The Spring framework</a>** is what ties together pretty much every enterprise application. Its dependency injection container and the incredible number of integrated technologies make this the one stop shop for Java developers: MVC, webflow, JPA, transaction management, JavaScript, security, etc. The introduction of many new features in a rather short timespan, might be turning Spring into a beast with many heads instead of the lean mean framework it used to be. For now, there is no alternative.
  * **Vaadin**, obviously.

And that&#8217;s all you need. It seems easy, only 3 technologies and no more. The reality is a little different.

<div style="float:right">
  <a title="feb610" href="http://www.flickr.com/photos/23631188@N03/4339313607/" target="_blank"><img src="http://farm5.static.flickr.com/4060/4339313607_c76190244a_m.jpg" border="0" alt="feb610" /></a><br /><small><a title="Attribution-NonCommercial License" href="http://creativecommons.org/licenses/by-nc/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="morag.riddell" href="http://www.flickr.com/photos/23631188@N03/4339313607/" target="_blank">morag.riddell</a></small>
</div>

I started both my GAE and Vaadin test projects in Eclipse. Although I don&#8217;t really have a preference when it comes to IDEs, it was the obvious choice because both GAE and Vaadin have Eclipse plugins that make development a lot easier. It took a little experimenting, but in the end, both worked together and I was a happy developer.

Until I wanted to add Spring to the mix. **Spring**, by its nature, **comes with tons and tons of dependencies** to many Java projects. And while this is the strength of Spring, it also showed the limitations of the dependency management in Eclipse (or actually the lack thereof).

For better or for worse, when it comes to dependency management, Java applications have only one popular tool and it&#8217;s called **Maven**. This is where things went wrong. I created a Maven project, I even used the GAE archetype that comes with <a title="Maven GAE plugin" href="http://www.kindleit.net/maven_gae_plugin/usage.html" target="_blank">this maven plugin</a>. I tried <a title="M2Eclipse" href="http://m2eclipse.sonatype.org/" target="_blank">the M2Eclipse integration</a>, which is great BTW. But nothing seemed to correctly configure the Google AppEngine plugin. **It never found the appengine-web.xml configuration file**.

It took me a while, but eventually I figured out, **the GAE plugin <a title="Issue 1515 - googleappengine" href="http://code.google.com/p/googleappengine/issues/detail?id=1515" target="_blank">does not support the traditional Maven project structure</a>**. A real shame in my humble opinion.

Luckily I found the solution: Just before publishing I found <a title="Maven Archetype for Google AppEngine" href="http://fornax-sculptor.blogspot.com/2009/10/maven-archetype-for-app-engine.html" target="_blank">this blogpost</a>. Patrik has created **an archetype that creates the files in just the right location**. You still need to be able to stomach the pretty inconsistent project structure, but at least everything works.

The Vaadin wiki also has a lot of <a title="Spring Integration" href="http://vaadin.com/wiki/-/wiki/Main/Spring%20Integration" target="_blank">useful</a> <a title="Google AppEngine HOWTO" href="http://vaadin.com/wiki/-/wiki/Main/Google%20AppEngine%20HOWTO" target="_blank">information</a>.

_Update_: If you want the full solution to this problem, <a title="Maven, Spring, Vaadin and AppEngine, all working together" href="http://www.streamhead.com/maven-spring-vaadin-appengine/" target="_blank">please check this follow up post</a>.

(<a title="broken heart" href="http://www.flickr.com/photos/kaderli/2265098258/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->