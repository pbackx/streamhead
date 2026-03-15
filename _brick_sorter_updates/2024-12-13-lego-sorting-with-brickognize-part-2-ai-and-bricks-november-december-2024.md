---
layout: page
title: "Lego Sorting with Brickognize part 2 - AI and Bricks - November/December 2024"
date: 2024-12-13
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---

![](/assets/brick_sorter_updates/2024-12-13-lego-sorting-with-brickognize-part-2-ai-and-bricks-november-december-2024/kYJEHCZOqUPhzeod8CxLh0uWgwHmkvf4pIsr5bxW-d1803dd681.png)

Hello LEGO enthusiasts,

Hello and welcome to the Lego sorter newsletter. As a reminder, you are
receiving this because you expressed interest in being kept up-to-date on my
adventures in sorting Lego bricks with AI and various contraptions. If you no
longer want to receive these mails, there is an unsubscribe link at the
bottom.  
  
This month, I've been making exciting progress with my machine, including a new
integration with Brickognize that makes sorting bricks smarter and faster. If
you're curious about the latest updates and challenges, keep reading!

**﻿﻿﻿Integrating Brickognize**

As suggested by you, the reader (Thanks!), I integrated Brickognize into the
Lego sorting machine, which eliminates the need to collect training data
manually and rely on a powerful GPU for training. With this update, you can
start sorting bricks straight away using [the brickognize
branch](https://github.com/pbackx/lego-sorter-pi/tree/brickognize) of the software.  
  
Currently, the integration is available in the [pi/predict.py](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/predict.py)
script, which offers two options for sorting: the old local AI method or the
new Brickognize-based approach. You can select your preference in the
[pi/04\_sorting\_bricks.ipynb](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/04_sorting_bricks.ipynb)
notebook.  
  
While still in the early stages, I’m planning to create a standalone
application for sorting that’s more user-friendly than Jupyter Notebook. Stay
tuned for updates!

**﻿﻿﻿Failure modes**

As I continue testing the machine, I’ve been documenting potential failure
modes to refine its performance and reliability. Here are the main challenges
I’ve identified so far:

* **﻿﻿﻿Feeding Issues**:
  + Bricks can get stuck in the initial feeder belt, which isn't wrapped in
    paper.
  + Larger bricks sometimes jam the middle conveyor belt,
    requiring manual intervention.
* **Brick Placement:**
  + Two pieces can drop in front of the camera
    simultaneously, especially smaller parts, leading to misclassification.
  + Some bricks are hard to distinguish from a top-down view. I’m exploring
    angled or multi-angle photos to improve accuracy.

Writing these down helps me brainstorm solutions and focus on the most
impactful fixes. The feeder section, in particular, has been frustrating—time
to revisit its original design!

**﻿﻿﻿What's Next?**

As we approach the end of 2024, I want to wish you an early Happy New Year!
It’s unlikely I’ll send another newsletter before January, so here’s what’s
next:  
  
I’m planning to transition the machine to use Lego Powered Up motors and the
[Pi Build HAT](https://www.raspberrypi.com/news/raspberry-pi-build-hat-lego-education/),
which will simplify the setup and significantly speed up operations. To
prepare, I’ve already picked up the [Audi RS Q e-tron
(42160)](https://www.lego.com/nl-be/product/audi-rs-q-e-tron-42160)—a fun build that also comes with three motors I
need!  
  
Thank you for following my journey. Your feedback and interest have been
incredibly motivating, and I look forward to sharing more progress in 2025.

See you next year,

[﻿](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/04_sorting_bricks.ipynb)Peter