---
id: 124
title: 'More fun with free 3D tools &#8211; materials'
date: 2008-06-10T10:00:37+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=124
permalink: /more-fun-with-free-3d-tools-materials/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/06/lichtbox.png
dsq_thread_id:
  - "5437906"
categories:
  - Graphics, Visuals and Texts
---
<a title="Google SketchUp evangelizing" href="http://www.streamhead.com/?p=104" target="_blank">If you hadn&#8217;t noticed already</a>, I am a huge fan of the simplicity of <a title="Google SketchUp" href="http://sketchup.google.com/" target="_blank">Google&#8217;s SketchUp</a>. It gives the power of 3D to the people. Everybody with a mouse and a partially descent computer can get started right here, right now.

<a title="IRender nXt" href="http://wiki.renderplus.com/index.php?title=IRender_nXt_-_Getting_Started" target="_blank">IRender nXt</a> recently released a new preview version of their Google SketchUp plugin, so that was enough for me to pick it up one more time. This time I started experimenting with materials. <a title="my sample portfolio" href="http://www.streamhead.com/model/" target="_blank">You can see some results here</a>. The new version seemed to be a lot faster. If I rendered my previous models it took only a tenth of the time. However, as soon as I started some more complicated materials, I lost all that speed gain again. Obviously, this is only normal, translucent, reflecting materials require much more complicated calculations and rendering passes.

Although IRender&#8217;s the material editor is pretty straightforward, it&#8217;s also not completely polished yet. It did crash on me a few times and it was terribly slow. The material editor uses the rendering engine to give you a preview of the material, so I guess that&#8217;s why it&#8217;s not that fast. I also couldn&#8217;t get bump-mapping to give me any publishable results, so none of the pictures use it.

[<img class="alignright size-thumbnail wp-image-126" title="blackchromedetail" src="http://www.streamhead.com/wp-content/uploads/2008/06/zwartchromedetail-150x150.jpg" alt="" width="150" height="150" />](http://www.streamhead.com/wp-content/uploads/2008/06/zwartchromedetail.jpg)The most annoying limitation was that I couldn&#8217;t clone materials and create a child material with almost, but not quite, the same parameters. It always copied the last setting (of the clone) over the original material. Rather annoying if you want to compare slightly different options. It might be related to the way IRender plugs into the SketchUp engine. I also got some very unexpected results, maybe bugs? I&#8217;m not sure if they are correct (from a light-ray-calculating point-of-view) but they sometimes look nice. For instance the one on the right was pretty unexpected.

As you&#8217;ll notice if you compare those renderings to the one in the previous post, even the smallest tweaks improve the endresult tremendously. The whole change parameter &#8211; render &#8211; change &#8211; render cycle is pretty long, but it certainly is worth it.

As a somewhat interesting aside: I used <a title="960 Grid System" href="http://960.gs/" target="_blank">the 960 Grid System CSS framework</a> to quickly get the nice grid layout. No tables were used, and I didn&#8217;t have to mess hours with CSS to get it to show up correctly. Certainly <a title="blogpost on the 960 framework" href="http://www.runningskull.com/2008/working-with-960gs/" target="_blank">worth a look</a> if you&#8217;re into that kind of thing.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->