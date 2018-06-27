---
id: 1601
title: 'Android Tutorial: Creating and Using an SD Card in the Emulator'
date: 2009-10-30T11:00:30+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1601
permalink: /android-tutorial-sd-card/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/10/wall-e_sdcard_reader.png
dsq_thread_id:
  - "42557030"
categories:
  - Java and JavaScript
---
In <a title="Android, No-cost Development Platform" href="http://www.streamhead.com/android-nocost-development-platform/" target="_blank">a previous post</a>, I mentioned how user-friendly Android is for developers. There&#8217;s extensive documentation and information on the architecture, the different components and best practices. However, the documentation has a few blind spots. Many of the tools have little documentation and no usage examples. The information is there, it&#8217;s just hidden behind a few layers of Android theory.

So I&#8217;m going to try and document a few of the basic things that you&#8217;ll probably need to know to start developing Android applications. Only for beginners and intermediate Android developers.

The first issue I ran into was trying to load files into the Android emulator. For instance, if you want to load MP3 files on a &#8220;real&#8221; Android phone, you&#8217;ll probably insert an SD card into the phone. The emulator can emulate this, but you need to jump through a few hoops:

**1.**

 **** First, you will need to create an SD card image file. This is comparable to, for instance, an ISO image of a CD-ROM. Creating an image is done via the <a title="mksdcard" href="http://developer.android.com/guide/developing/tools/othertools.html#mksdcard" target="_blank">mksdcard</a> tool. For instance:

<pre>mksdcard -l mysdcard 128M sdcard.img</pre>

**2.**

If you want to access the image, the emulator must be running with the image loaded. I&#8217;m going to assume you&#8217;re using the Eclipse tools. In there you need to specify the image on the command line. Open the &#8220;Run configurations&#8230;&#8221; dialogue and configure the image as follows (don&#8217;t forget to put in the correct directory)

[<img class="alignnone size-medium wp-image-1625" title="android_sdcard_commandline_config" src="http://www.streamhead.com/wp-content/uploads/2009/10/android_sdcard_commandline_config-300x267.png" alt="android_sdcard_commandline_config" width="300" height="267" srcset="http://www.streamhead.com/wp-content/uploads/2009/10/android_sdcard_commandline_config-300x267.png 300w, http://www.streamhead.com/wp-content/uploads/2009/10/android_sdcard_commandline_config.png 800w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2009/10/android_sdcard_commandline_config.png)

**3.**

Next start the emulator and verify that the SD card is loaded. The best way to do this is in the DDMS tool. To access it: click on the open perspective button:

[<img class="alignnone size-medium wp-image-1627" title="android_ddms_perspective" src="http://www.streamhead.com/wp-content/uploads/2009/10/android_ddms_perspective-300x200.png" alt="android_ddms_perspective" width="300" height="200" srcset="http://www.streamhead.com/wp-content/uploads/2009/10/android_ddms_perspective-300x200.png 300w, http://www.streamhead.com/wp-content/uploads/2009/10/android_ddms_perspective.png 430w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2009/10/android_ddms_perspective.png)

If the DDMS isn&#8217;t in the list, click &#8220;Other&#8230;&#8221; and choose it from there. Open the file explorer and you should be able to open the sdcard:

[<img class="alignnone size-medium wp-image-1628" title="android_file_explorer" src="http://www.streamhead.com/wp-content/uploads/2009/10/android_file_explorer-300x130.png" alt="android_file_explorer" width="300" height="130" srcset="http://www.streamhead.com/wp-content/uploads/2009/10/android_file_explorer-300x130.png 300w, http://www.streamhead.com/wp-content/uploads/2009/10/android_file_explorer.png 628w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2009/10/android_file_explorer.png)

**4.**

Add files to the sdcard: There are two options: either you can use the two icons in the top right corner of the DDMS tools (<img class="alignnone size-full wp-image-1629" title="android_pull_push" src="http://www.streamhead.com/wp-content/uploads/2009/10/android_pull_push.png" alt="android_pull_push" width="63" height="25" />) or you can use the command line tools. The following command pushes the file to your sdcard:

<pre>adb push <span style="font-style: italic;">myfile.mp3</span> /sdcard/</pre>

Not that the location on the Android phone (the &#8220;/sdcard/&#8221; part) needs to have &#8220;unix-style&#8221; forward slashes, so keep that in mind if you&#8217;re running on Windows.

**5.**

And that&#8217;s it. the file should appear in the DDMS file explorer. Next time, we&#8217;ll try to actually do something with the file we places on the Android emulator.

<a title="Wall-e Project on Flickr" href="http://www.flickr.com/photos/exalthim/3400989063/" target="_blank">Image credit</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->