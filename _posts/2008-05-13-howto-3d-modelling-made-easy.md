---
id: 104
title: 'Howto: 3D modelling made easy'
date: 2008-05-13T01:29:07+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=104
permalink: /howto-3d-modelling-made-easy/
dsq_thread_id:
  - "5437884"
categories:
  - Graphics, Visuals and Texts
---
<img class="aligncenter size-full wp-image-105" title="model & light" src="http://www.streamhead.com/wp-content/uploads/2008/05/lichtjes.jpg" alt="" width="500" height="333" srcset="http://www.streamhead.com/wp-content/uploads/2008/05/lichtjes.jpg 600w, http://www.streamhead.com/wp-content/uploads/2008/05/lichtjes-300x200.jpg 300w" sizes="(max-width: 500px) 100vw, 500px" />

Sure, it is not yet finished and polished at all, but there used to be a time that creating the model above, texturing it and adding the lighting, would take you days. Now you can do it all in a few hours (and that includes setup time of the raytracing engine). It&#8217;s 3D modelling for the masses. And it&#8217;s all free.

_Tip:_ I&#8217;ve included a few tips in the article that you won&#8217;t need when you are just starting out. I&#8217;ve labeled them so you can just skip them if you want.

<img class="alignleft size-full wp-image-106" title="1" src="http://www.streamhead.com/wp-content/uploads/2008/05/1.png" alt="" width="23" height="26" />Get yourself the free version of <a title="Google SketchUp" href="http://sketchup.google.com/" target="_blank">SketchUp</a>. SketchUp is difficult to compare to other 3D tools. It uses a very intuitive interface to create 3D objects. To get started, take a look at some of the tutorials and you should be modelling within the hour. SketchUp is primarily suited for architects and engineers. Basically anything that has right angles and flat surfaces. If you want to model more organic shapes, it might be a little more challenging. In all honesty, I haven&#8217;t tried it yet, so if you have, leave a comment to tell me how it went.

_Tip:_ There is also a pro version available, but I doubt you&#8217;ll need it. There is one difference to keep in mind once you start rendering, and that is that you cannot configure the solar orientation in the free version of SketchUp. You can always rotate your object, but that means you will loose handy abilities to draw along your two horizontal axises. I would suggest to first draw the model and when it&#8217;s almost finished, rotate it. At that point you will have plenty of guides to help you, so you won&#8217;t miss the axises that much. If you are modelling a building, you&#8217;ll also need Google Earth (also free) if you want to <a title="Google SketchUp - Get current view button" href="http://download.sketchup.com/OnlineDoc/gsu_win/Q-Google/google-CurrentViewButton.htm" target="_blank">configure the location</a>.

<img class="alignleft size-full wp-image-107" title="2" src="http://www.streamhead.com/wp-content/uploads/2008/05/2.png" alt="" width="23" height="26" />SketchUp does have some limited raytracing functions. Out-of-the-box it can give you an impression of the shadows casted by the sun. Raytracing is what you need when you want to calculate exactly how lightrays will behave on your model. SketchUp, however, does not allow you to add light sources or do any real raytracing, so you are very limited.

You could export your model into a package such as <a title="Blender" href="http://www.blender.org/" target="_blank">Blender</a>, but that would make roundtrip modelling difficult: once you export to Blender, it&#8217;s difficult, if not impossible to change the model in SketchUp.

My preferred solution right now is the IRender nXt raytracing plugin for SketchUp. It integrates perfectly and makes it easy to add lights and start your renders. <a title="Getting started with IRender nXt" href="http://wiki.renderplus.com/index.php?title=IRender_nXt_-_Getting_Started" target="_blank">This IRender wiki article</a> should get you started right away. Currently IRender nXt is completely free, however, it still is beta software and once finalized, it will probably cost you quite a bit. So enjoy it while you can.

_Tip:_ Watch out when introducing sunlight into your traces. It will seriously slow down the process and you risk running into the predefined limits. By default, the IRender nXt engine is configured to stop after 10 minutes. Usually I don&#8217;t have a nice result yet at that point if I enable sunlight, so I&#8217;ve increased this number.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->