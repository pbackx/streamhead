---
id: 329
title: What Every Flash Developer Ought to Know About flash.display.StageScaleMode
date: 2008-09-30T10:00:37+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=329
permalink: /flash-developer-flashdisplaystagescalemode/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/09/youtube2.png
dsq_thread_id:
  - "5438007"
image: /wp-content/uploads/2008/09/youtube2.png
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
While this post is only cursory related to using YouTube, it is important knowledge if you want to create fullscreen Flash applets and/or make sure they resize properly. So I have made it part of the series. In this post I&#8217;ll explain the <a title="flash.display.StageScaleMode" href="http://www.adobe.com/livedocs/flex/2/langref/flash/display/StageScaleMode.html" target="_blank">StageScaleMode</a>, which is a property that sometimes causes, what appears to be, weird behavior.

A recap of **the ActionScript 3.0 YouTube player** series:

  * <a title="Little Known Way to Create a Fully Customizable ActionScript 3.0 YouTube Player - Streamhead" href="http://www.streamhead.com/create-fully-customizable-actionscript-30-youtube-player/" target="_blank">Getting <strong>a list of videos</strong> (and some project setup)</a>
  * A bit about how **the Flash stage** works and **fullscreen** [this post]
  * [Install **a php script** to get the randomly generated key](http://www.streamhead.com/youtube-flash-video-flv-secret/)
  * [Getting the **key for a video**](http://www.streamhead.com/tying-youtube-services-pro-web-20-developer/)
  * [playing the video using **Flash&#8217;s FLV player** classes](http://www.streamhead.com/lazy-actionscript-developers-stream-flash-video/)

If you are an experienced Flash developer, you might want to skip this section, but it got me puzzled for a while. If you want to use the fullscreen mode of Flash, you&#8217;ll probably need a little knowledge of how a Flash applet can be resized. You could fix everything, so that images stay the same size, no matter how large your window is, but that would result in empty borders around the picture. It will look better if the video scales with the size of the applet. However, the interface elements usually don&#8217;t scale, or else you&#8217;d get giant play and pause buttons. To obtain this, you need to handle resizing yourself.

First I&#8217;d suggest to try out <a title="StageScaleMode example" href="http://www.streamhead.com/examples/StageScaleMode/" target="_blank">this basic applet</a>. It&#8217;s not user friendly, but it should give you an idea of how this thing works. Open it in a new window and resize away. Then change the scaleMode attribute to see how Flash handles resizing (click on the text to change it):

<a title="StageScaleMode example" href="http://www.streamhead.com/examples/StageScaleMode/" target="_blank"><img class="alignnone size-full wp-image-355" title="test applet" src="http://www.streamhead.com/wp-content/uploads/2008/09/tcw_512.jpg" alt="" width="500" height="281" srcset="http://www.streamhead.com/wp-content/uploads/2008/09/tcw_512.jpg 512w, http://www.streamhead.com/wp-content/uploads/2008/09/tcw_512-300x168.jpg 300w" sizes="(max-width: 500px) 100vw, 500px" /></a>

<a title="StageScaleMode.as source file" href="http://www.streamhead.com/wp-content/uploads/2008/09/stagescalemodesample.as" target="_blank">The full code is available</a>, but the important part is actually only a few lines:

<pre lang="ActionScript">private var modes:Array = new Array(StageScaleMode.EXACT_FIT,
				StageScaleMode.NO_BORDER,
				StageScaleMode.NO_SCALE,
				StageScaleMode.SHOW_ALL);
private var current:Number = 0;
private function changeMode(event:MouseEvent):void {
	stage.scaleMode = modes[++current % 4];
	modeText.text = "current stage scale mode: " + stage.scaleMode;
	event.stopPropagation();
}</pre>

Setting the **stage.scaleMode** attribute makes all the difference when resizing. Everytime you click on the text, the program will rotate over the 4 different possible values for the scaleMode:

  * **StageScaleMode.EXACT_FIT**: This stretches the image to fit the entire screen. Thus the image is deformed. You&#8217;re probably never going to need this mode, unless in very special circumstances.
  * **StageScaleMode.NO_BORDER**: Makes sure that the application fills the entire screen without deforming. No borders will be visible (unlike SHOW_ALL), but some parts of the application might drop of the screen. When using this mode, take extra care that user interface elements do not fall of the screen. In example applet, if you resize it just right, you can no longer change the mode. This is not exactly what you&#8217;d want in a finished application.
  * **StageScaleMode.NO_SCALE**: This is the easiest mode: just leave everything as is. This is the mode you want if you need complete control.
  * **StageScaleMode.SHOW_ALL**: Always show the entire applet, and keep the aspect ratio fixed (no stretching). In many cases this will be the best choice. It might however cause borders to appear alongside your applet.

Once you got that working, **the Flash fullscreen mode** is really a piece of cake. You need to do two things to make it happen:

  * In the ActionScript code change the display state of the stage:

<pre lang="ActionScript">stage.displayState = StageDisplayState.FULL_SCREEN;</pre>

  * If you run the applet now, you will get a security exception. On the page where you use the applet, you must explicitly specify that the applet is allowed to go fullscreen. If you use the index.html that FlashDevelop generates for you, you need to add the &#8220;**allowFullScreen**&#8221; parameter to the JavaScript loader:

<pre lang="JavaScript">var params = {
	menu: "false",
	scale: "noScale",
	<strong>allowFullScreen: "true"</strong>
};</pre>

Note:

  * I have now added the SWF metadata to specify screen size. I find it a little more convenient than specifying it in the properties. <a title="AS3 Projects and the SWF Metadata tag" href="http://blog.madebyderek.com/archives/2007/01/12/as3-projects-and-the-swf-metadata-tag/" target="_blank">See Derek&#8217;s post about it for more info</a> [<a title="Setting the width and height of a pure-ActionScript application" href="http://www.morearty.com/blog/2006/06/27/setting-the-width-and-height-of-a-pure-actionscript-application/" target="_blank">via the comments here</a>].

### Conclusion

In this post I&#8217;ve shown you that the StageDisplayState could be important to your Flash applet and how to use it. I have also demonstrated how easy it is to go full screen in Flash. I hope you enjoyed this post and let me know if you create anything based on it.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->