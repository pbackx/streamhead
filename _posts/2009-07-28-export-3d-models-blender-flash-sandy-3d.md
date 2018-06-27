---
id: 1438
title: Exporting Models From Blender to Flash Sandy 3D, Experiments in 3D
date: 2009-07-28T10:00:28+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1438
permalink: /export-3d-models-blender-flash-sandy-3d/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/07/a-wing.png
dsq_thread_id:
  - "27152945"
categories:
  - Flash and ActionScript
---
Last week, reader _rafbaf_ asked how to use Blender models in Sandy 3D. There are a few options, for instance Sandy 3D can import the <a title="COLLADA - Wikipedia" href="http://en.wikipedia.org/wiki/COLLADA" target="_blank">Collada</a> format that Blender exports. But there is also an easier way. <a title="Export your Blender objects straight to Away3D, Papervision3D and Sandy" href="http://www.rozengain.com/blog/2008/01/02/export-your-blender-objects-straight-to-away3d-papervision3d-and-sandy/" target="_blank">A Python script for Blender allows you to export models straight to ActionScript code</a>. However, as you will see in this post, it&#8217;s not as straightforward as it seems.

<a title="example project: importing Blender models in Sandy 3D" href="http://www.streamhead.com/wp-content/uploads/2009/07/BlenderAndSandy.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />Example FlashDevelop project.</a>

There&#8217;s a reason this post is titled &#8220;experiments&#8221;. It is actually an unfinished work, but I wanted to give you a look at what I&#8217;ve already been able to create. This is how far I got for now:



  1. First, I got an A-Wing from <a title="blendermodels" href="http://www.blendermodels.org/models/sci_fi/" target="_blank">the blendermodels archive</a>. Before I got the first render result shown in the picture above, I had to fix the normals of most of the meshes in there (in Blender: go into edit mode, select vertices and ctrl-n)
  2. Next, get the export script from <a title="Export your Blender objects straight to Away3D, Papervision3D and Sandy" href="http://www.rozengain.com/blog/2008/01/02/export-your-blender-objects-straight-to-away3d-papervision3d-and-sandy/" target="_blank">Dennis&#8217;s page</a> and install it. Take care to get the correct directory, it&#8217;s not that easy to find. If you have one of the latest versions of Blender, you should look in your user folder. For Windows that&#8217;s &#8220;C:Documents and Settings<username>Application DataBlender FoundationBlender.blenderscripts&#8221;.
  3. If you haven&#8217;t already done so, you also need to have <a title="Python Programming Language" href="http://www.python.org/" target="_blank">Python</a> installed. Python is necessary to execute the script.
  4. Once you got this out of the way, you will need to restart Blender. Check the file > export menu and verify that the ActionScript option is available. If it&#8217;s not, you probably placed the AS3Export.py file in the wrong directory.
  5. Select the object you want to export and click the export to ActionScript menu item. It&#8217;s probably a good idea to enter a package name, as this will keep your code cleaner.

Now you should have one or more .as files: one for every mesh and texture in your model. This model doesn&#8217;t come with textures, so there are none.

Next we are going to use those files in a FlashDevelop project. The first step is to create a new project in FlashDevelop and put the Sandy 3D library inside the src folder. <a title="Sandy 3D Tutorial: Getting Started" href="http://www.streamhead.com/sandy-3d-tutorial/" target="_blank">Like described in previous blog posts</a>.

Now inside the src directory, you should create a directory with the same name as the package you specified in step 5 above. If you forgot the package name or are not sure, you can open one of the files that was created and check the first line.

That&#8217;s pretty much it: add the meshes as Shape3D objects to your scene, just like you would add a cube or other shape:

<pre lang="actionscript">scene.root.addChild( new Mesh() );</pre>

(you might want to add an appearance too)

You&#8217;ll notice I&#8217;m skipping a few steps here, but they are all very basic. If you download the example project and read through <a title="Sandy 3D Tutorial: Getting Started" href="http://www.streamhead.com/sandy-3d-tutorial/" target="_blank">my previous</a> <a title="Tutorial - getting started with Sandy 3D and FlashDevelop" href="http://www.streamhead.com/tutorial-getting-started-with-sandy-3d-and-flashdevelop/" target="_blank">blog posts</a>, everything should be clear (feel free to comment if it isn&#8217;t).

You&#8217;ll notice a few issues/problems (correct me if I&#8217;m wrong):

  * The 3D object I choose, consists of several meshes. Each with their own texture (material in Sandy3D terminology). The export plugin doesn&#8217;t really help you on this point. You need to create every mesh and add them individually to the scene.
  * There seems to be an issue with the normal calculations. I did correct them in Blender as you can see in the small rendering at the top of my post, but still there seem to be missing triangles in the Sandy 3D version.
  * It looks like there is an issue with a bounding box or <a title="Sandy 3D tutorial on performance" href="http://www.flashsandy.org/tutorials/3.0/sandy_cs3_tut05" target="_blank">face culling</a>. I still need to investigate this thoroughly.

To be continued&#8230;

<a title="example project: importing Blender models in Sandy 3D" href="http://www.streamhead.com/wp-content/uploads/2009/07/BlenderAndSandy.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />Example FlashDevelop project.</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->