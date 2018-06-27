---
id: 173
title: 'The Secret of Reading Mouse Input in Flash Sandy3D &#8211; part 1'
date: 2008-08-19T10:00:50+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=173
permalink: /the-secret-of-reading-mouse-input-in-flash-sandy3d-part-1/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/08/mouseinput_part1.png
dsq_thread_id:
  - "5437976"
amazon_post_template:
  - ""
image: /wp-content/uploads/2008/08/mouseinput_part1.png
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
Previously, I&#8217;ve shown you a <a title="Sandy3D and FlashDevelop" href="http://www.streamhead.com/?p=74" target="_blank">few random</a> <a title="images in FlashDevelop" href="http://www.streamhead.com/?p=98" target="_blank">Flash tidbits</a>. The ultimate goal is to create a small arcade action game in a 3 dimensions. I&#8217;m taking this opportunity to learn <a title="Flash Sandy 3D engine" href="http://www.flashsandy.org/" target="_blank">Sandy 3D</a>, one of the better Flash 3D engines. In this two part feature, I will be going into the details of how to get mouse information into a 3D world.

<img class="alignleft size-full wp-image-184" title="2d to 3d mapping" src="http://www.streamhead.com/wp-content/uploads/2008/08/2dto3d.png" alt="" width="336" height="255" srcset="http://www.streamhead.com/wp-content/uploads/2008/08/2dto3d.png 336w, http://www.streamhead.com/wp-content/uploads/2008/08/2dto3d-300x227.png 300w" sizes="(max-width: 336px) 100vw, 336px" />Although this might seem easy, the underlying problem is that the mouse position is in 2 dimensions: an X and Y coordinate. Your screen is flat after all. However, the game world has 3 dimensions. So how do we map the cursor 2D position on the screen onto a 3D position in the game world?

In this post and the next, I&#8217;ll show you two ways to get this working. First I&#8217;ll show you the solution, which I think is &#8220;the best&#8221; from a theoretical perspective. Sadly it is not workable in real life, as it is too slow. In a second post, I&#8217;ll present a possibility which is sort-of hacky, because it works perfectly in this example, but if you want a slightly different game, it probably won&#8217;t help you (or you&#8217;ll have to do some Maths yourself, which could be complicated, depending on the case in question).

# The Right Way

The idea is to have the game playable on a 2D plane, but use 3D objects and effects to make it more interesting. So all objects and user interaction will happen only in 2 dimensions. It is not too well documented (there are <a href="http://www.flashsandy.org/tutorials/3.0/sandy_cs3_tut18" target="_blank">a bunch of tutorials</a> on the topic), but Sandy3D makes this very easy for you. In Sandy, you can <a title="Node addEventListener" href="http://sandy.googlecode.com/svn/trunk/sandy/as3/branches/3.0.2/docs/sandy/core/scenegraph/Node.html#addEventListener()" target="_blank">add listeners to any 3D object</a>. Basically any Flash event is supported and on top of that, it will return a Shape3DEvent, which contains the 3D position of the cursor on the object.

So easy enough, all I have to do is draw a &#8220;interactivity&#8221; plane in which I want the objects to move and attach a mouse listener. You&#8217;ll probably recognize a lot of this code:

<pre lang="ActionScript">package
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import sandy.core.scenegraph.*;
	import sandy.core.*;
	import sandy.events.*;
	import sandy.materials.attributes.*;
	import sandy.materials.*;
	import sandy.primitive.*;

	public class Demo1 extends Sprite
	{
		[Embed(source = 'library/capoeira.jpg')]
		private var capoeira:Class;

		private var scene:Scene3D;
		private var camera:Camera3D;
		private var shape:Shape3D;
		private var groundPlane:Shape3D;
		private var dir:int = 1;
		public function Demo1 ()
		{
			camera = new Camera3D (300, 300);
			camera.z = -300;

			var root:Group = createScene();
			scene = new Scene3D("scene", this, camera, root);

			addEventListener (Event.ENTER_FRAME, enterFrameHandler);
		}

		private function createScene () : Group
		{
			var g:Group = new Group ('scene');
			shape = new Plane3D ('plane', 10, 15);
			shape.tilt = 45;

			groundPlane = new Plane3D("ground", 300, 300, 10, 10);
			groundPlane.enableEvents = true;
			groundPlane.addEventListener( MouseEvent.MOUSE_MOVE, moveHandler);

			shape.appearance = new Appearance (new BitmapMaterial (new capoeira ().bitmapData));

			g.addChild (shape);
			g.addChild (groundPlane);

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

		private function moveHandler (event : Shape3DEvent) : void
		{
			shape.x = event.point.x;
			shape.y = event.point.y;
		}
	}
}</pre>



A few notes:

  * I purposely kept the plane to which the event handler is connected visible, so that it would be clear what happened. In any real game this would be invisible.
  * On my machine, the animated object correctly follows the mouse, but it is very laggy. In fact, if this was an arcade game, it would be unplayable. Sometimes it doesn't even update at all. If you have a faster computer, you might not notice it that much. But if you'd start adding other objects, chances are high you'd run into the problem at some point.
  * An event handler attached to a Sandy object returns a Shape3DEvent. This contains many useful properties. Such as the "point" that we use to extra the cursor location on the plane. No Math needed.
  * Compared to the previous Sandy3D tutorials, I have replaced the (older) World3D with a (newer) Scene3D object. The Scene3D is preferable as it allows more flexibility. You can have multiple Scene3D objects in your application (for instance, if you want a picture-in-picture type of display, or if you want to switch between worlds)
  * Although this is a very very basic example, this event handling is very powerful. It will work on anything. Put a sphere in your scene and it will allow you to follow the cursor on the sphere. However, the downside of all this power is that it does not perform too well.
  * Make sure to take a look at <a title="Sandy 3D tutorials" href="http://www.flashsandy.org/tutorials/3.0" target="_blank">the "User interaction" tutorials on the Sandy site</a> to grasp all the possibilities in Sandy 3D.

Next week I'll show you what actually happens behind the scene of the position calculation. In case of this particular plane, this turns out to be deceptively simple. In fact, we can do it ourselves and save many CPU cycles.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->