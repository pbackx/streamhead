---
id: 149
title: 'Vector vs Bitmap side-by-side &#8211; SVG &#038; PNG in Flash'
date: 2008-07-04T10:00:34+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=149
permalink: /vector-vs-bitmap-side-by-side-svg-png-in-flash/
dsq_thread_id:
  - "5437931"
amazon_post_template:
  - ""
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
Looking back at <a title="previous post on vector graphics in Flash" href="http://www.streamhead.com/?p=136" target="_blank">my previous post and the comments</a>, I don&#8217;t think the vector versus bitmap comparison was very clear, so I tried to show it differently with the applet above. In the meantime I also got some hands-on time with <a title="Flash Matrix API" href="http://livedocs.adobe.com/flex/3/langref/flash/geom/Matrix.html" target="_blank">matrix transformations in Flash</a>. It&#8217;s not really needed, but if you&#8217;re interested, you can do some reading up on <a title="matrix math" href="http://en.wikipedia.org/wiki/Transformation_matrix" target="_blank">matrix transformations on Wikipedia</a> and many other sites.
  
<!--more-->


  
Every <a title="AS3 DisplayObject" href="http://livedocs.adobe.com/flex/3/langref/flash/display/DisplayObject.html" target="_blank">DisplayObject</a> (Sprite and others) in ActionScript has a transform object associated with it. This can completely transform the object, among others you can manipulate the position and size with the <a title="AS3 Matrix" href="http://livedocs.adobe.com/flex/3/langref/flash/geom/Matrix.html" target="_blank">Matrix</a> object. You could directly change that matrix with the maths you&#8217;ve just learned, or you can use a number of handy shortcut functions. In the example I use:

  * **rotate**: this will rotate the object around the (0,0) point. If you are drawing on the main stage, this point is located in the upper left corner. This means that if you want to rotate something around its center, it has to be located at (0,0). That is why we need to ..
  * **translate**: this moves the object around the stage. You can actually define a coordinate system for every individual object to avoid having to translate it. This is possible if you place your sprite inside another sprite. To keep things simple I haven&#8217;t done this here, I might to it sometime later, but if you want to try it out, <a title="coorindate system in Flash" href="http://www.lukamaras.com/tutorials/actionscript/flash-coordinate-system-explained.html" target="_blank">here are two</a> <a title="Flash Solar System" href="http://www.flashandmath.com/intermediate/children/index.html" target="_blank">helpful articles</a>.
  * **scale**: allows you to scale the image in both directions.

And here is the full source code:

<pre lang="ActionScript">package  {

	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Matrix;
	import flash.ui.Mouse;

	public class Test extends Sprite {

		[Embed(source = 'library/starsmall.png')]
		private var starPNGClass:Class;
		private var starPNG:Bitmap = new starPNGClass ();

		[Embed(source='library/star.svg')]
		private var starSVGClass:Class;
		private var starSVG:Sprite = new starSVGClass ();

		private var scaleDir:int = +1;
		private var scaleCount:int = 0;

		public function Test() {
			trace("started");

			starSVG.height = 30;
			starSVG.width = 30;
			starSVG.x = 150-15;
			starSVG.y = 100 - 15;
			addChild(starSVG);

			starPNG.height = 300;
			starPNG.width = 300;
			starPNG.x = 50 - 150;
			starPNG.y = 100 - 150;
			addChild(starPNG);

			stage.addEventListener(Event.ENTER_FRAME, mouseMove);
			stage.addEventListener(MouseEvent.CLICK, click);
		}

		private function mouseMove(evt:Event):void {
			var starSVGMatrix:Matrix = starSVG.transform.matrix;
			starSVGMatrix.translate( -150, -100);
			starSVGMatrix.rotate(.02);
			starSVGMatrix.scale(1+scaleDir*.02, 1+scaleDir*.02);
			starSVGMatrix.translate( 150, 100);
			starSVG.transform.matrix = starSVGMatrix;

			var starPNGMatrix:Matrix = starPNG.transform.matrix;
			starPNGMatrix.translate( -50, -100);
			starPNGMatrix.rotate(.02);
			starPNGMatrix.scale(1+scaleDir*-.02, 1+scaleDir*-.02);
			starPNGMatrix.translate( 50, 100);
			starPNG.transform.matrix = starPNGMatrix;

			if (scaleCount++ &gt; 100) {
				scaleCount = 0;
				scaleDir *= -1;
			}
		}

		private function click(evt:MouseEvent):void {
			trace("clicked @ " + evt.stageX + "," + evt.stageY);
		}

	}

}</pre>

You will also need those <a title="bitmap star" href="http://www.streamhead.com/wp-content/uploads/2008/06/starsmall.png" target="_blank">two</a> <a title="vector star" href="http://www.streamhead.com/wp-content/uploads/2008/06/star.svg" target="_blank">images</a> in your library directory (<a title="using resources in FlashDevelop" href="http://www.streamhead.com/?p=98" target="_blank">see previous posts</a>):

<img class="alignnone size-full wp-image-152" title="starsmall" src="http://www.streamhead.com/wp-content/uploads/2008/06/starsmall.png" alt="" width="80" height="83" /><img class="alignright size-full wp-image-153" title="star1" src="http://www.streamhead.com/wp-content/uploads/2008/06/star1.svg" alt="" />

And that should get you going. As you probably noticed, you&#8217;re going to need a lot of maths to do visual animations. And this is just the tip of the iceberg, 3D graphics are a little more complicated. That&#8217;s why there are libraries like Sandy3D to help you out. But that is something for a future post.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->