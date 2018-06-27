---
id: 411
title: The YouTube Flash Video (FLV) secret
date: 2008-10-21T14:00:55+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=411
permalink: /youtube-flash-video-flv-secret/
enclosure:
  - |
    http://n4061ad.doubleclick.net/pfadx/com.ytpwatch.entertainment/main_617
    241
    video/x-ms-asf
    
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/10/youtube3.png
dsq_thread_id:
  - "5920010"
categories:
  - Flash and ActionScript
---
I&#8217;m sorry for the hyperbole in the title, but it really is something YouTube is very <a title="hush-hush | thesaurus" href="http://thesaurus.reference.com/search?q=hush-hush" target="_blank">hush-hush</a> about. In spite of that, direct access to **the <a title="Flash Video" href="http://en.wikipedia.org/wiki/FLV" target="_blank">Flash Video</a> file of YouTube movies** gives you a very powerful tool. You have **total control** over: when, how and where you play the video.

A recap of **the ActionScript 3.0 YouTube player** series:

  * <a title="Little Known Way to Create a Fully Customizable ActionScript 3.0 YouTube Player - Streamhead" href="../create-fully-customizable-actionscript-30-youtube-player/" target="_blank">Getting <strong>a list of videos</strong> (and some project setup)</a>
  * <a title="what you should know about flash.display.StageScaleMode" href="http://www.streamhead.com/flash-developer-flashdisplaystagescalemode/" target="_blank">A bit about how <strong>the Flash stage</strong> works and <strong>fullscreen</strong></a>
  * Install **a php script** to get the randomly generated key [this post]
  * Getting the **key for a video** [later post]
  * playing the video using **Flash’s FLV player** classes [later post]

Before we get started, I would like to make clear that, strictly speaking you may be violating <a title="YouTube Terms of Use" href="http://www.youtube.com/t/terms" target="_blank">the YouTube terms of use</a>. I suggest that you make sure that you have a linkback somewhere to the original YouTube page of any video you play this way. As long as it&#8217;s not intended for commercial use, I don&#8217;t think YouTube will mind. This also means that evrything in this post could break at any moment. YouTube has no obligation to keep things working the way they are. [Use at your own risk and make sure you have a backup plan](http://www.streamhead.com/beware-web-20-developer-stable-apis/ "web 2.0 developer: how stable are those apis?").

**How does YouTube work**:

  1. Lets take for instance the video at this url : <a title="Nice pants" href="http://www.youtube.com/watch?v=tlkd45W4TWU" target="_blank">http://www.youtube.com/watch?v=tlkd45W4TWU</a>
  2. In the URL above, you can see **the YouTube video ID**, visibly **tlkd45W4TWU**.
  3. If you load that page and analyze it, the definition of the embedded Flash player is particularly interesting. You can get to it using, for instance, <a title="Firebug" href="http://getfirebug.com/" target="_blank">Firebug</a>
  4. The flashvars and more specifically the &#8220;t=&#8221; part are especially interesting (lets call it the **T-parameter**) <pre lang="html"></pre>

  5. If you take a look at the network traffic (again Firebug is brilliant for this) you will notice a new request: http://www.youtube.com/get_video?**video_id=tlkd45W4TWU**&**t=OEgsToPDskJVR3U-M0h8Jfmjm804cAEx**
  6. This URI uses both the video id and T-parameter and is the one that returns the actual FLV file.

So what we need to do, is obtain the video_id, use that to request the page, extract the T-parameter and, finally, request the FLV. Because of <a title="Security error accessing url" href="http://www.wombatnation.com/2008/04/security-error-accessing-url" target="_blank">Flash&#8217;s security policies</a>, we cannot execute this request to the YouTube page from within the Flash applet. The easiest solution is to deploy a small server side script. <a title="YouTube Flash AS3 API" href="http://www.lostinactionscript.com/blog/index.php/2007/10/13/flash-you-tube-api/" target="_blank">Again the work has already been done for you</a>:

I&#8217;ve deployed this PHP script on [my random YouTube player](http://www.thecouchtv.com). And for the example above, [this is the result](http://www.thecouchtv.com/getVideoId.php?url=http://www.youtube.com/watch?v=tlkd45W4TWU).

## Conclusion

This part was a pretty technical overview of how YouTube deals with its video id&#8217;s and how the Flash Video file is requested from the server. A simple script can be deployed to perform the task of extracting this FLV. With the FLV URI, we now have complete control over the YouTube stream. This will be shown in the next installments of the series.

<a title="We open I.D." href="http://flickr.com/photos/yonnage/2890550080/" target="_blank">Image source</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->