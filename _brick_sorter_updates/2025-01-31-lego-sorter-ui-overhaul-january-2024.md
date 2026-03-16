---
layout: page
title: "Lego Sorter UI overhaul - January 2024"
date: 2025-01-31
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---
This post was originally send out to my newsletter subscribers. The newsletter documents all my updates and imrpovements to the Lego Sorting bot. It is an almost monthly newsletter (in practice, I send out about 6 newsletters per year). You can read previous editions here, or you can subscribe using the form below.

<div class="ml-embedded" data-form="wXZSvx"></div>

![](/assets/brick_sorter_updates/2025-01-31-lego-sorter-ui-overhaul-january-2024/VxzMzDqNgq0wuPpMdG12TwlqUARfte7fMeA9U5Ko-d4ba746399.png)

Hello builders and makers, and best wishes for 2025!

As we wrap up the first month of the year, I’m excited to present the latest
improvement to the Lego sorting machine: a brand-new interface! This update
makes the system easier to use, simpler to configure, and far more approachable
for those who aren’t into programming.

**The New UI**

Until now, the machine has been running on a patchwork of a REST service,
Jupyter notebook code, and miscellaneous bits and pieces. This made the system
challenging to fully understand—let alone customize.  
  
I decided it was time for a clean slate, so I created a new repository to house
the revamped version of the project. While there’s minimal shared code from the
previous setup, this fresh start feels perfect for a new year.

You can find [the new repository right here on
Codeberg](https://codeberg.org/peterb/sort_bot): ﻿<https://codeberg.org/peterb/sort_bot>﻿  
  
One major task still on my plate is **adding proper
documentation.** If you’re familiar with the old system, you’ll likely
figure things out. However, for newcomers, clear instructions are essential—and
that’s my next priority.

With the new setup, you can connect to the machine from any browser on your
network or directly via a connected screen on the Raspberry Pi.

The new interface offers a dashboard that provides key insights into the
machine's inner workings, while also giving you full control over sorting
configurations:

**Quick start:**

1. Install and configure the code as instructed in the readme.
2. Test if the camera stream works.
3. Check if you can control the buckets.
4. Predict a single brick.
5. When that’s working, start the machine and let the sorting fun begin! 🎉

**Next Steps**

Here’s what’s on my roadmap:

1. **Documentation:**  
   I’ll focus on creating detailed guides on how to run the system and extend
   its functionality.
2. **Simplified Installation:**  
   I plan to package everything for easy installation—no coding required. I may
   even create a pre-configured image that you can flash onto an SD card to get
   started right away.
3. **EV3 Replacement:**  
   I have been talking a long time about this, but I aim to replace the EV3 with
   a Raspberry Pi Build HAT in the next 2 or 3 months. This will streamline the
   setup and allow for faster, more reliable operation.

As always, your feedback is absolutely welcome. Thanks for following along on
this journey. Happy sorting, and I look forward to sharing more updates soon!

[﻿﻿](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/04_sorting_bricks.ipynb)Peter