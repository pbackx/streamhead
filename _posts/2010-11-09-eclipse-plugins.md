---
id: 2794
title: Essential and Not so Essential Eclipse Helios Plugins
date: 2010-11-09T10:00:45+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2794
permalink: /eclipse-plugins/
dsq_thread_id:
  - "169483364"
image: /wp-content/uploads/2010/11/eclipse_helios_plugins.png
categories:
  - Java and JavaScript
---
Ever since Eclipse Helios (3.6) was released, I&#8217;ve been wanting to do a full clean Eclipse install. I didn&#8217;t get around to it until this weekend. During that upgrade, I also made a recap of the different plugins I had installed on my old Eclipse. This post is a short summary of the plugins I use, have used and might use.

<!--more-->Not all plugins will be useful for any one, but I&#8217;m sure you&#8217;ll find something you want to try out in the list. I&#8217;ve also included links to the update sites that you can immediately paste into the Eclipse software manager.

## Essential Keepers

I was surprised at the fairly small number of plugins I wanted to keep in my new Eclipse install. However, those who made the cut, I consider essential. I wouldn&#8217;t be able to create my projects without them:

  * [Subclipse](http://subclipse.tigris.org/): If Subversion is your version control system, this plugin is the most essential you&#8217;ll install ([update site](http://subclipse.tigris.org/update_1.6.x))
  * [EclEmma](http://www.eclemma.org/) is a great way to visualize your unit test coverage and find blank spots ([update site](http://update.eclemma.org/))
  * [Google App Engine and GWT plugins](http://code.google.com/appengine/docs/java/tools/eclipse.html): I&#8217;m having a hate/love relationship with those tools. I don&#8217;t like how they take over your project with their inflexibility, but when they work, they work and don&#8217;t get in your way ([update site](http://dl.google.com/eclipse/plugin/3.6))
  * [Vaadin](http://vaadin.com/eclipse): Not essential for every one, but I am developing a Vaadin application after all. The plugin configures your workspace and also has easy access to handy tools, such as widgetset compilation ([update site](http://vaadin.com/eclipse))

## Freshly Added

I&#8217;ll also be adding a few plugins that I have experimented with and I think will be useful enough:

  * [Groovy plugin](http://groovy.codehaus.org/Eclipse+Plugin): For some reason I keep ignoring Groovy. That really needs to change as it seems to be a great mix of Jave and Python influences ([update site](http://dist.springsource.org/release/GRECLIPSE/e3.6/))
  * [Easyb](http://code.google.com/p/easyb/wiki/InstallingEclipsePlugin): I&#8217;m liking this framework for its top-down approach. Start by creating user stories, fill in the test code later. (and it&#8217;s written in Groovy, which gives me another reason to learn Groovy) I will probably be writing more on Easyb in the future ([update site](http://easyb.googlecode.com/svn/trunk/eclipse-plugins/org.easyb.eclipse.updatesite/))

## Removed Plugins

There are also a few plugins that I didn&#8217;t reinstall. Mostly because they are pretty memory and processor intense. They are useful, but I just couldn&#8217;t justify keeping them around.

  * Spring IDE, I&#8217;m probably not going to install this one as I&#8217;m phasing out Spring for my current hobby project. I also have a feeling SpringSource is starting to force us to download the standalone version of those tools, not the plugins. Which I don&#8217;t like (the Spring IDE org site seems to have disappeared of the face of the earth)
  * [m2eclipse](http://m2eclipse.sonatype.org/): Although I could really love this plugin. It was way too slow for me, so I&#8217;m not reinstalling this and I&#8217;m sticking with &#8220;mvn eclipse:eclipse&#8221; although that&#8217;s not perfect either.
  * [AspectJ](http://www.eclipse.org/aspectj/) integration: I installed this to use the annotation base dependency injection in Spring. It never worked quite right. I&#8217;m not sure if this was caused by AspectJ or the SpringIDE. I tried to figure it out, but when I realized I was loosing more time than I gained, I decided to just drop Spring dependency injection altogether (using the Vaadin data model, there aren&#8217;t too many dependencies anyway)

That&#8217;s my list. Feel free to share your favorites in the comments.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->