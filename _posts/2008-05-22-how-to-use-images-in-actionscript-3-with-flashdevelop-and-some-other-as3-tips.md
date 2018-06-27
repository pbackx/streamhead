---
id: 98
title: How to use images in ActionScript 3 with FlashDevelop (and some other AS3 tips)
date: 2008-05-22T12:53:30+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=98
permalink: /how-to-use-images-in-actionscript-3-with-flashdevelop-and-some-other-as3-tips/
dsq_thread_id:
  - "5437893"
amazon_post_template:
  - ""
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
<p class="update">
  <strong>update</strong>: I&#8217;ve created <a title="Embedding Bitmap Images in ActionScript 3 with FlashDevelop" href="http://www.streamhead.com/embedding-images/">a new and updated tutorial on embedding images in FlashDevelop</a>. I suggest you check out that tutorial instead of the one below. The new tutorial is cleaner, clearer and more up-to-date.
</p>

One of the main bumps you will run into when <a title="previous tutorial on Sandy3D and FlashDevelop" href="http://www.streamhead.com/?p=74" target="_blank">coding Sandy3D</a>, or basically any kind of graphical applet is loading resources, such as images. If you are working inside Adobe&#8217;s Flash environment, this all comes pretty naturally. But open source tools such as <a title="FlashDevelop - open source Flash development" href="http://www.flashdevelop.org/community/" target="_blank">FlashDevelop</a> do not have a graphical component, so you have to create your multimedia assets in other applications (<a title="Paint.NET - free software for digital photo editing" href="http://www.getpaint.net/" target="_blank">Paint.NET is nice</a>).

Before you get started, have a look at <a title="AS3 MovieClip vs Sprite" href="http://kanuwadhwa.wordpress.com/2007/09/10/76/" target="_blank">this MovieClip vs Sprite comparison</a> and <a title="AS3 getting started tutorial" href="http://www.senocular.com/flash/tutorials/as3withmxmlc/" target="_blank">this tutorial on starting with AS3</a> to understand why our base class extends Sprite and how events are handled. And if you want to know where all this is going, the idea is to recreate <a title="Flash game tutorial" href="http://www.emanueleferonato.com/2008/03/27/create-a-flash-game-like-bloons-tutorial/" target="_blank">something similar to this</a> in ActionScript 3 and FlashDevelop and then afterwards add some 3D goodness to it (3D objects, maybe 3D camera).

One important thing to know about event handlers is: don&#8217;t attach them to your main Sprite. This won&#8217;t work:

<pre lang="ActionScript">public class Test extends Sprite {
  public function Test() {
    graphics.lineStyle(1);
    graphics.beginFill(0xFF8000);
    graphics.drawCircle(50, 50, 10);
    addEventListener(MouseEvent.MOUSE_DOWN, down);
  }
  private function down(evt:MouseEvent):void {
    trace("down");
  }
}</pre>

My intuition was that it would attach mouse down events to the circle. But it does not. In most cases you would want to capture the whole sprite anyway. The solution is to add your listeners to the &#8220;_stage_&#8221; object. See the the examples below for a demonstration of this.

In Flash, images come in 2 types. Vector drawings or bitmaps. Pretty much all graphics you see on the Internet are bitmaps, every pixel in the bitmap is defined. A program such as <a title="Paint.NET - free software for digital photo editing" href="http://www.getpaint.net/" target="_blank">Paint.NET</a> will create those for you. Vector images are a different beast. Those images define the lines and forms that are used. In the example above, a circle is drawn, not a collection of points. The advantage is that the image quality will be a lot higher and it is possible to zoom in on the Flash applet without loosing quality. But (there always is a but) you can only draw those in the Adobe Flash editor. You can use existing .fla files with vector drawings in them, but you can&#8217;t make your own, unless you pay for the program. Either that or you would have to handcode everything. A future post will probably deal with that.

But this post deals with bitmaps. We will start from the following simple mouse-follow applet and replace the circle with a bitmap:

<pre lang="ActionScript">package  {
  import flash.display.Sprite;
  import flash.events.Event;
  import flash.ui.Mouse;

  public class Test extends Sprite {

    private var circle:Sprite = new Sprite();

    public function Test() {
      Mouse.hide();

      circle.graphics.lineStyle(1);
      circle.graphics.beginFill(0xFF8000);
      circle.graphics.drawCircle(0, 0, 10);
      addChild(circle);

      stage.addEventListener(Event.ENTER_FRAME, mouseMove);
    }
    private function mouseMove(evt:Event):void {
      circle.x = mouseX;
      circle.y = mouseY;
    }
  }
}</pre>

This is the result:



I like to store all my resources in a separate directory, called &#8220;_library_&#8220;. It&#8217;s not a the &#8220;real&#8221; library that you have in the Flash IDE, but it&#8217;s close enough. I&#8217;m using this crosshair bitmap:

[<img class="alignnone size-thumbnail wp-image-113" title="crosshair" src="http://www.streamhead.com/wp-content/uploads/2008/05/crosshair-150x150.png" alt="" width="78" height="78" srcset="http://www.streamhead.com/wp-content/uploads/2008/05/crosshair-150x150.png 150w, http://www.streamhead.com/wp-content/uploads/2008/05/crosshair.png 255w" sizes="(max-width: 78px) 100vw, 78px" />](http://www.streamhead.com/wp-content/uploads/2008/05/crosshair.png)

Once we have an image, it&#8217;s time to embed it. ActionScript 3 has an &#8220;Embed&#8221; tag that will allow you to put images in an applet. See <a title="Embedding resources with AS3" href="http://www.bit-101.com/blog/?p=853" target="_blank">this link</a> for the complete explanation. Basically, you define a private Class variable, put the cursor just above it and double click on your image. FlashDevelop will automatically insert the correct &#8220;Embed&#8221; tag in your code. A little tweaking to get the correct size and there you are:

<pre lang="ActionScript">package  {

	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.ui.Mouse;

	public class Test extends Sprite {

		[Embed(source='library/crosshair.png')]
		private var crosshairClass:Class;
		private var crosshair:Bitmap = new crosshairClass ();

		public function Test() {
			Mouse.hide();

			crosshair.height = 30;
			crosshair.width = 30;
			addChild(crosshair);

			stage.addEventListener(Event.ENTER_FRAME, mouseMove);
		}

		private function mouseMove(evt:Event):void {
			crosshair.x = mouseX - 15;
			crosshair.y = mouseY - 15;
		}

	}

}</pre>



As you will notice, the quality of the scaled down image is not that good, but using a larger sprite allows you to zoom in with little quality loss. Next time, I&#8217;ll show you how to fix this.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->