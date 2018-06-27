---
id: 74
title: 'Tutorial &#8211; getting started with Sandy 3D and FlashDevelop'
date: 2008-04-08T02:27:46+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=74
permalink: /tutorial-getting-started-with-sandy-3d-and-flashdevelop/
dsq_thread_id:
  - "5437852"
amazon_post_template:
  - ""
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
3D for the web, it has been coming to you ever since virtual reality was the mot-du-jour and <a href="http://en.wikipedia.org/wiki/VRML" target="_blank">VRML</a> the format to support, but it&#8217;s still not there yet. The latest craze now are Flash 3D engines. There are three worth mentioning: [Papervision3D](http://papervision3d.org/), [Away3D](http://www.away3d.com/) and, the one I&#8217;ll be talking about here, [Sandy3D](http://www.flashsandy.org/).

Flash development (or more specificically Action Script) is all fine and dandy, but it does require an investment in some software products. If you&#8217;d go the route of least resistance, you need [Adobe Creative Suite 3](http://www.adobe.com/products/creativesuite/) ($999 for the web standard edition) and some 3D software, [Autodesk 3ds Max](http://usa.autodesk.com/adsk/servlet/index?id=5659302&siteID=123112) ($3495 for 2009 edition) is the most widely supported. I don&#8217;t know about you, but as a hobbiest that leaves me only 2 options. Pirate the software, or go look in the free and open source community.

