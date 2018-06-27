---
id: 2516
title: Embedding Bitmap Images in ActionScript 3 with FlashDevelop
date: 2010-08-24T10:00:32+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2516
permalink: /embedding-images/
dsq_thread_id:
  - "132923039"
image: /wp-content/uploads/2010/08/embed_actionscript.png
categories:
  - Flash and ActionScript
---
ActionScript is probably one of the easiest languages to program visual effects. It has a wealth of APIs to manipulate images in all kinds of different ways. However, getting images into your program isn&#8217;t all that well documented. Especially if you are not working with Adobe&#8217;s commercial Flash products. For instance, the wonderful and free FlashDevelop. This article shows how to use the &#8220;embed&#8221; tag to embed images inside your Flash applet, which is one of the cleanest ways you can add those bitmaps to your application.

<!--more-->

This article is based on [FlashDevelop 3.2.2 RTM](http://www.flashdevelop.org/community/viewtopic.php?f=11&t=6956) but will probably work with almost any FlashDevelop version. It is an updated, rewritten and more focused version of [this article](../how-to-use-images-in-actionscript-3-with-flashdevelop-and-some-other-as3-tips), published back in May 2008. In this tutorial I&#8217;ll show you how to get started with FlashDevelop, embed a bitmap and show it on screen.

## Setup your system

Before you get started with this tutorial, you should make sure that you have configured FlashDevelop as explained in the [FlashDevelop getting started guide](http://www.flashdevelop.org/wikidocs/index.php?title=Getting_Started). When the debug players are installed (I went with version 10.1), choose [the ActionScript 3 option](http://www.flashdevelop.org/wikidocs/index.php?title=AS3) at the bottom of the page and install [the free Flex SDK](http://opensource.adobe.com/wiki/display/flexsdk/Downloads) (I picked the free Adobe Flex 4 SDK).

## Creating a project

With FlashDevelop installed and configured, the next step is creating a new project:

  * Project > New Project
  * We&#8217;re going to write an ActionScript 3 application, so pick AS3 Project
  * At the bottom of the dialog, enter a name and a location. It doesn&#8217;t really matter what you enter here, just choose something that suits you.
  * I left the package blank, which creates files in the default package.
  * OK

You should see your project structure on the right. Now open the &#8220;src&#8221; folder and double-click Main.as. This should open the file. If you test the movie (the blue arrow triangle in the top bar, just to the left of the &#8220;debug&#8221; dropdown), you&#8217;ll probably see an error in the output pane (bottom): &#8220;No application is associated with the specified file for this operation&#8221;.

<div>
  Go back to the project window on the right (I had to click on the little tab at the bottom)
</div>

<div>
  <ul>
    <li>
      Right click on your projects top folder.
    </li>
    <li>
      Choose &#8220;Properties&#8230;&#8221;
    </li>
    <li>
      At the bottom, in the &#8220;Test Movie&#8221; dropdown, pick &#8220;Play in new tab&#8221; (this is my preferred method, feel free to experiment with the others)
    </li>
  </ul>
  
  <p>
    After clicking ok and rerunning the test (blue triangle), a new tab should open which displays absolutely nothing. That&#8217;s fine though, it means everything is working. Close the tab and we&#8217;ll get started on the program.
  </p>
</div>

## Embedding an image

<div>
  Now it&#8217;s time to get to the gist of the tutorial, actually embedding the image. If you look at your project structure, you&#8217;ll also see that FlashDevelop has created a &#8220;lib&#8221; folder, this is where we&#8217;re going to put the images we use in the program.
</div>

<div>
  First, find an image somewhere on the Internet and put it in that lib folder. If it shows up on the project view in FlashDevelop, you did it correctly.
</div>

<div>
  The final step before we can use the image is to add it to the library: right click on the image in the project view and choose &#8220;Add to library&#8221;. If everything goes well, it will now display in blue instead of black.
</div>

<div>
  With the Main.as file open:
</div>

<div>
  <ul>
    <li>
      Put the cursor somewhere just above the &#8220;function Main()&#8221; declaration
    </li>
    <li>
      Right click on the image you want to embed and choose &#8220;Insert Into Document&#8221;
    </li>
    <li>
      An &#8220;Embed&#8221; code should have appeared.
    </li>
    <li>
      Just underneath this new line, add the variable declaration for this image.
    </li>
  </ul>
  
  <pre>private var layer0Class : Class;</pre>
  
  <ul>
    <li>
      On the next line, instantiate the class, so that we can use it:
    </li>
  </ul>
  
  <pre>private var layer0:Bitmap = new layer0Class();</pre>
  
  <ul>
    <li>
      If you type this, you will see a FlashDevelop popup when you start typing Bitmap. As soon as you see this, you can select the class you need, which is &#8220;flash.display.Bitmap&#8221;. This will also import that class.
    </li>
    <li>
      If that didn&#8217;t happen, you will need to manually add the import. Right at the top of the file, where there are two import statements, add:
    </li>
  </ul>
  
  <pre>import flash.display.Bitmap;</pre>
  
  <h2>
    Displaying the bitmap
  </h2>
</div>

<div>
  Now comes the easiest part:
</div>

<div>
  <ul>
    <li>
      Find the function where it says &#8220;// entry point&#8221; (feel free to remove this line as it is not functional)
    </li>
    <li>
      Just underneath that line add
    </li>
  </ul>
  
  <pre>addChild(layer0);</pre>
  
  <div>
    You should now have the following program:
  </div>
</div>

<pre lang="ActionScript">package 
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class Main extends Sprite 
	{
		[Embed(source = '../lib/Parallax-scroll-example-layer-0.gif')]
		private var layer0Class:Class;
		private var layer0:Bitmap = new layer0Class();
		
		public function Main():void 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);

			addChild(layer0);			
		}
	}	
}</pre>

If you test the movie again, the image should show up. You&#8217;ve just embedded and instantiated your first bitmap in ActionScript.

<div>
  With this knowledge and some very basic ActionScript 3 programming experience, you can already create some nice effects, such as <a href="http://en.wikipedia.org/wiki/Parallax_scrolling">this parallax scrolling</a> example:
</div>



<a title="Parallax Scrolling AS3" href="http://github.com/pbackx/ParallaxScrollingAS3" target="_blank">You can find the full source and project files on GitHub</a>.

([Image credit](http://www.flickr.com/photos/liamngls/413522957/))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->