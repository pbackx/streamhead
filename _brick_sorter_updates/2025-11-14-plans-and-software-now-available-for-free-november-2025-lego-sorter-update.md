---
layout: page
title: "Plans and Software now available for free 🗂️ - November 2025 Lego Sorter Update"
date: 2025-11-14
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---

![](/assets/brick_sorter_updates/2025-11-14-plans-and-software-now-available-for-free-november-2025-lego-sorter-update/TeHe3w2tplpr2GFaEj1A554Onit7aL7LRBEeO7tY-3eb61e6cbc.jpg)

Hello builders and makers,

Welcome to this (sort-of) monthly newsletter! You’re receiving this because you
signed up for updates on the automated Lego sorting machine. If you’re no
longer interested, feel free to unsubscribe using the link at the bottom—no
tricks, no hard feelings.

# Pushing Boulders

In Greek mythology, Sisyphus was cursed to roll a boulder up a hill for
eternity. Every time he got close to the top, the boulder rolled back down.
Software development sometimes feels just like that: solve one problem, and
three new ones appear.

Let me tell you the story of my pursuit to redesign the LEGO sorting machine
with cheaper, more accessible components.

## **﻿﻿Attempt 1: The Build HAT Dream**

I started as a firm believer in the Build HAT. It eliminated the need for an
extra hub, making the system simpler and cheaper. But the standard library was
limited and unreliable, and writing custom firmware was beyond my capabilities.
After too much time spent chasing ghosts, I made the difficult decision to
scrap the idea.

## **﻿﻿Attempt 2: The PyBricks Broadcast Protocol**

Next, I turned to the Technic Hub and the PyBricks library. PyBricks offers a
few options for inter-device communication. The interesting ones are:

1. A Bluetooth broadcast protocol that requires no setup at all.
2. Bluetooth serial communication requires establishing a Bluetooth
   connection.

The broadcast protocol seemed simple and easy to use. What could go wrong?
Implementing the protocol on the computer side was a nightmare. Someone had
cracked it for Linux, but hadn't ported it to other systems. I tried to write a
Windows version, but abandoned ship before diving into the great technical
depths of Bluetooth specs and low-level drivers.

## **﻿﻿Attempt 3: Serial Bluetooth (Revisited)**

Third time's the charm? I circled back to serial Bluetooth, which I'd
previously dismissed as unreliable. But this time, it just worked. Maybe
PyBricks improved, maybe the Bluetooth library did, or maybe the Technic Hub
had a change of heart. Whatever the reason, the only hiccup was buffering the
data (the hub sends it in tiny 10-byte chunks). That is a small price to pay
for progress.

## **﻿﻿The Payoff: Plans and Code**

Remember my promises from the last newsletter? They're here.

* [Turntable plans are now on
  Rebrickable](https://rebrickable.com/mocs/MOC-240509/pbackx/customizable-poweredup-turntable/#details)—minimal parts, easy to adapt if you're missing a
  brick or two.
* [Software is up on my Codeberg
  profile](https://codeberg.org/peterb/sort_bot_powered_up).

**﻿The catch?** No price tag, it's all free. Documentation is
sparse for now, but I'm working on a video tutorial. I didn't want to delay the
release any longer.

# What's Next?

As I near the top of this hill, I can't shake the Sisyphus vibe. Will the
boulder roll back? To hedge my bets, I've kept things simple. I very carefully
tried to avoid overengineering the solution (a personal weakness).

For my end-of-year project, I'm going wild: experimenting with shaker-based
sorting, inspired by other builders. Can I make it work with a pure LEGO build?
No idea. But that's the fun part.

![](/assets/brick_sorter_updates/2025-11-14-plans-and-software-now-available-for-free-november-2025-lego-sorter-update/y72j2IavMdkZTVuw_giphy-b26ec67c6a.gif)

As always, your feedback is absolutely welcome. Thanks for following along on
this journey. Happy sorting, and I look forward to sharing more updates soon!

[﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿](https://github.com/pbackx/lego-sorter-pi/blob/brickognize/pi/04_sorting_bricks.ipynb)Peter