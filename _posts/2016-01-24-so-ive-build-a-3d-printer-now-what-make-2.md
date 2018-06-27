---
id: 3833
title: 'Starter&#8217;s Guide to 3D Printing: &#8220;So I&#8217;ve Build a 3D Printer, Now What?&#8221; (make #2)'
date: 2016-01-24T22:43:15+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3833
permalink: /so-ive-build-a-3d-printer-now-what-make-2/
pdrp_attributionLocation:
  - tag
dsq_thread_id:
  - "4571353665"
categories:
  - 3D Printing
tags:
  - 2016 Maker Challenge
---
Over the Christmas break I built [a RepRap 3D printer](http://s.click.aliexpress.com/e/fQvvnUnu7). Everything went well until it was finished. The information on getting started with actual printing is very fragmented and all over the place. So here&#8217;s a short guide for any budding RepRappers who can&#8217;t wait to get started.

<!--more-->

For a few years now, I&#8217;ve always wanted to build my own 3D printer. At the end of last year, I felt the time was right. Because it&#8217;s open source, a RepRap was my first choice.

As a first 3D printer build, I would suggest any one to go for a cheap kit. [I like Sunhokey on AliExpress. Their support is great!](http://s.click.aliexpress.com/e/fQvvnUnu7)

The documentation that comes with the printer is fine and you&#8217;ll be able to build the machine in 1 or 2 days.

## Calibration

However, the documentation ends when you turn on the printer. There is a bit of information, but it&#8217;s limited. That&#8217;s a pity, because it&#8217;s only then that the real work starts.

I&#8217;m sure you will want to print something ASAP and do all the tweaking later on. However, take 10 minutes and calibrate the following two things first:

  1. Leveling the bed and configuring the 0 position of the Z axis.
  2. Tweaking the &#8220;esteps&#8221; setting.

Take some time to get this right and you&#8217;ll be on your way for a quick and successful first print.

### Leveling the bed

Leveling the printer bed properly is the most important thing you need to do. The following video gives a good advise for how to do this. The Sunhokey RepRap Prusa i3 has tumb screws on the bed itself so it was a lot easier than what is shown, but the core idea doesn&#8217;t change.

[embedyt] http://www.youtube.com/watch?v=t5N-ouqU9sM[/embedyt]

### Configuring the esteps

Setting the right value for &#8220;esteps&#8221; is important to properly fill the objects and make them sturdy. Start with the first video and try the second if you feel like it could help.

[embedyt]https://www.youtube.com/watch?v=w_Wb0i0-Qvo[/embedyt]

[embedyt]https://www.youtube.com/watch?v=cnjE5udkNEA[/embedyt]

## First Prints

That was the boring part. Now it&#8217;s time to print something!

For your first prints, choose models that are not too complex and that have a good base. Also try to avoid large overhangs and bridges (parts floating in between others). Here are 5 good models to get started:

[<img class="size-medium wp-image-3842 alignnone" src="http://www.streamhead.com/wp-content/uploads/2016/01/Robot_Montage_MG_4628_preview_featured-300x225.jpg" alt="Maker Faire Robot by MAKE" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2016/01/Robot_Montage_MG_4628_preview_featured-300x225.jpg 300w, http://www.streamhead.com/wp-content/uploads/2016/01/Robot_Montage_MG_4628_preview_featured.jpg 628w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.thingiverse.com/thing:40212)

MAKE&#8217;s robot is a great small piece to get started. Start with the version with arms up. It&#8217;s small, so if something goes wrong, you&#8217;ll see it right away. It has a good wide base, so it should stick to the print bed well.

<a href="http://www.thingiverse.com/thing:1193565" rel="attachment wp-att-3843"><img class="alignnone size-medium wp-image-3843" src="http://www.streamhead.com/wp-content/uploads/2016/01/VTD1_preview_featured-300x225.jpg" alt="Victorian TofuDogs by dutchmogul" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2016/01/VTD1_preview_featured-300x225.jpg 300w, http://www.streamhead.com/wp-content/uploads/2016/01/VTD1_preview_featured.jpg 628w" sizes="(max-width: 300px) 100vw, 300px" /></a>

These are four more good models. They are fun to print in different sizes and colors. There&#8217;s a little more detail in them than in the maker robot. Check how well the faces are printed and try to improve.

<a href="http://www.thingiverse.com/thing:913069/" rel="attachment wp-att-3844"><img class="alignnone size-medium wp-image-3844" src="http://www.streamhead.com/wp-content/uploads/2016/01/IMG_4217_preview_featured-300x225.jpg" alt="Low Poly T-rex by slavikk" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2016/01/IMG_4217_preview_featured-300x225.jpg 300w, http://www.streamhead.com/wp-content/uploads/2016/01/IMG_4217_preview_featured.jpg 628w" sizes="(max-width: 300px) 100vw, 300px" /></a>

This is a good model to start and experiment with supports. A support is additional material that you print to support printing of, in this case, the chin. The idea is that you can easily remove it when printing is done.

By default, Slic3r will generate too much support structures. I&#8217;m still figuring the right settings out myself.

<a href="http://www.thingiverse.com/thing:977873" rel="attachment wp-att-3845"><img class="alignnone size-medium wp-image-3845" src="http://www.streamhead.com/wp-content/uploads/2016/01/P1030869_preview_featured-300x225.jpg" alt="Toy Boat by CreativeTools" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2016/01/P1030869_preview_featured-300x225.jpg 300w, http://www.streamhead.com/wp-content/uploads/2016/01/P1030869_preview_featured.jpg 628w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Another awesome model. With this one you can test overhangs (parts that print at an angle). You shouldn&#8217;t need any supports at all to print this properly.

<a href="http://www.thingiverse.com/thing:357444" rel="attachment wp-att-3846"><img class="alignnone size-medium wp-image-3846" src="http://www.streamhead.com/wp-content/uploads/2016/01/18animals1_preview_featured-300x225.jpg" alt="18animals puzzle by onepointdiy" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2016/01/18animals1_preview_featured-300x225.jpg 300w, http://www.streamhead.com/wp-content/uploads/2016/01/18animals1_preview_featured.jpg 628w" sizes="(max-width: 300px) 100vw, 300px" /></a>

This is a neat puzzle. It&#8217;s more difficult than you think.

Although you won&#8217;t be able to print it in multiple colors, it&#8217;s a very good test for your E-steps settings. If it&#8217;s too low, the parts won&#8217;t be filled. If it&#8217;s too high, the pieces will stick together.

## Next steps

When you&#8217;ve printed all of these models and some, you will start to get a good feel of what works and what doesn&#8217;t. At this point, all of the calibration advise will start to make a lot more sense. So now you could start printing some calibration objects to tweak your settings.

&nbsp;

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->