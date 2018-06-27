---
id: 1122
title: 'Tutorial: Applying and Manipulating a Mask in ActionScript 3'
date: 2009-03-17T10:00:16+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1122
permalink: /tutorial-applying-manipulating-mask-actionscript-3/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/03/masks.png
dsq_thread_id:
  - "13830051"
image: /wp-content/uploads/2009/03/masks.png
categories:
  - Flash and ActionScript
tags:
  - as3
  - flashdevelop
---
Flash has become the de-facto standard for all kinds of web animations. One of the main reasons, is that it offers an impressive array of bitmap manipulation functions. Out of the box it probably has one of the richest API&#8217;s to manipulate bitmaps, vectors and even animation. One of those possibilities is masking, which I will explain in this post.

<a title="AS3 mask tutorial in FlashDevelop" href="http://www.streamhead.com/wp-content/uploads/2009/03/worldscape.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />download the full source and FlashDevelop project right here</a>

As you will learn in this small tutorial, applying a mask to any Flash object is incredibly easy. However, if you search for more information on Google, you&#8217;ll only find ActionScript 2 tutorials. This one is specific for ActionScript 3 and furthermore it is a pure ActionScript solution, so you don&#8217;t need to buy anything. <a title="How to use Sand3D with FlashDevelop" href="http://www.streamhead.com/tutorial-getting-started-with-sandy-3d-and-flashdevelop/" target="_blank">FlashDevelop</a> will do just fine. They have just released <a title="FlashDevelop 3.0.0 RC2" href="http://www.flashdevelop.org/community/viewtopic.php?f=11&t=4374" target="_blank">a new version</a>.

Applying a mask is just as easy as it used to be in AS2:

<pre lang="ActionScript">background.mask = myMask;</pre>

The mask itself is a Sprite on which I drew a rectangle. You could make it pretty much any shape. I put the rectangle in the top left corner and moved the sprite. This will make it a lot easier to move and rescale the sprite later on.

<pre lang="ActionScript">myMask = new Sprite();
myMask.graphics.beginFill(0x00FF00);
myMask.graphics.drawRect(0, 0, myMaskSize, myMaskSize);
myMask.x = 350;
myMask.y = 250;
addChild(myMask);</pre>

This is all pretty straightforward, however I was a bit stumped when I wanted to let the user move the mask with his mouse. Apparently it&#8217;s not possible to attach an event listener to a Sprite once it is a mask. According to all the AS2 demos I found, this used to be possible. But no problem, I attached them to the stage. If you only want to register clicks on the displayed area, you might want to do a little processing of the mouse coordinates in the mouseDown method, but I didn&#8217;t bother.

Just for kicks I also added a mouse wheel listener, so that you can change the size of the masked area. This is the result:



You might notice that Flash still forwards the scroll event to the browser, so the browser window also scrolls. Apparently there isn&#8217;t a good solution for this problem. So beware if you want to use the scroll event in a real application.

<a title="AS3 mask tutorial in FlashDevelop" href="http://www.streamhead.com/wp-content/uploads/2009/03/worldscape.zip" target="_blank"><img class="alignleft size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />download the full source and FlashDevelop project right here</a>

[Image credit](http://www.flickr.com/photos/exfordy/128576390/ "Masks - Flickr")

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->