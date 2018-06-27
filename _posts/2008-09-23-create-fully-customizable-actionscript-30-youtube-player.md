---
id: 315
title: Little Known Way to Create a Fully Customizable ActionScript 3.0 YouTube Player
date: 2008-09-23T10:00:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=315
permalink: /create-fully-customizable-actionscript-30-youtube-player/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/09/youtube1.png
dsq_thread_id:
  - "5438002"
image: /wp-content/uploads/2008/09/youtube1.png
categories:
  - Flash and ActionScript
---
So you want to **integrate YouTube videos in your Flash application** and think that the <a title="YouTube API" href="http://code.google.com/apis/youtube/overview.html" target="_blank">YouTube API</a> will get you there. If you&#8217;re doing **ActionScript 3.0** development, it won&#8217;t. However, in this post and a bunch of follow-ups, I&#8217;ll show you how it is possible to get that video playing. See <a title="The Couch TV - random video for your entertainment" href="http://www.thecouchtv.com/" target="_blank">TheCouchTV, the random YouTube player</a>, for an example. Jut click on the video to make it go full screen.

The first thing you&#8217;ll notice if you go to Google&#8217;s API site, is that everything is for **JavaScript and ActionScript 2.0**. No problem you&#8217;ll say, I don&#8217;t feel like learning AS2, but I do know my way around JavaScript. That&#8217;s all fine, until you want to play that video fullscreen. Due to security constraints, it is not possible to **fullscreen** a Flash applet from outside the applet (pretty reasonable if you ask me). So you need to add a button inside Flash, but the fully customizable and chromeless YouTube player is AS2, so it cannot be easily integrated in an AS3 application.

It is possible, and it will be the first thing you&#8217;ll find when you start Googling for solutions. There are <a title="Sample Code: Using the API with AS3" href="http://groups.google.com/group/youtube-api-gdata/browse_thread/thread/3c98068961296b38/aacc52cc732cf979" target="_blank">a bunch of <strong>wrappers</strong> that can make it work</a>, but they don&#8217;t feel &#8220;right&#8221;. It&#8217;s messy, especially if you like to be in full control. If you look even further, most likely, you&#8217;ll end up on <a title="Lost In Actionscript - Shane McCartney" href="http://www.lostinactionscript.com/blog/" target="_blank">Shane McCartney&#8217;s excellent Flash blog</a>, which has <a title="You Tube Flash AS3 / AS2 API  »  Lost In Actionscript - Shane McCartney" href="http://www.lostinactionscript.com/blog/index.php/2007/10/13/flash-you-tube-api/" target="_blank">a nice Flex application showing you how to <strong>directly access the YouTube FLV files</strong></a>. **No need for the YouTube supplied Flash applet**. The code is available, it&#8217;s just not very well documented. The AS3 sample underneath the player won&#8217;t even work, because Shane changed the API afterwards.

<div style="float:right;">
  <a title="Stairs to Home" href="http://www.flickr.com/photos/30264437@N02/2864769851/" target="_blank"><img src="http://farm4.static.flickr.com/3212/2864769851_55c93f4130_m.jpg" border="0" alt="Stairs to Home" /></a><br /> <small><a title="Attribution-ShareAlike License" href="http://creativecommons.org/licenses/by-sa/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="Ivy Dawned" href="http://www.flickr.com/photos/30264437@N02/2864769851/" target="_blank">Ivy Dawned</a></small>
</div>

This series of posts will show you the key features of the YouTube interface Shane created and it will begin to expand on it. As the Flex GUI components are not available to FlashDevelop users, I won&#8217;t go into those. But I will give you some info to directly stream it using standard Flash objects, no need for external libraries. I&#8217;ll just use the API to get a list of videos, pick a random one and start playing it. These are the steps needed to get it work. I&#8217;ve split them up to not make the posts too long:

  * Getting **a list of videos** (and some project setup) [in this post]
  * <a title="what you should know about flash.display.StageScaleMode" href="http://www.streamhead.com/flash-developer-flashdisplaystagescalemode/" target="_blank">A bit about how <strong>the Flash stage</strong> works and <strong>fullscreen</strong></a>
  * Install **a php script** to get the randomly generated key [later post]
  * Getting the **key for a video** [later post]
  * playing the video using **Flash&#8217;s FLV player** classes [later post]

