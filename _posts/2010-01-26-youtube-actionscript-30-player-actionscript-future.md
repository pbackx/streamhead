---
id: 1791
title: YouTube ActionScript 3.0 Player, Welcome to the ActionScript future
date: 2010-01-26T10:00:53+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1791
permalink: /youtube-actionscript-30-player-actionscript-future/
Image:
  - http://www.streamhead.com/wp-content/uploads/2010/01/a_couch.png
dsq_thread_id:
  - "61534679"
categories:
  - Flash and ActionScript
---
This weekend, I finally brought <a title="The Couch TV - random YouTube at your command" href="http://www.thecouchtv.com/" target="_blank">The Couch TV</a>s frontpage up to date. It had been broken for a while, ever since my little YouTube ActionScript 3 hack stopped working. Since YouTube announced their ActionScript 3.0 player, a few months ago, there is no need for a hack anyway. Now there is a clean way to integrate YouTube in your ActionScript 3 programs.

Integration is incredibly easy, you can read <a title="YouTube ActionScript 3.0 Player API reference" href="http://code.google.com/intl/nl/apis/youtube/flash_api_reference.html" target="_blank">the documentation</a> in about 10 minutes and that&#8217;s really all you need to know. No hidden options or special URLs necessary.

I did create a small wrapper class, to make addressing the player a little more typesafe (and this also gives you autocompletion). Check out my <a title="The Couch TV SVN repo" href="http://svn.assembla.com/svn/thecouch/" target="_blank">Assembla SVN repository</a> for the full code of what you can see on <a title="The Couch TV - random YouTube at your command" href="http://www.thecouchtv.com/" target="_blank">The Couch TV</a> (there&#8217;s code for full screen in there that doesn&#8217;t work right now).

You can find the wrapper <a title="YouTubePlayer.as on Assembla SVN" href="http://svn.assembla.com/svn/thecouch/trunk/src/thecouch/YouTubePlayer.as" target="_blank">right here</a>. The YouTubePlayer class extends Loader, which means you can add it anywhere you like. The class first needs to load the actual YouTube player on YouTube.com. This means you need to wait until everything is loaded before you can use the player. In ActionScript code it looks like this:

<pre lang="ActionScript">package thecouch 
{
	import flash.display.Sprite;
	import flash.events.Event;
	/**
	 * @author Peter Backx - thecouchtv.com
	 */
	public class SimpleExample extends Sprite 
	{
		private var player:YouTubePlayer;
		
		public function SimpleExample() 
		{
	        addChild(player = new YouTubePlayer());
			player.addEventListener(YouTubePlayer.PLAYER_READY, playerReady);
		}
		
		private function playerReady(event:Event):void 
		{
			player.loadVideoById("2gGopKNPqVk");
		}
	}
	
}</pre>

I&#8217;ve also added wrappers for the loadVideoByUrl methods and a listener for the &#8220;ended&#8221; even. That means, you can use those directly on the YouTubePlayer object. You&#8217;ll have nice code completion in your editor. And unlike the example in the documentation this means you also have compile time type safety. The joy of typesafe object oriented programming.

The <a title="Main.as on Assembla SVN" href="http://svn.assembla.com/svn/thecouch/trunk/src/thecouch/Main.as" target="_blank">Main class</a> shows you how to use them. If you want other methods or events, feel free to add them, or you can always ask me. I&#8217;d be delighted to expand this wrapper a little more.

The previous posts in this series (not all of them are still applicable, but will be updated shortly):

  * <a href="http://www.streamhead.com/create-fully-customizable-actionscript-30-youtube-player/" title="Fully Customizable AS3 YouTube Player" target="_blank">Getting a list of videos (and some project setup)</a>
  * <a href="http://www.streamhead.com/flash-developer-flashdisplaystagescalemode/" title="The Flash stage" target="_blank">A bit about how the Flash stage works and fullscreen</a>
  * <a href="http://www.streamhead.com/youtube-flash-video-flv-secret/" title="PHP proxy-ing around security contraints" target="_blank">Install a php script to get the video parameters</a>
  * <a href="http://www.streamhead.com/tying-youtube-services-pro-web-20-developer/" title="YouTube hacking" target="_blank">Getting the parameters for a video</a>
  * <a href="http://www.streamhead.com/lazy-actionscript-developers-stream-flash-video/" title="Playing FLV files in ActionScript 3" target="_blank">playing the video using Flash’s FLV player classes</a>

Next up, I&#8217;m going to remove the proprietary YouTube Data API calls with <a title="AS3-YouTube-Data-API" href="http://code.google.com/p/as3-youtube-data-api/" target="_blank">this project</a>.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->