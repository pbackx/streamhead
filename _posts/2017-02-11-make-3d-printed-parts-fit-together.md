---
id: 3945
title: How to Make 3D Printed Parts Fit Together
date: 2017-02-11T10:08:07+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3945
permalink: /make-3d-printed-parts-fit-together/
aFhfc_head_code:
  - ""
aFhfc_footer_code:
  - ""
image: /wp-content/uploads/2017/01/print_in_place_ball_bearings-672x372.jpg
categories:
  - 3D Printing
---
One of the great things about 3D printing is that you can print an entire model in one go. The typical example is the fully assembled &#8220;print-in-place&#8221; ball bearing as shown in the image above. This is printed in one go, no assembly required. However, the tolerances are pretty small which requires a well-tuned 3D printer. In this article, I describe how I tune my machine for perfect fit.

<!--more-->

Because layers of a 3D printed object are never perfectly aligned, you need a bit of a margin between parts that should touch. If you don&#8217;t, the two parts will fuse together.

There are test objects that you can print to help you figure out what margins you need. I printed [this test](http://www.instructables.com/id/Objet-3D-Printer-Fit-Tests/) and it turns out, the parts didn&#8217;t even fit at the largest margin.

Clearly something was wrong with my settings.

And thus began a frustrating experience of figuring out how to exactly align all the different factors that influence a perfectly printed part.

The **three factors** you need to take into account are:

  * **E-steps**, or how fast your extruder will push filament through the nozzle.
  * The extrusion size, which is the **layer height** and **extrusion width** of the extruded filament.
  * The **extrusion multiplier**, which allows you to tweak the amount of filament extruder per type of filament.

## Calibrate E-steps

This is the most important thing to you can do to improve your prints. You need to tune the extruder steps setting to perfection. I&#8217;ve already mentioned those in [my previous article](http://www.streamhead.com/so-ive-build-a-3d-printer-now-what-make-2/), but I&#8217;m going to repeat those two videos, these are exactly what you need:

[embedyt]https://www.youtube.com/watch?v=w_Wb0i0-Qvo[/embedyt]

[embedyt]https://www.youtube.com/watch?v=cnjE5udkNEA[/embedyt]

[This is the model you need](https://github.com/ahmetcemturan/SFACT/blob/master/calibration/_40x10.STL).

## Extrusion Width and Layer Height

In your slicer, you can configure the extrusion width and layer height.

**Your layer height should stay well below your nozzle diameter**. If you have a 0.4mm nozzle, a layer height of 0.2mm is fine. 0.1mm will work too, but your prints will take double the time.

Most slicers, such as Slic3r will, by default, automatically calculate an extrusion width value that they consider &#8220;good&#8221; for your nozzle diameter.

**In general you want the extrusion width to be wider than the diameter of your nozzle**. So if you have a 0.4mm diameter nozzle, go for 0.5mm width. If you go below that, chances are there will be some overextrusion which will almost certainly make parts not fit (most importantly, you&#8217;ll get too small holes in your prints)<figure id="attachment_3957" style="width: 680px" class="wp-caption aligncenter">

<img class="size-full wp-image-3957" src="http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_advanced_settings_for_4_nozzle.png" alt="" width="680" height="589" srcset="http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_advanced_settings_for_4_nozzle.png 680w, http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_advanced_settings_for_4_nozzle-300x260.png 300w" sizes="(max-width: 680px) 100vw, 680px" /><figcaption class="wp-caption-text">I decided to go for 0.5mm extrusion width for everything. Some articles suggest decreasing the perimeter width, but going below 0.5mm only made things worse on my printer.</figcaption></figure> 

Many tutorials on fit calibration will tell you to decrease the extrusion width of the perimeters. This is good advice, as long as you don&#8217;t go below your nozzle&#8217;s diameter.

<img class="aligncenter size-large wp-image-3952" src="http://www.streamhead.com/wp-content/uploads/2017/02/s-plugs-1024x576.jpg" alt="A bunch of calibration test prints" width="474" height="267" srcset="http://www.streamhead.com/wp-content/uploads/2017/02/s-plugs-1024x576.jpg 1024w, http://www.streamhead.com/wp-content/uploads/2017/02/s-plugs-300x169.jpg 300w, http://www.streamhead.com/wp-content/uploads/2017/02/s-plugs-768x432.jpg 768w" sizes="(max-width: 474px) 100vw, 474px" />

## Extrusion Multiplier

With all of that out of the way, it&#8217;s time to start printing calibration pieces and fine tune the extrusion multiplier until the result is what you want.

[I like this S-plug design because it is a quick print, unlike some other calibration objects](http://www.thingiverse.com/thing:342198).

Start by printing it with your current settings and check that:

  * The bottom and top layers are filled, but are not bulging.
  * The pieces fit. You should need a bit of force to push them together.
  * Layers are not separated

Probably your first test is not going to be right. This is where tuning the extrusion multiplier comes into play.

Go to the filament settings in your slicer program and change the **extrusion multiplier: increase it if you the fit is too loose or decrease it if you were not able to push the parts together.**<figure id="attachment_3958" style="width: 807px" class="wp-caption aligncenter">

<img class="size-full wp-image-3958" src="http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_filament_settings.png" alt="" width="807" height="289" srcset="http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_filament_settings.png 807w, http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_filament_settings-300x107.png 300w, http://www.streamhead.com/wp-content/uploads/2017/02/slic3r_filament_settings-768x275.png 768w" sizes="(max-width: 807px) 100vw, 807px" /><figcaption class="wp-caption-text">The ColorFabb filament uses an extrusion multiplier of 0.9 which is at the low end. This is because I did most the tuning with a cheap filament that was not 1.75mm but a bit less. I probably should redo my E-steps tuning.</figcaption></figure> 

## Result

You are now able to print all of those cool objects with joints and bearings that always used to fuse together. Awesome!

From now on, every time you want to start using a new roll of filament, you print a few S plugs and adjust the extrusion multiplier for that filament. That will ensure perfect fit.

[This is a cool test object if you&#8217;re looking for something to try](http://www.thingiverse.com/thing:1230075).

<img class="aligncenter size-large wp-image-3953" src="http://www.streamhead.com/wp-content/uploads/2017/02/stackable_box_toy-1024x576.jpg" alt="A crossing between a robot and a box" width="474" height="267" srcset="http://www.streamhead.com/wp-content/uploads/2017/02/stackable_box_toy-1024x576.jpg 1024w, http://www.streamhead.com/wp-content/uploads/2017/02/stackable_box_toy-300x169.jpg 300w, http://www.streamhead.com/wp-content/uploads/2017/02/stackable_box_toy-768x432.jpg 768w" sizes="(max-width: 474px) 100vw, 474px" />

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->