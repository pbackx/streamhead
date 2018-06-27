---
id: 2773
title: 'Tutorial: FlashDevelop and Papervision3D, the Basics'
date: 2010-11-05T10:00:44+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2773
permalink: /tutorial-flashdevelop-and-papervision3d-the-basics/
dsq_thread_id:
  - "167482310"
image: /wp-content/uploads/2010/11/FlashDevelop_Papervision3D_tutorial.png
categories:
  - Flash and ActionScript
---
It&#8217;s been a while since I <a title="Flash and ActionScript Game Engines" href="http://www.streamhead.com/flash-actionscript-game-engines/" target="_blank">indulged in my Flash and 3D hobby</a>. I&#8217;ve been a longtime Sandy 3D fan, but it was about time I tried the competition. This post gives a short overview of how to set up FlashDevelop to run your first <a title="Papervision3D" href="http://blog.papervision3d.org/" target="_blank">Papervision3D</a> application.

<!--more-->Before you get started, you&#8217;ll need a few essential tools:

  * I&#8217;ll use <a title="TortoiseSVN downloads" href="http://tortoisesvn.net/downloads" target="_blank">TortoiseSVN</a> (or any other SVN client) to get the latest version of Papervision3D. You can download a zip file of the current version, but setting this up once will make it a lot easier to follow all the latest development.
  * I like <a title="FlashDevelop" href="http://www.flashdevelop.org/wikidocs/index.php?title=Main_Page" target="_blank">FlashDevelop</a> because it&#8217;s free and it has everything an IDE needs. I&#8217;m going to assume you&#8217;ve gone through the setup process and have configured FlashDevelop to use ActionScript 3 with the Flex SDK. This is also entirely free of charge and <a title="Installing the Flex SDK" href="http://www.flashdevelop.org/wikidocs/index.php?title=AS3#Installing_the_Flex_SDK" target="_blank">isn&#8217;t as much work as you might think</a>.

## Getting the Papervision3D code

Start of by creating a directory where you want to put the Papervision3D distribution. This won&#8217;t be your project directory because the distribution also contains the API documents and some examples.

In this directory right click and choose &#8220;SVN Checkout &#8230;&#8221; (adapt this to your system and SVN client) and enter the Papervision3D repository URL, which is <a title="Papervision3D SVN repository" href="http://papervision3d.googlecode.com/svn/trunk/as3/trunk/" target="_blank">http://papervision3d.googlecode.com/svn/trunk/as3/trunk/</a>. Choose &#8220;Fully recursive&#8221; if it isn&#8217;t already selected and click ok.

After a while you&#8217;ll have the distribution on your PC. It&#8217;ll contain a few directories, most importantly &#8220;src&#8221; containing the actual Papervision3D library.

## Setting up a Papervision3D project in FlashDevelop

No we&#8217;re ready to start a FD project. Open FlashDevelop and create a new AS3 Project. Put it in a different location than where you previously check out the Papervision3D distribution in order to avoid conflicts.

FlashDevelop will set up the project and create a &#8220;src&#8221; directory. It will also create an initial Main.as Flash application, but we&#8217;ll be replacing that in the next steps.

Copy the Papervision3D code into the src directory. Go into the src directory of the Papervision3D distribution and copy both directories (&#8220;nochump&#8221; and &#8220;org&#8221;) into the src directory of the FlashDevelop project.

Your workspace is ready.

## Running the MeshCutting example

Papervision3D comes with a few examples, most of them require you to set up external resources, but not the MeshCutting example.

You&#8217;ll find it in the &#8220;examples/FlexSDK/MeshCutting&#8221; directory of the Papervision3D distribution.

Copy the files in the &#8220;examples/FlexSDK/MeshCutting/src&#8221; to your project&#8217;s &#8220;src&#8221; directory. Make sure you replace the Main.as.

That should do it. Run the FlashDevelop project and you&#8217;ll be looking at this (animated):

[<img class="alignnone size-medium wp-image-2788" title="Papervision3D_mesh_cutting_example" src="http://www.streamhead.com/wp-content/uploads/2010/11/Papervision3D_mesh_cutting_example-300x241.png" alt="Papervision3D mesh cutting example" width="300" height="241" srcset="http://www.streamhead.com/wp-content/uploads/2010/11/Papervision3D_mesh_cutting_example-300x241.png 300w, http://www.streamhead.com/wp-content/uploads/2010/11/Papervision3D_mesh_cutting_example.png 816w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2010/11/Papervision3D_mesh_cutting_example.png)

And now the real work starts.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->