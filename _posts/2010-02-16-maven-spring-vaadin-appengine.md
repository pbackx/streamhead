---
id: 1893
title: Maven, Spring, Vaadin and Google AppEngine, Happy Together
date: 2010-02-16T10:00:16+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1893
permalink: /maven-spring-vaadin-appengine/
Image:
  - http://www.streamhead.com/wp-content/uploads/2010/02/happy_together.png
dsq_thread_id:
  - "67130628"
image: /wp-content/uploads/2010/02/happy_together.png
categories:
  - Java and JavaScript
---
In true open source spirit, I scratched my itch. No, not that itch. If you complain about open source projects, you have all the tools at your disposal to fix the problem yourself. Last week, I posted that <a title="Google AppEngine, Vaadin, Spring, a Match Not Made in Heaven" href="http://www.streamhead.com/google-appengine-vaadin-spring-match-heaven/" target="_blank">it&#8217;s not straightforward at all to make <strong>Spring, Google AppEngine (GAE) and Vaadin work together in Eclipse</strong></a>. This week, I present **the solution**.

_Update_: I&#8217;ve added a necessary repository to the pom file. So if you had problems previously, please download the file again. Your issues should be solved.

<!--more-->

**<a title="Maven pom.xml with Spring, Vaadin and  Google AppEngine pre-configured" href="../wp-content/uploads/2010/02/pom.xml" target="_blank"><img class="alignnone size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="" width="30" height="24" /></a>** <a title="Maven pom.xml with Spring, Vaadin and  Google AppEngine pre-configured" href="../wp-content/uploads/2010/02/pom.xml" target="_blank">download the pom.xml</a>

It&#8217;s a fairly long <a title="Maven simplifies development" href="http://www.streamhead.com/maven-simplifies-seam-facelets-development-handle-xml/" target="_blank">Maven</a> pom.xml file, but I believe it remains understandable and usable. Using Maven also makes it easier to integrate your project in continuous build systems and to cooperate on a project with other people. The remainder of this post discusses the details, but you can just go ahead and **<a title="Maven pom.xml with Spring, Vaadin and Google AppEngine pre-configured" href="http://www.streamhead.com/wp-content/uploads/2010/02/pom.xml" target="_blank">download the pom.xml right away</a>**.

In order to get started you should:

  * Adjust the pom.xml to your liking. You probably want to change the artifact and group id&#8217;s.
  * Run &#8220;**mvn clean**&#8221; to create a clean project with the dependencies in the right location.
  * Run &#8220;**mvn eclipse:eclipse**&#8221; to generate the Eclipse configuration files.
  * **Import the project into Eclipse** (or you can use the <a title="m2eclipse" href="http://m2eclipse.sonatype.org/" target="_blank">m2eclipse Maven integration</a> if you like)
  * Start programming your project. With this configuration you will be able to follow <a title="Spring Integration - Vaadin" href="http://vaadin.com/wiki/-/wiki/Main/Spring%20Integration" target="_blank">the Spring integration tutorial on the Vaadin site</a> (including the annotation driven configuration, which is my favorite).

If you like to know a little more about what the pom.xml does, here are the various issues that are resolved by it.

<div style="float:right;">
  <a title="Concord Jet" href="http://www.flickr.com/photos/10287726@N02/4359308044/" target="_blank"><img src="http://farm5.static.flickr.com/4004/4359308044_d599bc2b66_m.jpg" border="0" alt="Concord Jet" /></a><br /><small><a title="Attribution License" href="http://creativecommons.org/licenses/by/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="simononly" href="http://www.flickr.com/photos/10287726@N02/4359308044/" target="_blank">simononly</a></small>
</div>

## Google AppEngine

The main issue with Google AppEngine is managing the WAR structure. The Eclipse plugin for GAE cannot directly deploy a .WAR file and it needs a very rigid structure. It takes the contents of the &#8220;war&#8221; directory and deploys that. The exact directory cannot be changed, neither can the location of the dependencies. So the pom take care of:

  * Java classes are compiled to /war/WEB-INF/classes
  * JAR dependencies are managed in /war/WEB-INF/lib (&#8220;mvn clean&#8221; both deletes the old jar files and copies the new ones in the directory)

## Eclipse project files

The second large block of code you&#8217;ll find in the pom.xml is setting up the Eclipse project files:

  * Configuring the various &#8220;natures&#8221; (those are the different plugins that are enabled for the project)
  * Setting up the environment with, for instance, some additional validators and builders.
  * For all of this to work, you will need to have all the corresponding Eclipse plugins installed (Vaadin plugin, Spring and AspectJ)

As always, this work would not have been possible without <a title="Maven Archetype for Google AppEngine" href="http://fornax-sculptor.blogspot.com/2009/10/maven-archetype-for-app-engine.html" target="_blank">the help</a> of a <a title="Spring application - Vaadin example" href="http://dev.vaadin.com/browser/incubator/SpringApplication" target="_blank">few people</a>. I stand on the shoulders of giants.

There are still a few to-do&#8217;s left:

  * Google AppEngine has recently been update from version 1.3.0 to 1.3.1. 
  * Maven support inside Eclipse is not yet enabled. I think adding the &#8220;org.maven.ide.eclipse.maven2Nature&#8221; nature to the pom.xml should solve this, but I haven&#8217;t tried it out yet.

**<a title="Maven pom.xml with Spring, Vaadin and  Google AppEngine  pre-configured" href="../wp-content/uploads/2010/02/pom.xml" target="_blank"><img title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="" width="30" height="24" /></a>** <a title="Maven pom.xml with  Spring, Vaadin and  Google AppEngine pre-configured" href="../wp-content/uploads/2010/02/pom.xml" target="_blank">download the pom.xml</a>

Good luck and be sure to let me know if you encounter problems or have tips.

(<a title="so happy together" href="http://www.flickr.com/photos/thomashawk/3043998465/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->