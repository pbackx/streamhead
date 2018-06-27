---
id: 439
title: Tying the YouTube Services Together Like a Pro Web 2.0 Developer
date: 2008-10-28T10:00:23+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=439
permalink: /tying-youtube-services-pro-web-20-developer/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/10/youtube4.png
dsq_thread_id:
  - "6118586"
image: /wp-content/uploads/2008/10/youtube4.png
categories:
  - Flash and ActionScript
---
Connecting different webservices together could leave open the door to **attacks on your privacy** by malicious individuals. This post goes into how **Flash protects** you from this, but still leaves open possibilities to tie together interesting mashups. I also explain how this fits in the large picture of our YouTube project and give an example.

A recap of **the ActionScript 3.0 YouTube player** series:

  * <a title="Little Known Way to Create a Fully Customizable ActionScript 3.0 YouTube Player - Streamhead" href="../create-fully-customizable-actionscript-30-youtube-player/" target="_blank">Getting <strong>a list of videos</strong> (and some project setup)</a>
  * <a title="what you should know about flash.display.StageScaleMode" href="http://www.streamhead.com/flash-developer-flashdisplaystagescalemode/" target="_blank">A bit about how <strong>the Flash stage</strong> works and <strong>fullscreen</strong></a>
  * <a title="The YouTube Flash FLV secret you should know" href="http://www.streamhead.com/youtube-flash-video-flv-secret/" target="_blank">Install <strong>a php script</strong> to get the video parameters<br /> </a>
  * Getting the **parameters for a video** [this post]
  * playing the video using **Flash’s FLV player** classes [later post]

## Crossdomain.xml

<a title="Same origin policy" href="http://en.wikipedia.org/wiki/Same_origin_policy" target="_blank">Browsers do not allow websites to load resources from other domains</a>. There is a very good reason for that. It&#8217;s called a **<a title="Cross-site Scripting - Wikipedia" href="http://en.wikipedia.org/wiki/Cross_site_scripting" target="_blank">cross-site scripting</a> attack**. However, web 2.0 mashups inherintly use data from different domains. They&#8217;re called mashup for a reason. So JavaScript developers have figured out clumsy **workarounds** for the cross domain restrictions. If you&#8217;re a ActionScript developer, you&#8217;re in luck. The Flash player supports a <a title="Flash cross-domain policy files" href="http://blogs.adobe.com/stateofsecurity/2007/07/crossdomain_policy_files_1.html" target="_blank">crossdomain.xml</a> file, that makes it possible for web service owners to open up the &#8220;safe&#8221; parts of their service to cross-site scripting.

YouTube also implements this crossdomain.xml, but it **only opens the api** for outside Flash access. So if you use the feeds, for instance to get recent videos, this will work perfectly. You can check the <a href="http://gdata.youtube.com/crossdomain.xml" target="_blank">crossdomain.xml</a> on the gdata.youtube.com domain. However, the &#8220;normal&#8221; YouTube domain, where the videos and pages are <a href="http://youtube.com/crossdomain.xml" target="_blank">does not allow outside access</a>.

For videos, that&#8217;s not a problem, media files are not subject of this same origin policy. But this does mean that we cannot directly get the T-parameter because that is on the video page (<a title="The YouTube Flash FLV secret you should know" href="http://www.streamhead.com/youtube-flash-video-flv-secret/" target="_blank">see previous post for details</a>). Exactly for that reason, we created a little php script to help us out. This will reside on the same server as our Flash file, so we can access it without restrictions and it will get the T-parameter for us.

## The YouTube ActionScript class

Now lets get back to some ActionScript programming, shall we? Before you can use the method for getting **the video id and T-parameter**, you will need to change the **url of the php script**. Make sure the script is on the **same domain** as where you will be hosting the Flash file. As long as you are testing locally, you don&#8217;t need to worry about it, but it might be best to fix this straight away. This will save you some headaches in the future.

Open up src/com/flashdynamix/services/YouTube.as and change lines 19-21:

<pre lang="ActionScript">private static const servicesDomain : String = "http://YOURDOMAIN/YOURPATH/";
//private static const videoIdUrl : String = servicesDomain + "getVideoId.aspx";
private static const videoIdUrl : String = servicesDomain+"getVideoId.php";</pre>

Just fill in the domain and path of the php script. And depending on what you use (php or asp) comment the correct line (<a title="YouTube Flash AS3 API" href="http://www.lostinactionscript.com/blog/index.php/2007/10/13/flash-you-tube-api/" target="_blank">the original library</a> also comes with an asp implementation if you prefer that one). That&#8217;s all there is to it. Save the file and close. You are ready to try it out.

## Testing loading the video ID and T-parameter

Now that the setup is done, it&#8217;s really easy to get the video id and T-parameter. The YouTube class provides **a &#8220;videoId&#8221; method** just for this purpose. The following code is only a small change compared to <a title="Creating a fully customizable AS3 YouTube player" href="http://www.streamhead.com/create-fully-customizable-actionscript-30-youtube-player/" target="_blank">the code shown in the first post of the series</a>. It still gets 20 videos for the &#8220;lego&#8221; tag and afterwards it requests the parameters for the first video of that list.

<pre lang="ActionScript">package
{
	import com.flashdynamix.events.CustomEvent;
	import com.flashdynamix.services.YouTube;
	import flash.display.Sprite;
	import flash.events.ErrorEvent;
	import flash.events.Event;

	public class Main extends Sprite
	{
		private var yt : YouTube;

		public function Main():void
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		private function init(e:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);

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
					trace("loaded: video id = " + e.value.id + " and T-parameter = "+e.value.t);
					break;
			}
		}
		private function onError(e:ErrorEvent):void {
			trace("IOError : " + e );
		}
	}
}</pre>

The output will look like:

<pre>start YouTube search
search finished
first item : THE SIMPSONS intro lego style - http://www.youtube.com/watch?v=CgEIGx0JKL8
requesting the video id and t-parameter
loaded: video id = CgEIGx0JKL8 and T-parameter = OEgsToPDskIt_LVCPsgv_hVr5d7DIs6U</pre>

As you can see, **I added an event to listen for in the onLoaded method**. When the video parameters are received, the YouTube class will generate a **YouTube.VIDEOID** event, which is where we output the results. That&#8217;s really all there is to it.

## Conclusion

After this post, we are now **ready to start playing the video**. We have everything that is needed to load the FLV file. You could even download it to your harddrive if you wanted to. In the next post, I will explain the ActionScript 3 methods for playing a video.

<a title="original picture" href="http://flickr.com/photos/krazydad/212545979/" target="_blank">Image credit</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->