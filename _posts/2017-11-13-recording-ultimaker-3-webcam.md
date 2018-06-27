---
id: 4109
title: Recording the Ultimaker 3 Webcam
date: 2017-11-13T18:43:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=4109
permalink: /recording-ultimaker-3-webcam/
image: /wp-content/uploads/2017/11/4603211518_49a80588cc_z-640x372.jpg
categories:
  - 3D Printing
---
So you&#8217;ve got this awesome Ultimaker 3 printer with a build-in webcam. But no way to record and review your prints later on. Are you going to sit around, babysitting your printer at night?

<!--more-->

Well, no, you don&#8217;t have to! The webcam broadcasts a video that you can watch (and record) from anywhere in your network.

There are two steps to recording your video:

  * Find the IP address of your printer. It&#8217;s three clicks in the printer&#8217;s menu.
  * Record the broadcast using your preferred software. Tip: VLC works on almost any platform and is free.

## Find the IP address

When your printer is powered on, pick &#8220;System&#8221; from the root menu:<figure id="attachment_4113" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-4113" src="http://www.streamhead.com/wp-content/uploads/2017/11/UM3_main_menu-300x169.jpg" alt="" width="300" height="169" srcset="http://www.streamhead.com/wp-content/uploads/2017/11/UM3_main_menu-300x169.jpg 300w, http://www.streamhead.com/wp-content/uploads/2017/11/UM3_main_menu-768x432.jpg 768w, http://www.streamhead.com/wp-content/uploads/2017/11/UM3_main_menu-1024x576.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2017/11/UM3_main_menu.jpg)<figcaption class="wp-caption-text">Ultimaker 3 main menu with System option highlighted.</figcaption></figure> 

Now open the &#8220;Network&#8221; menu:<figure id="attachment_4114" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-4114" src="http://www.streamhead.com/wp-content/uploads/2017/11/UM3_system_menu-300x169.jpg" alt="" width="300" height="169" srcset="http://www.streamhead.com/wp-content/uploads/2017/11/UM3_system_menu-300x169.jpg 300w, http://www.streamhead.com/wp-content/uploads/2017/11/UM3_system_menu-768x432.jpg 768w, http://www.streamhead.com/wp-content/uploads/2017/11/UM3_system_menu-1024x576.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2017/11/UM3_system_menu.jpg)<figcaption class="wp-caption-text">Ultimaker 3 system menu with Network option selected.</figcaption></figure> 

Finally select the &#8220;Connection Status&#8221; option and the IP address will show at the bottom of the screen.<figure id="attachment_4115" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-4115" src="http://www.streamhead.com/wp-content/uploads/2017/11/UM3_connection_status-300x169.jpg" alt="" width="300" height="169" srcset="http://www.streamhead.com/wp-content/uploads/2017/11/UM3_connection_status-300x169.jpg 300w, http://www.streamhead.com/wp-content/uploads/2017/11/UM3_connection_status-768x432.jpg 768w, http://www.streamhead.com/wp-content/uploads/2017/11/UM3_connection_status-1024x576.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2017/11/UM3_connection_status.jpg)<figcaption class="wp-caption-text">Ultimaker 3 connection status, showing the IP address of the printer.</figcaption></figure> 

Now you can construct the URL of the broadcast or stream. It looks like this:

<pre>http://&lt;YOUR IP ADDRESS HERE&gt;:8080/?action=stream</pre>

So in my case that would be _http://192.168.0.151:8080/?action=stream_. In your case, the IP address will be different, so the stream URL will also be slightly different.

You can open this URL in your browser to verify that it is correct. You should see the image of the webcam.

## Recording the Broadcast

There are many ways to record the video stream of your webcam. They can be simple or they can be complicated.

If you are not very technical, I would suggest you get yourself [VLC Media Player](https://www.videolan.org/vlc/). It&#8217;s free and it works on almost any system.

Before you start, you will want to configure the folder where the recordings are stored:

  * In the menu go to Tools > Preferences > Input/Codecs
  * Enter your folder in  Files > Record directory or filename<figure id="attachment_4110" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-4110" src="http://www.streamhead.com/wp-content/uploads/2017/11/vlc_configure_record_directory-300x240.png" alt="" width="300" height="240" srcset="http://www.streamhead.com/wp-content/uploads/2017/11/vlc_configure_record_directory-300x240.png 300w, http://www.streamhead.com/wp-content/uploads/2017/11/vlc_configure_record_directory-768x615.png 768w, http://www.streamhead.com/wp-content/uploads/2017/11/vlc_configure_record_directory.png 905w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2017/11/vlc_configure_record_directory.png)<figcaption class="wp-caption-text">Configure the folder where VLC will store recordings.</figcaption></figure> 

To record your stream, first open it by going to the &#8220;Media&#8221; menu item and choose &#8220;Open Network Stream&#8230;&#8221;<figure id="attachment_4111" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-4111" src="http://www.streamhead.com/wp-content/uploads/2017/11/vlc_open_stream-300x238.png" alt="" width="300" height="238" srcset="http://www.streamhead.com/wp-content/uploads/2017/11/vlc_open_stream-300x238.png 300w, http://www.streamhead.com/wp-content/uploads/2017/11/vlc_open_stream.png 540w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2017/11/vlc_open_stream.png)<figcaption class="wp-caption-text">Open a network stream in VLC</figcaption></figure> 

Next, record the stream by picking the &#8220;Record&#8221; option from the &#8220;Playback&#8221; menu.

To stop the recording, click the record option again.

That&#8217;s all there is to it. You can now go into the folder you selected and rewatch the print.

Don&#8217;t forget to check out [my other 3D printing articles](http://www.streamhead.com/category/3d-printing/), where you can learn to fix the most annoying problem with 3D prints: [making them fit properly](http://www.streamhead.com/make-3d-printed-parts-fit-together/).

([image credit](https://www.flickr.com/photos/tysonluneau/4603211518/in/photostream/))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->