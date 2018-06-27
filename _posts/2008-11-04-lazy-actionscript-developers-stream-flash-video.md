---
id: 450
title: 'The Lazy ActionScript Developer&#8217;s Way to Stream Flash Video'
date: 2008-11-04T10:00:40+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=450
permalink: /lazy-actionscript-developers-stream-flash-video/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/10/youtube5.png
dsq_thread_id:
  - "6605993"
image: /wp-content/uploads/2008/10/youtube5.png
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
In this final installment of my tutorial on YouTube hacking, I&#8217;m going to show **how to build the FLV URL for YouTube videos** and start **streaming the FLV** in your ActionScript application. As you will notice, this is very little work, because it is based on the streaming example in the AS3 language reference. I&#8217;m being lazy.

A recap of **the ActionScript 3.0 YouTube player** series:

  * <a title="Little Known Way to Create a Fully Customizable ActionScript 3.0 YouTube Player - Streamhead" href="../create-fully-customizable-actionscript-30-youtube-player/" target="_blank">Getting <strong>a list of videos</strong> (and some project setup)</a>
  * <a title="what you should know about flash.display.StageScaleMode" href="http://www.streamhead.com/flash-developer-flashdisplaystagescalemode/" target="_blank">A bit about how <strong>the Flash stage</strong> works and <strong>fullscreen</strong></a>
  * <a title="The YouTube Flash FLV secret you should know" href="http://www.streamhead.com/youtube-flash-video-flv-secret/" target="_blank">Install <strong>a php script</strong> to get the video parameters<br /> </a>
  * <a title="Tying the YouTube Services Together" href="http://www.streamhead.com/tying-youtube-services-pro-web-20-developer/" target="_blank">Getting the <strong>parameters for a video</strong></a>
  * playing the video using **Flash’s FLV player** classes [this post]

## Constructing the YouTube video URL

There are several ways to get to this one. You could fire up FireBug and check the network logs, or you could check <a title="YouTube AS3 API" href="http://www.lostinactionscript.com/blog/index.php/2007/10/13/flash-you-tube-api/" target="_blank">Shane&#8217;s code</a> and open his Main.as class. Skip to line 67 and you&#8217;ll see:

<pre lang="ActionScript">case YouTube.VIDEOID :
	fvc.play(YouTube.FLVUrl + e.value.id + "&t=" + e.value.t);
	break;</pre>

What this means: to construct the full URL to a YouTube Flash video file, you take the base URL and add both the video id and the T-parameter as arguments. An example URL might look like this:

http://www.youtube.com/get_video?**video_id**=v6ICEpYEcD8&**t**=OEgsToPDskIltmXs7gZ89kc2a3Z1SRGN

