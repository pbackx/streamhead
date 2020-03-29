---
title: 3D Printing with ColorFabb varioShore TPU Filament
author: Peter Backx
layout: post
categories:
  - 3D Printing
---
I've been running a number of experiments to get some experience with [ColorFabb's new varioShore filament](https://colorfabb.com/varioshore-tpu-black). This is a TPU filament, so it's flexible, but the really interesting part is that it will expand when printed. How much it expands depends on the printing temperature.

<!--more-->



## Printing TPU on the Ultimaker 3

I have an Ultimaker3 printer that uses [a Bowden setup](https://www.fabbaloo.com/blog/2015/11/11/bowden-or-direct-a-primer-on-extruder-styles). Printing flexible materials, including this TPU materials such as varioShore can be tricky on bowden printers because the filament can tangle at various places in the feeder system.

The Ultimaker has a pretty good setup with very few places where the filament can bunch up, but it still happens.

When printing at lower temperatures, the feeder has to push the filament harder through the extruder. If it has to push too hard, the filament will tangle inside the feeder assembly. This of course ruins the print and is a mess to clean up. 

This can also happen on direct drive extruders, but a lot less, because a direct drive does not have to push against the additional friction of the bowden tube.

In practice, this meant that I was not able to reliably print below about 210°C. But as you'll read below, that didn't matter too much.

## varioShore Variable Expansion

[The varioShore box and site](https://colorfabb.com/varioshore-tpu-black) explain that the filament will not expand if you print between 190 and 200 degrees. If you increase the temperature it will start expanding.

I did a number of [testprints](https://www.thingiverse.com/thing:2939551) to figure out what the right temperature was for my printer:

* Up to about 210 degrees, there was little to no expansion.
* Anything higher and the magic started to happen. I did not see much difference between temperatures. 230 and 240 both required flow rates of about 60% (pictures show 70% but that's too much)

You can see the difference quite clearly in the following picture. The rightmost prints only had a 70% flowrate, but still the joints fused together:

![infill comparison](https://www.streamhead.com/assets/img/varioshore/ColorFabb_varioShore_infill_comparison.jpg)

For reference, here's the temperatures that they were printed at. Notice the issues I had printing at lower temperatures:

![printing temperatures](https://www.streamhead.com/assets/img/varioshore/ColorFabb_varioShore_temperature.jpg)

When I got those measurements down, I noticed something strange. I was expecting that the "expanded" prints would be more flexible than the "non-expanded" ones. But this turns out to be incorrect.

## Infill

The reason why is the infill. I used the same infill (20%) for all prints. However, when the material expanded, this meant there was actually more infill. Which in turn meant it was less flexible.

So the secret to playing around with the flexibility of prints is not the printing temperature (which is hard to change dynamically anyway) but it is the amount of infill.

At 200 degrees and 20% infill there was a under-extrusion at the top (see above) and the end result was also extremely flexible:

![200 degrees and 20%infill](https://www.streamhead.com/assets/img/varioshore/200_degrees_20_infill.gif)

At 240 degrees, again with 20% infill, the result was a lot stiffer. Also notice the stringing, which is inherent to TPU and Bowden. It can be cleaned up quite easily with a small knife or a bit of sanding:

![240 degrees and 20% infill](https://www.streamhead.com/assets/img/varioshore/240_degrees_20_infill.gif)

I did a final test print that had a number of the segments at 20% infill and others at 5%. The difference was easy to feel, but hard to show in a picture.

[In Cura, you can vary the infill by adding a simple object such as a square and using the "per model settings" to change the infill in certain areas](https://ultimaker.com/en/resources/52004-adjustment-tools). Note that the Cura manual is not entirely up-to-date with the latest Cura, but it's close enough.

## Conclusion

ColorFabb's varioShore is not the easiest material to print with. It required testing and experimenting before I was able to finetune the printing parameters and get the results I wanted.

But once I got that done, I was really happy with the material. It's very versatile, extremely light and strong. 

One thing I did not mention yet, is the feel of the material, it has a slight rough feeling and is completely different than the PLA or PETG prints that I am used to.