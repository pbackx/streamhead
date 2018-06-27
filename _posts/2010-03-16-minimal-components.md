---
id: 2069
title: ActionScript 3 Minimal Comps for Quick Prototyping
date: 2010-03-16T10:00:41+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2069
permalink: /minimal-components/
dsq_thread_id:
  - ""
image: /wp-content/uploads/2010/03/minimal_duck.png
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
Recently, <a title="About / Contact - BIT-101" href="http://www.bit-101.com/blog/?page_id=2" target="_blank">Keith Peters</a> has been putting overtime into his <a title="Minimal Comps" href="http://www.minimalcomps.com/" target="_blank">Minimal Comps</a> library. It&#8217;s an ActionScript 3 library that offers a large number of typical user interface components. Easily and quickly you can construct basic user interfaces in ActionScript. When Flex is a little too heavy, this is a really neat solution.

<!--more-->This is basically the most minimal minimal component application you&#8217;re going to see:

<pre lang="ActionScript">package 
{
	import com.bit101.components.PushButton;
	import flash.display.Sprite;
	import flash.events.Event;
	import org.flashdevelop.utils.FlashConnect

	public class Main extends Sprite
	{
		public function Main():void
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(e:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);

			new PushButton(this, 100, 100, "Click me", onBtnClick);
		}

		private function onBtnClick(e:Event):void
		{
			FlashConnect.trace("clicked");
		}
	}
}</pre>

Inspired by this <a title="Minimal tutorial 01" href="http://www.minimalcomps.com/tutorials/minimal_tutorial_01.html" target="_blank">minimal tutorial</a> and written for <a title="FlashDevelop" href="http://www.flashdevelop.org/" target="_blank">FlashDevelop</a> (remove the FlashConnect statements if you&#8217;re working in another editor).

BTW I wanted to give a demonstration where I integrated the YouTube data API, but it appears that none of the libraries are really up-to-date and/or well enough documented to get started in under 15 minutes. <a title="as3-youtube-data-api" href="http://code.google.com/p/as3-youtube-data-api/" target="_blank">This one comes closest</a>, but if you have a good suggestion, please let me know.

([image credit](http://www.flickr.com/photos/ahudson/2053348794/))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->