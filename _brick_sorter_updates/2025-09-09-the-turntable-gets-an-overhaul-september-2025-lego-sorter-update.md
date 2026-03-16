---
layout: page
title: "The Turntable Gets an Overhaul 🎡 - September 2025 Lego Sorter Update"
date: 2025-09-09
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---
This post was originally send out to my newsletter subscribers. The newsletter documents all my updates and imrpovements to the Lego Sorting bot. It is an almost monthly newsletter (in practice, I send out about 6 newsletters per year). You can read previous editions here, or you can subscribe using the form below.

<div class="ml-embedded" data-form="wXZSvx"></div>

Hello builders and makers,

Welcome to this (sort-of) monthly newsletter! You’re receiving this because you
signed up for updates on the automated Lego sorting machine. If you’re no
longer interested, feel free to unsubscribe using the link at the bottom—no
tricks, no hard feelings.

# Why the Delay?

This newsletter is long overdue, and I’ll be honest: I kept delaying it because
I was always *one step away* from the next breakthrough. I wanted to
share something fully finished, but I kept moving the goalpost. No more
waiting—here’s what I’ve been (slowly) working on over the past two months:
**a complete overhaul of the turntable section**, where bricks get
sorted into bins.

Let’s dive into the updates, covering both **hardware** (the
bricks) and **software** (the Build HAT and Python code).

![](/assets/brick_sorter_updates/2025-09-09-the-turntable-gets-an-overhaul-september-2025-lego-sorter-update/ZIpV4oJ1SNdeDFJrWUSi9TnDTmEekwGrBT7H69ww-f4ddb6ea4e.png)

# 1. Hardware: A Fresh Start

I’ve mentioned before that I urgently needed to move away from EV3 parts. While
they’re easier to work with for this kind of project, they’re outdated, hard to
find, and expensive. The new turntable design now uses a **Lego Technic
Large Motor**, which is currently one of the easiest Lego motors to
source.

### Key Improvements:

* **Simplified Design:** The new turntable uses far fewer parts
  than before. I’m still using the "Bucket Wheel" as parts donor, but I’m
  confident many components can be swapped for similar alternatives (something
  I’ll explore later).
* **Reliability:** I rebuilt the turntable twice—earlier
  prototypes *seemed* perfect in theory but failed in practice. This
  version has been running smoothly without issues.

### **What’s Left to Do:**

* **Stability Testing:** I need to load the bins and confirm that
  the smaller footprint remains stable. I’m optimistic, but only testing will
  tell.
* **Calibration:** Since this design no longer includes a color
  sensor, it will rely on detecting motor stalls for calibration. Lego uses
  this approach often, but it’s surprisingly tricky with the Build HAT.

![](/assets/brick_sorter_updates/2025-09-09-the-turntable-gets-an-overhaul-september-2025-lego-sorter-update/9x7jjTZ3mCqSGDYjzOAYDr8LDo5WKo6tAxectQ3s-526c1d10c6.png)

# 2. Software: The Build HAT Experience

The Lego motor connects to a Build HAT, which interfaces with a Raspberry Pi.
Both are accessible and reasonably well-supported, but I’ve hit a few snags:

* The software library is basic and hasn’t seen regular updates.
* The special power supply also doesn’t play nicely with the Raspberry Pi 5.

Nothing deal-breaking, but it’s made me question whether the Build HAT is
the best long-term choice. I want hardware that’s affordable and future-proof.

## Coding with Claude

I’ve been “vibe coding” with my AI coding buddy, Claude. It’s a fun,
unconventional way to write software, but it has its quirks. Claude insisted
the code was flawless, yet the turntable wasn’t behaving as expected. With some
guidance, we arrived at functional, maintainable code—but it took a few
iterations.

# 3. Next Steps.

* **Finalize Calibration:** The code is almost there. A week or
  two more with Claude should iron out the kinks.
* **Publish Plans:** I’ll model the turntable in **Lego
  Studio** and release the plans (and code) for free on
  **Rebrickable**.
* **Future Updates:** The camera section of the sorting
  machine works well, so I don't think I will do a big redesign of it. However,
  for the front section, I’m eyeing designs with a **shaker
  motor**, which seem more reliable than my current setup.

# Final Thoughts

Progress is slower than I’d like, but it’s progress nonetheless. Thanks for
sticking around, and stay tuned for the Rebrickable release!

As always, your feedback is absolutely welcome. Thanks for following along on
this journey. Happy sorting, and I look forward to sharing more updates soon!

[﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/04_sorting_bricks.ipynb)Peter