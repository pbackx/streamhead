---
id: 136
title: 'How to use vector graphics in FlashDevelop &#8211; SVG in Flash'
date: 2008-06-27T10:00:39+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=136
permalink: /how-to-use-vector-graphics-in-flashdevelop-svg-in-flash/
dsq_thread_id:
  - "5437922"
amazon_post_template:
  - ""
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
<a title="Vector Scope" href="http://www.flickr.com/photos/35236669@N00/2504327638/" target="_blank"><img src="http://farm3.static.flickr.com/2400/2504327638_2e9b11fb35.jpg" border="0" alt="Vector Scope" /></a>
  
<small><a title="Attribution-ShareAlike License" href="http://creativecommons.org/licenses/by-sa/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="Kichigai Mentat" href="http://www.flickr.com/photos/35236669@N00/2504327638/" target="_blank">Kichigai Mentat</a></small>

In <a title="images in FlashDevelop" href="http://www.streamhead.com/?p=98" target="_blank">my previous Flash post</a>, I already touched on the subject of a major reason why you might still prefer the expensive Adobe Flash IDE over FlashDevelop: it&#8217;s the integrated vector editor. Vector graphics give you the major advantage of begin scalable with little to no quality loss. Try to print out any graphic you see on the web and you will notice it&#8217;s blocky. Not so with vector based graphics. They are inherently easily scalable, in both directions, smaller and bigger.

Most of what you create in the Adobe Flash IDE, are vector graphics. Using bitmaps is not really encouraged, and with reason. If you looked closely at the two applets in the previous post, you might have noticed that the quality of the crosshair picture in the last one is not very good. That&#8217;s because it is based on a bitmap. The circle one however, looks perfect.

So if FlashDevelop doesn&#8217;t let you create vector graphics, how are you going to do it? It&#8217;s easy: use the <a title="Home improvement with InkScape" href="http://www.streamhead.com/?p=129" target="_blank">previously mentioned</a> Inkscape. It lets you create SVG graphics, Scalable Vector Graphics.  <a title="an SVG star" href="http://www.streamhead.com/wp-content/uploads/2008/06/star.svg" target="_blank">Like this one</a>. This is the bitmap representation (most browsers don&#8217;t natively support the format):

[<img class="alignnone size-full wp-image-138" title="star" src="http://www.streamhead.com/wp-content/uploads/2008/06/star.png" alt="" width="161" height="166" />](http://www.streamhead.com/wp-content/uploads/2008/06/star.png)

[<img class="alignnone size-medium wp-image-137" title="star" src="http://www.streamhead.com/wp-content/uploads/2008/06/star.svg" alt="" />](http://www.streamhead.com/wp-content/uploads/2008/06/star.svg)

Ones you got the SVG file, it&#8217;s really easy to embed it. Put it in the library directory and use the same type of embed code as you would do for bitmaps. Then change the type of the embedded object from Bitmap to Sprite. That&#8217;s it, you&#8217;re done. You should have this piece of code:

<pre lang="ActionScript">package  {

	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.ui.Mouse;

	public class Test extends Sprite {

		[Embed(source='library/star.svg')]
		private var crosshairClass:Class;
		private var crosshair:Sprite = new crosshairClass ();

		public function Test() {
			trace("started");
			Mouse.hide();

			crosshair.height = 30;
			crosshair.width = 30;
			crosshair.scaleX = .30;
			crosshair.scaleY = .30;
			addChild(crosshair);

			stage.addEventListener(Event.ENTER_FRAME, mouseMove);
			stage.addEventListener(MouseEvent.CLICK, click);
		}

		private function mouseMove(evt:Event):void {
			crosshair.x = mouseX - 15;
			crosshair.y = mouseY - 15;
		}

		private function click(evt:MouseEvent):void {
			trace("clicked @ " + evt.stageX + "," + evt.stageY);
		}

	}

}</pre>

And compiled, this is what it looks like:



That&#8217;s all dandy, but there are a few issues to keep in mind:

  * For some reason, it&#8217;s impossible in FlashDevelop to right click on your SVG and &#8220;add to library&#8221;. So you can&#8217;t double click to insert the embed tags automatically. But if you type it by hand, it works perfectly.
  * It appears that the gradient functionality is not working as it should. If you look at the bitmap, or open the SVG in Inkscape, you&#8217;ll see that I have added a gradient, but it does not show in Flash. I&#8217;ll have to look into that one day.
  * I would suggest that you change the document size in Inkscape to be as small as possible. Either that, or put object in top left corner. This will make sure that object is correctly positioned when you load it in your Flash applet.

To finish, here&#8217;s a 400% zoomed image of the same star, once as PNG and once SVG:

[<img class="alignleft size-full wp-image-140" title="Star bitmap 400% zoomed" src="http://www.streamhead.com/wp-content/uploads/2008/06/starbitmapzoomed.png" alt="" width="160" height="160" srcset="http://www.streamhead.com/wp-content/uploads/2008/06/starbitmapzoomed.png 160w, http://www.streamhead.com/wp-content/uploads/2008/06/starbitmapzoomed-150x150.png 150w" sizes="(max-width: 160px) 100vw, 160px" />](http://www.streamhead.com/wp-content/uploads/2008/06/starbitmapzoomed.png)[<img class="size-full wp-image-141" title="Star vector 400% zoomed" src="http://www.streamhead.com/wp-content/uploads/2008/06/starvectorzoomed.png" alt="" width="160" height="160" srcset="http://www.streamhead.com/wp-content/uploads/2008/06/starvectorzoomed.png 160w, http://www.streamhead.com/wp-content/uploads/2008/06/starvectorzoomed-150x150.png 150w" sizes="(max-width: 160px) 100vw, 160px" />](http://www.streamhead.com/wp-content/uploads/2008/06/starvectorzoomed.png)

You&#8217;ll see that the right image has a smooth edge, with properly applied <a title="anti-aliasing explained" href="http://en.wikipedia.org/wiki/Anti-aliasing" target="_blank">anti-aliasing</a>. The little bit of anti-aliasing you see on the left image, was created by Inkscape when I exported the bitmap. This effect might not be very profound for this little example, but if you are going to be zooming and rotating image a lot in your Flash applet, it will make a huge difference.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->