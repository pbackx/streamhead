---
id: 371
title: Web 3.0? Probably Not, But Java Applets Enable a New Way of Visualization.
date: 2008-10-07T14:00:24+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=371
permalink: /web-30-java-applets-enable-visualizing/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/09/web30.png
dsq_thread_id:
  - "5467867"
categories:
  - Java and JavaScript
---
In spite of many efforts, the web has mostly been a **two dimensional** affair. Until now.

Meet **<a title="Free web3D platform" href="http://www.3dxplorer.com/" target="_blank">3DXplorer</a>**, a plugin-less way of showing **3 dimensional scenes** (you know, games) to the user. Web designers used to be limited to showing you a few pictures of an object from different angles to give an impression of what it would look like. Now 3DXplorer lets you **walk around the object, even interact with it** (not in this example)

<a title="Caveat emptor on Wikipedia" href="http://en.wikipedia.org/wiki/Caveat_emptor" target="_blank">Caveat emptor</a>:

  * 3DXplorer runs as **a Java applet**. That means you need a <a title="Java SE" href="http://java.sun.com/javase/downloads/index.jsp" target="_blank">Java runtime environment (JRE)</a> installed. Most of the times, that will be the case, but you could run into some issues if you don&#8217;t have a recent one.
  * It&#8217;s all very new, there&#8217;s **very little documentation** available on how to make stuff work and there are a few bugs in the editor, hence I don&#8217;t have a nice demonstration of interactivity.
  * If you think web, you think interconnections and links. This is not easily achievable. You can add links to web pages, but it&#8217;s not as easy as HTML.
  * There&#8217;s **no shadow** casting yet.

Obviously you could do something similar in Flash using the latest 3D toolkits, but the quality and size of scenes would be a lot lower (<a title="3D worlds and procrastinating" href="http://www.streamhead.com/heres-a-quick-way-to-feel-happy-about-procrastinating/" target="_blank">see the bigger demos</a>).

## A little tutorial

If you want to try it out yourself, just sign up on the 3DXplorer page, create a new project and you can start editing. There is a limited amount of presets and models available to get you going, but you can also import your own. I created the model above in <a href="http://www.streamhead.com/method-helping-homeowners-sneak-peak-remodeling-plans/" target="_blank">SketchUp</a> and imported it in 3DXplorer. This was really easy:

  1. Create a SketchUp model.
  2. Choose File > Export > 3D Model &#8230; and save your creation. If you have problems, save as Google Earth 4 file (this can be chosen in the box at the bottom, labeled &#8220;Export type&#8221;)
  3. Change the file extension of that file to zip and open it. Inside you&#8217;ll find a few files, but you only need the one ending in &#8220;dae&#8221;. Extract that one.
  4. Now open up your project and start editing.
  5. Inside the project, right click and choose &#8220;Add new object&#8221;
  6. On this dialog click &#8220;Upload files to collection&#8230;&#8221; and pick your file.
  7. In the Upload dialog, you might need to change the dimensions. I always have to divide by 100 for some reason.
  8. That&#8217;s it, you can place your object.
  9. The only thing I couldn&#8217;t get to work is importing textures.

## Conclusion

3D on the web seems to be the next step, but people are not very willing to adopt new plugins that are usually needed. Plugins that might not exist for your favorit platform or browser. 3DXplorer gets around this issue by using a plugin that is probably already installed on your system. In addition, It offers a simple, but limited interface to create your world.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->