Before we start, lets **configure a FlashDevelop project**

  * Make sure you use the latest version, <a title="FlashDevelop" href="http://www.flashdevelop.org/" target="_blank">FlashDevelop</a> (FD) is improving with every release, even a minor one. I&#8217;m using 3.0.0 Beta9 for this post.
  * Create a new AS3 project in a directory of your choice.
  * FD will create a directory structure. &#8220;bin&#8221; are the files you&#8217;ll upload to the webserver when everything is done. &#8220;src&#8221; holds your ActionScript files and &#8220;lib&#8221; everything else (like images)
  * <a title="Shane McCarthy's YouTube AS3 library" href="http://www.flashdynamix.com/downloads/youTube.zip" target="_blank">Download Shane&#8217;s youTube.zip file with his YouTube library</a> and extract it.
  * Copy the &#8220;com&#8221; directory in &#8220;currentas3classes&#8221; into your own &#8220;src&#8221; directory. (Don&#8217;t overwrite Main.as, we can&#8217;t use it, because it uses Flex classes not available freely)
  * FlashDevelop should notice this automatically and add the &#8220;com&#8221; directory structure to your project.
  * Open the Main.as in your project (FD created a base layout for you)
  * Ready to go.

First things first. Before you can start developing and running your YouTube applications, you should **get your own developer key**. <a title="YouTube API Developer Home" href="http://code.google.com/apis/youtube/dashboard/" target="_blank">This is a really painless procedure</a>, it will take you less then two minutes, even less if you already have a Google account (who hasn&#8217;t?). When you have this key, open the YouTube.as file in com/flashdynamix/services. On line 14 you&#8217;ll see the variable that you need to change (it&#8217;s a public variable, so you could do it in the main, but I think it&#8217;s better to do it here)

<pre lang="ActionScript">public static var clientKey : String = "ytapi-XXXXXXXX-YYYYYYYYY-vuj2k916-0";</pre>

With that little thing out of the way, it&#8217;s time to discover the YouTube.as class. This is the central class you will be using to access all data on YouTube. This class works **asynchronuously**. You launch a method (for instance videosForTag) and it will just return nothing. In the background the class sends a request to YouTube and when the response is received, it will generate an event.

The main program should then be **listening to that event** and it can read and process the result at that point. It will be much clearer with a little code. I added a YouTube private variable and two listeners, the init method is than really short and clean:

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
						for each (var video:Object in e.value.items) {
							trace(video.title + " - " + video.link);
						}
					} catch (evt:ArgumentError) {
						trace("ERROR : No Videos For Tag");
					}
					break;
			}
		}

		private function onError(e:ErrorEvent):void {
			trace("IOError : " + e );
		}

	}

}</pre>

So what happens when you run the program:

  1. When the object is initialized, the init method is called.
  2. The init method instantiates a YouTube object and attaches 2 event listeners. One for when an error is encountered during a request and one for when the request is completed.
  3. As a last step, the method videosForTag is invoked. This will send a request to YouTube and get the first 20 movies that match the &#8220;Lego&#8221; tag.
  4. If an error occurs (for instance, no Internet connection), the onError method called to display the error.
  5. If no error occurs, the onLoaded method is called and it will print out the title and url for each of the 20 movies that were found.

That&#8217;s pretty much all there is to it. Depending on which method you call on the YouTube object, it will return a CustomEvent with a different id. If you want to experiment, add a default option that traces the id and you&#8217;re on your way.

In this post we saw the YouTube class and how it can be used to asynchronuously connect to the YouTube API to get lists of videos. The next step is going to be to actually play one of those movies. If you can&#8217;t wait, go ahead and check out the rest of Shane&#8217;s code, that&#8217;s the way I learned it. It&#8217;s really not that hard.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->