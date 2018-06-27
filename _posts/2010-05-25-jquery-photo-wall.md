---
id: 2325
title: Three jQuery Tutorials for a Perfect Photo Wall
date: 2010-05-25T10:00:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2325
permalink: /jquery-photo-wall/
dsq_thread_id:
  - "100717513"
image: /wp-content/uploads/2010/05/amazon_windowshop.png
categories:
  - Java and JavaScript
---
I&#8217;ve been doing a little research into <a title="jQuery" href="http://jquery.com/" target="_blank">jQuery</a> and the many many plugins and tutorials available. Vaadin and GWT can be nice if you want to create a full-blown web application, but sometimes you just need something a little lighter that just gets the job done. For instance, in this post I take a look at the existing tutorials to create a &#8220;photo wall&#8221;, a big webpage consisting of photos that can be manipulated.

<!--more-->If there&#8217;s one reason you choose to work with 

<a title="jQuery" href="http://jquery.com/" target="_blank">jQuery</a> it should be the massive and seemingly endless amount of documentation, tutorials and extensions. In fact, you might even be tempted to not choose jQuery because there&#8217;s a true risk of information overload. But if you get through that, jQuery is a great JavaScript library that will transform your JS code into something that is actually readable.

I want to dive a little deeper into jQuery with a small sample application. The main screen is going to be a wall of images. Loosely inspired by <a title="Amazon Windowshop" href="http://www.windowshop.com/" target="_blank">Amazon Windowshop</a> (the site doesn&#8217;t work for me right now), but I don&#8217;t think I&#8217;m going to incorporate a 3rd dimension.

I started by Google-ing a bit and turned up 3 tutorials to get started. I think you&#8217;ll like them too.

## <a title="Sliding Panel Photo Wall Gallery" href="http://tympanus.net/codrops/2010/05/14/sliding-panel-photo-wall-gallery-with-jquery/" target="_blank">Sliding Panel Photo Wall Gallery by Codrops</a>

<img class="alignnone size-full wp-image-2329" title="photowall" src="http://www.streamhead.com/wp-content/uploads/2010/05/photowall.jpg" alt="Sliding Panel Photowall" width="580" height="315" srcset="http://www.streamhead.com/wp-content/uploads/2010/05/photowall.jpg 580w, http://www.streamhead.com/wp-content/uploads/2010/05/photowall-300x162.jpg 300w" sizes="(max-width: 580px) 100vw, 580px" />

Is the most literal implementation of what I was looking for. It goes into the code necessary to show a thumbnail of a large number of images and click through for a dynamically loaded detail page. Interesting and clear code.

## <a title="Sponsor Flip Wall" href="http://tutorialzine.com/2010/03/sponsor-wall-flip-jquery-css/" target="_blank">Sponsor Flip Wall by Tutorialzine</a>

<img class="alignnone size-full wp-image-2330" title="sponsor_flip_wall" src="http://www.streamhead.com/wp-content/uploads/2010/05/sponsor_flip_wall.jpg" alt="Sponsor Flip Wall" width="620" height="340" srcset="http://www.streamhead.com/wp-content/uploads/2010/05/sponsor_flip_wall.jpg 620w, http://www.streamhead.com/wp-content/uploads/2010/05/sponsor_flip_wall-300x164.jpg 300w" sizes="(max-width: 620px) 100vw, 620px" />

Another nice example of a slightly different interpretation. It has a neat card-turning effect to show details. Also lots of code and a nice demo. There is some PHP code, but it can be easily replaced, even if you don&#8217;t know PHP.

## <a title="Build a Photo Wall" href="http://kylerush.net/javascript/tutorial-flickr-api-javascript-jquery-ajax-json-build-detailed-photo-wall/" target="_blank">Use the Flickr API to Build a Photo Wall</a>

<img class="alignnone size-full wp-image-2331" title="flickr-tutorial-img" src="http://www.streamhead.com/wp-content/uploads/2010/05/flickr-tutorial-img.jpg" alt="Flickr Photo Wall" width="630" height="200" srcset="http://www.streamhead.com/wp-content/uploads/2010/05/flickr-tutorial-img.jpg 630w, http://www.streamhead.com/wp-content/uploads/2010/05/flickr-tutorial-img-300x95.jpg 300w" sizes="(max-width: 630px) 100vw, 630px" />

This one adds integration with Flickr on top of the photo wall.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->