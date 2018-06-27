---
id: 178
title: 'The Secret of Reading Mouse Input in Flash Sandy3D &#8211; part 2'
date: 2008-08-26T10:00:06+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=178
permalink: /the-secret-of-reading-mouse-input-in-flash-sandy3d-part-2/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/08/mouseinput_part2.png
dsq_thread_id:
  - "5437981"
amazon_post_template:
  - ""
image: /wp-content/uploads/2008/08/mouseinput_part2.png
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
This posts is a continuation of <a title="part 1 on how to read mouse input in Flash Sandy3D" href="http://www.streamhead.com/?p=173" target="_blank">the previous post</a> and goes into more detail on how to greatly speed up the 2D > 3D mapping by analyzing what actually happens. Usually I&#8217;d let Sandy3D do everything for me, but in this case, it turns out it is too slow and the calculation is not complicated at all.

What actually happens in part 1 is this:

  * We have a camera with a viewport of 300 by 300 pixels looking at (0,0,0)
  * There is a plane centered at (0,0,0) and perpendicular to the z-axis. So it faces us.
  * This means the plane will be projected perfectly onto the screen. As is shown in the following figure.

[<img class="alignnone size-full wp-image-195" title="2D to 3D mapping" src="http://www.streamhead.com/wp-content/uploads/2008/08/2dto3dmapping.png" alt="" width="277" height="218" srcset="http://www.streamhead.com/wp-content/uploads/2008/08/2dto3dmapping.png 461w, http://www.streamhead.com/wp-content/uploads/2008/08/2dto3dmapping-300x236.png 300w" sizes="(max-width: 277px) 100vw, 277px" />](http://www.streamhead.com/wp-content/uploads/2008/08/2dto3dmapping.png)

Because of this, it is really simple to calculate the mouse coordinate in the 3D space. The top left corner (0,0) maps to the &#8220;plane&#8221;-coordinate (-150, 150) and the bottom right corner (300,300) maps to (150,-150). The necessary calculation is easy and can be found in the event handler in the following code:

<pre lang="ActionScript">package  {

	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import sandy.core.Scene3D;
	import sandy.core.scenegraph.Camera3D;
	import sandy.core.scenegraph.Group;
	import sandy.core.scenegraph.Shape3D;
	import sandy.materials.Appearance;
	import sandy.materials.BitmapMaterial;
	import sandy.primitive.Plane3D;

	public class MappingOurown extends Sprite {

		[Embed(source = 'library/capoeira.jpg')]
		private var capoeira:Class;

		private var scene:Scene3D;
		private var camera:Camera3D;
		private var shape:Shape3D;
		private var dir:int = 1;

		public function MappingOurown()
		{
			camera = new Camera3D (300, 300);

			var root:Group = createScene();
			scene = new Scene3D("scene", this, camera, root);

			addEventListener (Event.ENTER_FRAME, enterFrameHandler);
			stage.addEventListener (MouseEvent.MOUSE_MOVE, stageMoveHandler);
		}

		private function createScene () : Group
		{
			var g:Group = new Group ('scene');
			shape = new Plane3D ('plane', 10, 15);
			shape.tilt = 45;

			shape.appearance = new Appearance (new BitmapMaterial (new capoeira ().bitmapData));

			g.addChild (shape);

			return g;
		}

		private function enterFrameHandler (event : Event) : void
		{
			if (shape.pan > 60) {
				dir = -1;
			} else if (shape.pan &lt; -60) {
				dir = 1;
			}
			shape.pan += dir*3;
			scene.render();
		}

		private function stageMoveHandler (event : MouseEvent) : void
		{
			var x:Number = event.localX - 145;
			var y:Number = -1 * (event.localY - 145);
			shape.x = x;
			shape.y = y;
		}
	}
}</pre>



Notes:

  * The dimensions of the Flash applet are put at 300 x 300. In FlashDevelop you can do this in the Project > Properties dialog.
  * The mouse move handler is attached to the stage, so it no longer receives 3D events, but just the ordinary MouseEvent.
  * I've left out the "camera.z = -300;" statement, because -300 is the default z-value for the camera in Sandy 3D
  * I have replaced the "*" import statements with specific classes. This is not required, but it does have the advantage to clearly show which dependencies exist in your program.
  * You'll notice that the 3D object does not follow the mouse exactly. I could just hide the cursor and be done with it (few people will notice). But it is nagging me and I have no idea why that is. I'll ask around and see if any one can explain this to me.

And that's really all there is to it. This really only works because the playing field is exactly the same as the screen. You might be tempted to rotate the field for cool perspective effects, but as soon as you do that, the calculation becomes more complicated.

Now it's about time to introduce some interesting 3D objects and get some real action going. But that's for a next post.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->