(I have not linked the URL, as it probably won&#8217;t work, because the T-parameter changes over time)

## Streaming the FLV

For this one I&#8217;m going to use the existing ActionScript 3 classes. In particular <a title="flash.net.NetConnection language reference" href="http://livedocs.adobe.com/flex/3/langref/flash/net/NetConnection.html" target="_blank">flash.net.NetConnection</a> and <a title="flash.net.NetStream language reference" href="http://livedocs.adobe.com/flex/3/langref/flash/net/NetStream.html" target="_blank">flash.net.NetStream</a>. In the following code I&#8217;m adding <a title="flash.net.NetStream example" href="http://livedocs.adobe.com/flex/3/langref/flash/net/NetStream.html#includeExamplesSummary" target="_blank">the language reference example</a> to the already existing code.

What happens might not be clear when you look at the code. That&#8217;s because we use a lot of event handlers. But if you take your time and go over the code it will become clear. What goes on is this:

  1. We create a NetConnection.
  2. If this goes well the netStatusHandler is called with the event &#8220;NetConnection.Connect.Success&#8221;. This in turn will launch the YouTube query to locate a video and create the URL to play it.
  3. This part we&#8217;ve already discussed in previous posts: 
      1. Create the YouTube object and add listeners.
      2. Get a list of videos for a tag.
      3. When that lists returns, select the first one and get the T-parameter from our PHP script
  4. We construct the YouTube FLV URL (see above) and call the play method.
  5. The play method creates a NetStream and Video object and starts the play the video.

Everything else you see is basically code to handle possible errors:

<pre lang="ActionScript">package
{
  import com.flashdynamix.events.CustomEvent;
  import com.flashdynamix.services.YouTube;
  import flash.display.Sprite;
  import flash.events.AsyncErrorEvent;
  import flash.events.ErrorEvent;
  import flash.events.Event;
  import flash.events.NetStatusEvent;
  import flash.events.SecurityErrorEvent;
  import flash.media.Video;
  import flash.net.NetConnection;
  import flash.net.NetStream;

  public class Main extends Sprite {
    private var connection : NetConnection;
    private var stream : NetStream;
    private var video : Video;
    private var yt : YouTube;

    public function Main():void {
      if (stage) init();
      else addEventListener(Event.ADDED_TO_STAGE, init);
    }

    private function init(e:Event = null):void {
      removeEventListener(Event.ADDED_TO_STAGE, init);

      trace("creating NetConnection");
      connection = new NetConnection();
      connection.addEventListener(NetStatusEvent.NET_STATUS, netStatusHandler);
      connection.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
      connection.connect(null);
    }

    private function netStatusHandler(event : NetStatusEvent):void {
      switch (event.info.code) {
        case "NetConnection.Connect.Success":
          connectStream();
          break;
        case "NetStream.Play.StreamNotFound":
          trace("Unable to locate video");
          break;
        case "NetStream.Play.Start":
          trace("start playing");
          break;
        case "NetStream.Play.Stop" :
          trace("stop playing");
          break;
      }
    }

    private function securityErrorHandler(event:SecurityErrorEvent):void {
      trace("securityErrorHandler: " + event);
    }

    private function connectStream():void {
      trace("start YouTube search");
      yt = new YouTube();
      yt.addEventListener(Event.COMPLETE, onLoaded);
      yt.addEventListener(ErrorEvent.ERROR, onError);
      yt.videosForTag("lego");
    }

    private function onLoaded(e:CustomEvent):void {
      switch (e.id) {
        case YouTube.SEARCH :
          trace("search finished");
          try {
            trace("first item : " + e.value.items[0].title + " - " + e.value.items[0].link);
          } catch (evt:ArgumentError) {
            trace("ERROR : No Videos For Tag");
          }
          trace("requesting the video id and t-parameter");
          yt.videoId(e.value.items[0].link);
          break;
        case YouTube.VIDEOID :
          trace("loaded: video id = " + e.value.id + " and T-parameter = " + e.value.t);
          play(YouTube.FLVUrl + e.value.id + "&t=" + e.value.t);
          break;
      }
    }

    private function onError(e:ErrorEvent):void {
      trace("IOError : " + e );
    }

    private function play(url:String):void {
      trace("playing: " + url);
      stream = new NetStream(connection);
      stream.addEventListener(NetStatusEvent.NET_STATUS, netStatusHandler);
      stream.addEventListener(AsyncErrorEvent.ASYNC_ERROR, asyncErrorHandler);
      video = new Video();
      video.attachNetStream(stream);
      stream.play(url);
      addChild(video);
    }

    private function asyncErrorHandler(event:AsyncErrorEvent):void {
      // ignore AsyncErrorEvent events.
    }
  }
}</pre>

I&#8217;ve put <a title="a zip file with all files used in this 5 part tutorial" href="http://www.streamhead.com/wp-content/uploads/2008/10/ytposts.zip" target="_blank">all files we used in the tutorials in a handy zip file</a>. Just expand and open in FlashDevelop.

## Conclusion

In this 5th and final post of the series I have shown how to actually **stream the YouTube FLV**. It was particularly easy because Flash already has everything you need. It&#8217;s a matter of finding the right classes and using them.

That wraps up the 5 part tutorial. Feel free to leave a comment if you found this useful or not. I&#8217;m also open for suggestions for improvements or other subjects for future tutorials.

<a title="lazy on Flickr" href="http://flickr.com/photos/50826080@N00/2235601624/" target="_blank">Image credit</a>.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->