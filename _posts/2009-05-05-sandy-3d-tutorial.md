---
id: 1278
title: 'Sandy 3D Tutorial: Getting Started with Sandy and FlashDevelop'
date: 2009-05-05T10:00:04+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1278
permalink: /sandy-3d-tutorial/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/04/sandy3d_flashdevelop.png
dsq_thread_id:
  - "17363164"
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
Over the last year or two, developing 3D applications in Flash has become increasingly feasible, for almost any ActionScript developers. A number of open source 3D engines, like <a title="Sandy 3D engine for AS3 & AS2" href="http://www.flashsandy.org/" target="_blank">Sandy 3D</a>, have popped up. Combined with the incredible <a title="FlashDevelop.org" href="http://www.flashdevelop.org/" target="_blank">FlashDevelop</a>, any one can get started, right away. However, because FlashDevelop does not have the authoring tools of Adobe&#8217;s Flash tools, you need to know a few differences that you won&#8217;t find in many tutorials, but I will explain them in this post.

This is a refreshed version of <a title="Tutorial - getting started with Sandy 3D and FlashDevelop" href="http://www.streamhead.com/tutorial-getting-started-with-sandy-3d-and-flashdevelop/" target="_blank">my previous tutorial</a>, where I explained the important differences you need to know to get started with FlashDevelop and Sandy 3D. I won&#8217;t go into setting up FlashDevelop, all details mentioned in the previous post are still valid.

But the Sandy 3D Engine has changed slightly (for the better, mind you). I&#8217;ll point out what&#8217;s new and give some additional examples. But first, lets look at the result:



The code consists of 4 main parts, I&#8217;ve split them up, but if you want, you can go right ahead and download the entire FlashDevelop workspace:

<a title="FlashDevelop example project with Sandy3D" href="http://www.streamhead.com/wp-content/uploads/2009/05/boxes.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />download the full source and FlashDevelop project</a>

## 1. Using bitmaps

I&#8217;ve gone over this a few times, but it bears repeating as this is something you won&#8217;t use in CS3. In FlashDevelop, you add a bitmap in the lib directory. With this done, you put an embed tag in your code (or double click, FD can usually do this for you) and on the next line you put the class name you want to assign to this embedded resource. As a final step, you need to instantiate the object.

It sounds much more complicated then it is, just look at the code:

<pre lang="actionscript">[Embed(source = '../../../../lib/aqua.png')]
private var aquaClass:Class;
private var aquaBitmap:Bitmap = new aquaClass();</pre>

## 2. Creating and texturing the 3D objects

With the bitmaps imported, we can use them to texture objects. This is done by setting the objects appearance. The appearance has a few options, but for now, we&#8217;ll only set one material on it. The material is the object that actually contains the texture.

For instance, the background image when you move over the cube is a Plane3D object on which we set an appearance that consists of a BitmapMaterial:

<pre lang="actionscript">plane = new Plane3D( "thePlane", 200, 200);
material = new BitmapMaterial(beamsBitmap.bitmapData);
material.lightingEnable = true;
plane.appearance = new Appearance(material);</pre>

More complicated objects can contain multiple surfaces. If you want to set them all alike, just use the code above, but you can also address them individually. You use the &#8220;aPolygons&#8221; collection for that. Depending on the object and the parameters you choose, you might need to experiment a little to find the correct polygons.

For instance, this code sets the front and back side of the box in the example:

<pre lang="actionscript">var material:Material = new BitmapMaterial(logoBitmap.bitmapData);
material.lightingEnable = true;
var app:Appearance = new Appearance( material );
var i:int;
for (i = 0; i &lt; 4; i++ )
    myBox.aPolygons[i].appearance = app;</pre>

## 3. Listening to events

While the way you handle events hasn&#8217;t changed since previous versions of Sandy, the MOUSE_MOVE event was removed. It is no longer handled, probably because of performance reasons, but I&#8217;m not entirely clear on the reasons.

The official tutorials also now suggest to put the event handling on the container, this is part of your object that is actually displayed. If you can, I would suggest to use this, because it&#8217;s probably a lot quicker.

There are cases where you might like to obtain the Shape3DEvent. Take a look at <a title="Tutorial 18 - Sandy events" href="http://www.flashsandy.org/tutorials/3.0/sandy_cs3_tut18" target="_blank">the tutorial on the Sandy site</a> to decide if you&#8217;d need that. But to reiterate, the Sandy event system no longer supports the MOUSE_MOVE event.

In the example, the event listener for the mouse over event looks like this:

<pre lang="actionscript">    myBox.container.addEventListener(MouseEvent.MOUSE_OVER, overHandler);
private function overHandler(event:MouseEvent):void {
    if(!zoomedIn)
        g.addChild(plane);
}</pre>

## 4. Setting up the scene and camera

New in Sandy3D (although it&#8217;s not that new any longer) is the removal of World3D. World3D was a singleton class, which meant that you could have only one in your program. It has now been replaced by Scene3D, of which you can create and render multiple in your program.

So if you want, you can have different scenes or different cameras in your program. Cool, but don&#8217;t overdo it, keep in mind that every scene you add will also add to the processing power required.

Setting up the camera is exactly the same as before:

<pre lang="actionscript">private function init(e:Event = null):void
{
    removeEventListener(Event.ADDED_TO_STAGE, init);
    // entry point
    camera = new Camera3D( 300, 300 );
    camera.x = 0;
    camera.y = 50;
    camera.z = -200;
    camera.lookAt(0,0,0);

    var root:Group = createScene();

    scene = new Scene3D( "scene", this, camera, root );

    addEventListener( Event.ENTER_FRAME, enterFrameHandler );
}</pre>

I haven&#8217;t discussed the tweening used to move the cube in the program. If you&#8217;re interested, please let me know and I&#8217;ll write another blogpost. Otherwise, you now have all parts to get started with 3D development in FlashDevelop.

Good luck and don&#8217;t forget to show those results!

<a title="FlashDevelop example project with Sandy3D" href="http://www.streamhead.com/wp-content/uploads/2009/05/boxes.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />download the full source and FlashDevelop project</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->