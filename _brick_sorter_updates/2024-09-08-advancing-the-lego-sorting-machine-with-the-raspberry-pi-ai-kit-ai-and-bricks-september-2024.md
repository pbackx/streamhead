---
layout: page
title: "Advancing the LEGO Sorting Machine with the Raspberry Pi AI Kit - AI and Bricks - September 2024"
date: 2024-09-08
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---
This post was originally send out to my newsletter subscribers. The newsletter documents all my updates and imrpovements to the Lego Sorting bot. It is an almost monthly newsletter (in practice, I send out about 6 newsletters per year). You can read previous editions here, or you can subscribe using the form below.

<div class="ml-embedded" data-form="wXZSvx"></div>

![](/assets/brick_sorter_updates/2024-09-08-advancing-the-lego-sorting-machine-with-the-raspberry-pi-ai-kit-ai-and-bricks-september-2024/J4l4deDaDc39RBnfjhIhDRRYvzR8R85GitwxvPs1-2654ec6849.jpg)

Hello LEGO enthusiasts,

Welcome to the latest update on the progress of my automated LEGO sorting
machine! Although this mail does not contain any major updates, I'm really
excited about the possibilities of the new hardware.

**Hardware Update: Raspberry Pi Integration**

In my ongoing quest to streamline the system, I’ve been exploring the
possibility of running the AI model directly on the Raspberry Pi 5, eliminating
the need for a desktop PC. Fortunately, the recent release of an AI kit,
designed specifically for the Raspberry Pi, now makes this possible.

I received the AI kit in late August, and installation was smooth and
straightforward. However, here are a few key points to keep in mind if you’re
considering a similar setup:

1. The Raspberry Pi 5 uses a new camera connector, so not all older cameras may
be compatible and you will, for sure, need a conversion cable (only a few
dollars).

2. It’s a good idea to get the active cooler for the Raspberry Pi 5 to avoid
overheating.

3. Many AI examples won’t run remotely, so I recommend connecting a screen,
mouse, and keyboard directly to the Pi.

**Learning and Next Steps**

While getting the existing AI examples up and running was relatively easy,
extending them or developing custom models is more complex due to limited
documentation. In the next few weeks, I'll be diving into the following areas:

- **GStreamer Pipelines:** Learning the basics to optimize
performance, as the AI kit integrates with GStreamer.

- **Model Training:** Retraining existing models using the Hailo
AI stick, which is central to this new kit.

- **Custom Model Creation:** Developing a custom AI model with the
Hailo software suite.

- **Remote Development:** Exploring RTSP streaming from the
Raspberry Pi via GStreamer and Video4Linux to improve remote development
workflows.

- **Camera Mounting:** Finding a better camera mounting solution
(hopefully with 3D-printable options) and testing the high-quality camera.

I’ll keep you updated as I continue to work through these challenges and
discoveries.

Stay tuned for more updates!

Best,

Peter