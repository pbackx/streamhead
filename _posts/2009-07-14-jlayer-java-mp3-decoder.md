---
id: 1419
title: JLayer, Java MP3 decoder
date: 2009-07-14T10:00:31+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1419
permalink: /jlayer-java-mp3-decoder/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/07/mp3_player.png
dsq_thread_id:
  - "25401034"
categories:
  - Java and JavaScript
---
For a hobby project, I wanted to play and analyze MP3 files from a Java program. It turns out that&#8217;s not as easy as you might think. Probably due to licensing issues MP3 playback is not included with the standard Java development kit. Luckily there are some great people at <a title="JZoom" href="http://www.javazoom.net/" target="_blank">JZoom (formerly JavaZoom)</a> have created an open source library to help out: <a title="MP3 library for the Java platform" href="http://www.javazoom.net/javalayer/javalayer.html" target="_blank">JLayer (formerly JavaLayer)</a>.

The documentation is minimal, but who needs it when programming a Java MP3 player is as simple as:

<pre lang="java">new Player(new FileInputStream(args[0])).play();</pre>

The code itself is also very legible, which is nice if you plan to mess with it. And they have a few add-ons. The one you will want is the JavaSound standard library. Using <a title="MP3 SPI for Java Sound" href="http://www.javazoom.net/mp3spi/mp3spi.html" target="_blank">MP3 SPI</a>, JLayer integrates perfectly with JavaSound, so you don&#8217;t actually need to learn any new APIs if you already know JavaSound.

<a title="MP3 Player ... on Flickr" href="http://www.flickr.com/photos/simplycute/1517615096/" target="_blank">Image credit</a>.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->