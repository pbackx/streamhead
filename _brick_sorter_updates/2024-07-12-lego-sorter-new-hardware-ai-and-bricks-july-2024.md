---
layout: page
title: "Lego Sorter new hardware 🔌 - AI and Bricks - July 2024"
date: 2024-07-12
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
---
This post was originally send out to my newsletter subscribers. The newsletter documents all my updates and imrpovements to the Lego Sorting bot. It is an almost monthly newsletter (in practice, I send out about 6 newsletters per year). You can read previous editions here, or you can subscribe using the form below.

<div class="ml-embedded" data-form="wXZSvx"></div>

![](/assets/brick_sorter_updates/2024-07-12-lego-sorter-new-hardware-ai-and-bricks-july-2024/uIUXyfJY6YtVRsOVPaX0U0SBIwPNU2ypAGjwkFBM-e97f96b02f.jpg)

**note**: I had ChatGPT generate a header image, because I don't yet have anything to show. Read on to find out why 🫣

**Hello and welcome to the first newsletter!** You are receiving this because you expressed interest in being kept up-to-date on my adventures in sorting Lego bricks with AI and various contraptions.

I haven't decided on the name yet, but for now, let's go with "AI and Bricks". Let me know if you have a better idea.

## What's been keeping me busy

Ever since I first built my [Lego sorting machine](https://github.com/pbackx/lego-sorter-pi/), I have been annoyed by the complexity of the setup.

To make everything work you need:

* An EV3 hub for controlling the motors
* A Raspberry Pi for the camera
* A desktop or laptop PC as the brains

This presents a number of problems:

* Hardware ages and needs to be maintained. Maintaining many components is costly. For instance, I don't expect that EV3 hubs will be easily available for much longer. Even the much newer Mindstorms Hub is no longer produced (except for the Spike Prime, which is harder to get a hold of).
* Communication between all of those devices can be difficult and is certainly not easy to learn. I did some experiments with the new Mindstorms Hub and the awesome [pybricks](https://pybricks.com/) library. But even with the proper tools, doing communication correctly is hard.
* If you want to train deep learning networks on your own computer, you need some powerful hardware or you will be waiting a long time. Also, the setup is complicated.

All of these have been issues from the start of the project, but at the time, I did not find a good way around them. That was over 3 years ago.

## Fast forward

However, times have changed and I believe there is a proper solution to all the issues now. The only caveat is that it is fairly expensive to get started (more on that at the end of the email).

Recently, there have been some interesting developments with regards to the Raspberry Pi ecosystem:

* A ["Build HAT"](https://www.raspberrypi.com/news/raspberry-pi-build-hat-lego-education/) was released that allows you to directly connect Powered Up components to the Raspberry Pi. It has 4 connectors, which is one too few for my current machine, but I think I can probably work around that limitation. This would remove the need for a Lego hub.
* An ["AI kit"](https://www.raspberrypi.com/products/ai-kit/) is now on sale, making it possible to run deep learning networks on the Raspberry Pi. This kit makes it possible to run existing networks on the Raspberry Pi. The main problem with this one is that it is out-of-stock everywhere. I have been waiting for my order since the beginning of June.

One important thing to know about the AI kit is that it is not possible to do training of the deep learning network on the Raspberry Pi. For that, you still need another solution. One option I am thinking about is [Google Colab](https://colab.research.google.com/), which is completely free for personal use and would be the ideal candidate for people that don't have a powerful computer at home.

The main disadvantage I see with Google Colab is the fact that it is Google, and it could go away at any moment with very little notice upfront.

## Cost

Now about the elephant in the room, what is all of this going to cost?

A Raspberry Pi 5 with Build HAT and AI Kit is going to set you back at least 150 USD/EUR. And that is assuming you can re-use some existing parts you have, like a power supply and the cables you need.

On top of that, if you need to upgrade from EV3 motors and sensors to the new Powered Up ones, this also isn't going to come free. Most recent Technic models that include motors have come with these for the last few years, so you may already have those. As far as I know, no Technic models come with sensors, so that could be a problem.

On the other side, using Colab no longer requires a powerful computer, which could easily save 1000+ USD/EUR.

## Conclusion

While I am a bit hesitant about the cost, I feel this is going to be the way forward for the next update of my machine.

Next month, I should be able to show some initial results of the AI kit (I have been promised it should ship any moment now).

What are your thoughts on the new hardware? Too expensive? Do you have some other things lying around that could be repurposed?