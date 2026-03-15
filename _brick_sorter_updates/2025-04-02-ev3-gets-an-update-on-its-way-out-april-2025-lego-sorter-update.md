---
layout: page
title: "EV3 Gets an Update 🆙 on Its Way Out 🪦 - April 2025 Lego Sorter Update"
date: 2025-04-02
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---

![](/assets/brick_sorter_updates/2025-04-02-ev3-gets-an-update-on-its-way-out-april-2025-lego-sorter-update/BY575xoS1l9Hw31uQT8B2qjYg3Lrz2PYtP4BXxx8-fc0f9ca177.jpg)

Hello builders and makers,

This update is long overdue, thanks to an incredible ski season ⛷️! Although
the current development isn't fully complete, I didn't want to delay this
newsletter any longer. I've made significant improvements to the EV3 code.
However, I've also realized that it ultimately leads to a dead end.

**﻿﻿EV3 Code**

Except for some cosmetic changes, I haven't updated the code that runs on the
EV3 since the start of the project. And it was starting to show.

The most important issue was when one of the motors would not be correctly
connected. Because the contacts are starting to age, bad connections with the
cables were occurring more frequently and, when it happened, it was crashing
the EV3. This was terribly annoying.

At the same time, I also wanted to improve the way that you can install the
software.

﻿﻿﻿[The new version that you can find
on Codeberg](https://codeberg.org/peterb/sort_bot-control) does:

* **﻿Error checking**. When something is not connected, it does
  not crash, but sends an error message through MQTT so you know what is wrong
  and can correct it.
* **Installs as a Debian package**. I still need to publish the
  package, but when it is done, the entire EV3 setup will be writing the SD
  card and executing one *apt-get* statement.

During the development, I ﻿wanted to buy some spare EV3 motors, however it
turns out that these parts have become terribly expensive. If you wanted to buy
all the EV3 parts required for the LEGO sorting machine on Bricklink, you would
need to pay about €300/$300 😦

That's just unacceptable, so replacing the EV3 parts with new PoweredUp parts
is now a lot higher on my priority list!

**﻿﻿What's Next?**

Here’s what I will be working on next:

1. **Documentation:**  
   Both the EV3 code and last month's server code need to be documented. When
   that is done, setup of the sorting machine's software should be a matter of
   minutes or at most an hour and no training will be required.
2. **EV3 Replacement:**  
   I have known for quite some time, but the EV3 has got to go. It is expensive
   and outdated.

As always, your feedback is absolutely welcome. Thanks for following along on
this journey. Happy sorting, and I look forward to sharing more updates soon!

[﻿﻿﻿﻿﻿﻿﻿﻿﻿](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/04_sorting_bricks.ipynb)Peter