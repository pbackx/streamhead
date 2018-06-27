---
id: 2733
title: Debugging Vaadin custom components
date: 2010-10-19T10:00:07+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2733
permalink: /debugging-vaadin-custom-components/
dsq_thread_id:
  - "158510769"
categories:
  - Java and JavaScript
---
After releasing <a title="Powered by Reindeer, Vaadin, AppEngine all in one package" href="http://www.streamhead.com/powered-by-reindeer/" target="_blank">a very first glimpse at my Vaadin/Google  AppEngine framework</a>, I&#8217;ve been continuing development. I&#8217;m now at the point of creating my first Vaadin custom component. Vaadin&#8217;s custom components are part GWT widgets, part Java code that runs on the server. It&#8217;s a fairly intricate and advanced task, but <a title="Vaadin, promoting a toolkit via a book" href="http://www.streamhead.com/vaadin-promote-great-gwt-toolkit/" target="_blank">the Vaadin book explains it well</a>. As long as you keep <a title="Book of Vaadin - client site architecture" href="http://vaadin.com/book/-/page/architecture.client-side.html#figure.architecture.client-side" target="_blank">the Vaadin architectural overview</a> close by, most things will just work. But sometimes, you will want to debug your components. This requires a few leaps that aren&#8217;t very intuitive (not caused by Vaadin btw)

<!--more-->To debug GWT widgets, you must launch a special instrumented version of the Jetty server (bundled with the Google Eclipse plugins) and have a browser that communicates with that server. Either this is via a plugin or a custom browser. I know this sounds complicated, but Google&#8217;s Eclipse integration makes it very easy. I tip my hat to the Google engineers for this spectacular feat.

In order to get this development environment working, you&#8217;ll need to work around a few peculiar perks of those plugins.

## Invalid build paths for the SDKs

When you enable both the GWT and App Engine plugins in a project that was not created via those plugins, you have a high chance of seeing messages like these:

<pre>The App Engine SDK '&lt;...&gt;\war' on the project's 
build path is not valid</pre>

Or a similar error for the GWT SDK.

Apparently this is caused by a bug in both plugins. They require their dependencies to be first in the classpath order. So to solve those message you have to play a little with the order of dependencies in your Java build path. Place the Google dependencies high and the web application ones low.

With a little experimenting you should be able to get rid of those red crosses.

## Out of memory when instantiating the widgets

When you launch the server in debug mode and open the application in a browser. The browser plugin will contact the server, which in turn will instantiate the widgets. This always kept failing on me with the following error message:

<pre>18:20:17.435 [ERROR] [com.example.xxx.widgetset.xxxWidgetset] 
Failed to create an instance of 
'com.vaadin.terminal.gwt.client.WidgetSet' via deferred binding</pre>

and the server will also offer you this helpful message:

<pre>18:20:17.558 [ERROR] [com.example.xxx.widgetset.xxxWidgetset] 
Out of memory; to increase the amount of memory, use the 
-Xmx flag at startup (java -Xmx128M ...)</pre>

Sadly though, this message is of no use, I tried increasing the heap size by a lot, nothing changed until I increased the permanent generation size:

<pre>-XX:MaxPermSize=512M</pre>

Everything worked flawlessly from there on.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->