Luckely there are a few options for creating Flash and 3D. This post is about the Flash part. [FlashDevelop](http://osflash.org/flashdevelop) is an open source development environment for Flash Actionscript and integrates seamlessly with the Flex SDK (free from Adobe). As you will see in this post, it is missing the designer features that the CS3 tools have (vector graphics, timeline editing), but as far as Actionscript editing goes, it&#8217;s on par with anything out there and better than most.

As an introduction, here is a short tutorial on how to get the [Sandy3D getting started video](http://www.flashsandy.org/tutorials/3.0/video_getting_started) example working on FlashDevelop.

**_First set up your environment_**

  1. If you want to use the latest release of Sandy3D, as we will do in this tutorial, get and install [TortoiseSVN](http://tortoisesvn.net/).
  2. Get FlashDevelop ([currently 3.0.0 beta 6](http://www.flashdevelop.org/community/viewtopic.php?t=2574)) and the [Adobe Flex SDK](http://opensource.adobe.com/wiki/display/flexsdk/Download+Flex+3). Install both.
  3. Start up FlashDevelop and open **Tools > Program Settings&#8230;** Click on **AS3Context** on the left and fill in the **Flex SDK location**:

![flash develop setup](http://www.streamhead.com/wp-content/uploads/2008/04/fdsetup.png)

_**Lets get started**_

  1. Watch the [getting started video](http://www.flashsandy.org/tutorials/3.0/video_getting_started) and follow along.
  2. Create a project directory, eg &#8220;New Sandy Project&#8221;.
  3. Inside it, create a &#8220;**sandy**&#8221; directory and use TortoiseSVN to check out the latest Sandy3D release, as shown in the video. Use [the current release URL here](http://sandy.googlecode.com/svn/trunk/sandy/as3/branches/3.0.2/src/sandy) at your own risk (best to follow the video and find the latest release yourself)
  4. In your project folder, create a **Demo1.as** file.
  5. No need to create the <span style="text-decoration: line-through;">Demo1.fla</span> file as this is not used by FlashDevelop.
  6. Unlike with CS3, you will need to manage your resource library (images, etc) by hand. So create a &#8220;**library**&#8221; directory inside your project folder.
  7. Search two images on the Net and place them in the library directory. One will be used for the background, one will be used as a texture for the plane object we are going to draw.
  8. Open FlashDevelop and start a new Project: **Project > New Project..**.
  9. Choose an empty ActionScript3 project. Enter any project name you like. In the location field browse to the project directory you created. Leave the package name empty and click OK.
 10. Select an output file name in **Project > Properties&#8230;**. For instance &#8220;New Sandy Project.swf&#8221;.
 11. In the Project view, open the library directory and right click on both images and select &#8220;**Add to library**&#8220;.
 12. Again in the Project view, right click on Demo1.as and select &#8220;**Always compile**&#8220;. Double click on the file to open it. You should have a view similar to this one:

![fdreadytogo.png](http://www.streamhead.com/wp-content/uploads/2008/04/fdreadytogo.png)

_**Enter the code**_

This one is the bulk of the work. In the Demo1.as view, type the code for the example:

<pre>package
{
	import flash.display.Sprite;
	import sandy.core.scenegraph.Camera3D;
	import sandy.core.scenegraph.Group;
	import sandy.core.scenegraph.Shape3D;
	import sandy.core.World3D;
	import sandy.materials.Appearance;
	import sandy.materials.WireFrameMaterial;
	import sandy.primitive.Plane3D;

	public class Demo1 extends Sprite
	{
		private var world:World3D;

		public function Demo1()
		{
			world = World3D.getInstance ();
			world.container = this;

			world.camera = new Camera3D (this.width, this.height);

			var scene:Group = new Group ('scene');
			var shape:Shape3D = new Plane3D ('plane', 100, 100, 10, 10);
			shape.appearance = new Appearance (new WireFrameMaterial ());

			scene.addChild (shape);
			scene.addChild (world.camera);
			world.root = scene;
		}
	}
}</pre>

Hit ctrl-enter or select the little play button (test movie). Everything should compile and run fine, but you will see an empty movie. FlashDevelop automatically imports classes for you, so if you typed in everything by hand, like in the video, you could skip the step where you locate the missing import statements.

There are two reasons the code is not displaying anything:

**_1._** The &#8220;this&#8221; object does not have a width and height. In the demo video a vector image is attached as background. I don&#8217;t think this is possible with FlashDevelop only (let me know if it is), so my option is to get a bitmap from the net &#8220;gradient.jpg&#8221; in this case and use that one. We can do this by embedding an image. Just before the &#8220;private var world:World3D;&#8221; line, add this:

<pre>[Embed(source = 'library/gradient.jpg')]
private var gradient:Class;</pre>

And now add this to the main sprite class. Just before &#8220;world = &#8230;&#8221; add

<pre>this.addChild (new gradient ());</pre>

Run again and you should already see your background.

_**2.**_ The second issue is that the camera is not pointed in the right direction. Add the code as instructed in the video. Your entire program should now be:

<pre>package
{
	import flash.display.Sprite;
	import sandy.core.scenegraph.Camera3D;
	import sandy.core.scenegraph.Group;
	import sandy.core.scenegraph.Shape3D;
	import sandy.core.World3D;
	import sandy.materials.Appearance;
	import sandy.materials.WireFrameMaterial;
	import sandy.primitive.Plane3D;

	public class Demo1 extends Sprite
	{
		[Embed(source = 'library/gradient.jpg')]
		private var gradient:Class;

		private var world:World3D;

		public function Demo1()
		{
			this.addChild (new gradient ());

			world = World3D.getInstance ();
			world.container = this;

			world.camera = new Camera3D (this.width, this.height);

			var scene:Group = new Group ('scene');
			var shape:Shape3D = new Plane3D ('plane', 100, 100, 10, 10);
			shape.appearance = new Appearance (new WireFrameMaterial ());

			scene.addChild (shape);
			scene.addChild (world.camera);
			world.root = scene;

			world.camera.setPosition ( -100, -100, -100);
			world.camera.lookAt (0, 0, 0);
			world.render ();
		}
	}
}</pre>

Run the movie again and the plane should be visible.

There&#8217;s a little more in the video than that, but that&#8217;s for another post. At least you should already be well on your way to running all the other Sandy3D tutorials.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->