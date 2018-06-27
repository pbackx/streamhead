---
id: 1475
title: Audio Analysis Architecture Based On JLayer
date: 2009-08-11T10:00:24+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1475
permalink: /audio-analysis-jlayer-excel/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/08/tiers.png
dsq_thread_id:
  - "29047394"
categories:
  - Java and JavaScript
---
<a title="5 Free Audio Analysis Tools" href="http://www.streamhead.com/free-audio-analysis-tools/" target="_blank">As mentioned last week</a>, my next project revolves around audio analysis. The first step is acquiring data and for that,  <a title="JLayer, Java MP3 decoder" href="http://www.streamhead.com/jlayer-java-mp3-decoder/" target="_blank">I had already found the perfect Java solution</a>. JLayer makes it easy to obtain data, but a sound file contains very large amounts of it. This post goes into a basic architecture to tame that data and get it into a form that can be processed.

<a title="BeatIt 0.0 NetBeans project" href="http://www.streamhead.com/wp-content/uploads/2009/08/BeatIt_v0.0.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />Download the NetBeans example project</a>

There are a few ways to get the wave data out of an mp3 file using JLayer. <a title="MP3 SPI documentation" href="http://www.javazoom.net/mp3spi/documents.html" target="_blank">You could use the MP3SPI driver to play data through the JavaSound API and capture the bytes</a>. But there&#8217;s no reason to make it that complicated.

JLayer can stream data to its own AudioDevice class. This is a callback class that has hooks for opening and closing a device, which we don&#8217;t need. The important hook is the one that sends the bytes to the device. This is where you can capture the raw stream. Most audio analysis, however, doesn&#8217;t use the raw stream, but averages the data to reduce the amount of data to process.

<div style="float:right;">
  <a title="Everyone has layers.....OHh today I happened to make it to  100,000 views  luv ya all mwah xox" href="http://www.flickr.com/photos/21560098@N06/3802156991/" target="_blank"><img src="http://farm3.static.flickr.com/2549/3802156991_6d2bc0e2f3_m.jpg" border="0" alt="Everyone has layers.....OHh today I happened to make it to  100,000 views  luv ya all mwah xox" /></a><br /> <small><a title="Attribution License" href="http://creativecommons.org/licenses/by/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="1happysnapper( Challenge starts,be nice)" href="http://www.flickr.com/photos/21560098@N06/3802156991/" target="_blank">1happysnapper( Challenge starts,be nice)</a></small>
</div>

So that is how I ended up with my layered architecture:

  1. JLayer itself decodes the mp3 file and offers the byte stream to &#8230;
  2. &#8230; the audio device. This layer does only very basic processing. In the current example project you&#8217;ll find a device that averages the samples. I could add Fast Fourier Transform in the future.
  3. The final layer are the actual brains. I&#8217;ve called them &#8220;processor&#8221;. This is where the magic will happen.

That&#8217;s all there is to the current version of my project. For now it&#8217;s just a zip file, but if there is interest, I might put it on some public VCS.

The main advantage of the current architecture are:

  * There&#8217;s only one dependency to outside projects: JLayer. This has advantages for portability.
  * Splitting the basic processing that every analysis project needs anyway into its own layer, frees the actual processing from doing actual processing.

<a title="BeatIt 0.0 NetBeans project" href="../wp-content/uploads/2009/08/BeatIt_v0.0.zip" target="_blank"><img title="download" src="../wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />Download the NetBeans example project</a>

(<a title="Flickr photo" href="http://www.flickr.com/photos/eskimoblood/1141466676/" target="_blank">Image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->