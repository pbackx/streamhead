---
id: 4
title: 'Multiroom Audio &#038; Video, Can You Afford It?'
date: 2007-12-08T09:59:30+00:00
author: Peter Backx
layout: post
guid: http://streamhead.com/willtell/?p=4
permalink: /multiroom/
Image:
  - http://www.streamhead.com/wp-content/uploads/2007/12/revox.png
dsq_thread_id:
  - "5437718"
amazon_post_template:
  - ""
image: /wp-content/uploads/2007/12/revox.png
categories:
  - Tools
---
A multiroom audio & video system gives you centralized control of your audio and video streams. It (usually) consists of a **central source of all your media** (DVD archive, CD collection, cable box, etc.), a distribution network, **several endpoints** that can consume the media and a way to control what is played on which endpoint. Most systems will cost you an arm and a leg and then some.

<!--more-->(this post was completely overhauled on May 20th 2011)

From expensive to cheap, here&#8217;s a short overview.

## High-end fully integrated systems

<p style="text-align: left;">
  <a title="Revox multiroom options" href="http://www.revox.com/#/multiroom/mr_options"><img class="size-full wp-image-3243 aligncenter" title="revox_resystem_m100" src="http://www.streamhead.com/wp-content/uploads/2007/12/revox_resystem_m100.png" alt="" width="344" height="273" srcset="http://www.streamhead.com/wp-content/uploads/2007/12/revox_resystem_m100.png 344w, http://www.streamhead.com/wp-content/uploads/2007/12/revox_resystem_m100-300x238.png 300w" sizes="(max-width: 344px) 100vw, 344px" />Revox</a> offers some brilliantly designed multiroom systems. They consist of a central system and for every room you need a connected amplifier and, if you like, an in-wall control module. I don&#8217;t know the exact current prices, but last time I checked, the central module is about   €2000 and each additional room will set you back another €700 (and you need to have the wiring ready).
</p>

If you&#8217;re in this range of appliances, also check out [Bang & Olufsen&#8217;s BeoLink](http://www.bang-olufsen.com/home-integration-beolink "BeoLink - Bang & Olufsen"). As far as I can tell by the advertising, it constructs a distributed mesh network between your appliances so they can share media. I&#8217;m sure it won&#8217;t come cheap as you&#8217;re forced to use B&O components only. But just like the Revox stuff it looks incredibly pretty.

## Semi Affordable Plug and Play Gear

<img class="aligncenter size-full wp-image-3245" title="sonos_zoneplayer_120" src="http://www.streamhead.com/wp-content/uploads/2007/12/sonos_zoneplayer_120.png" alt="" width="510" height="291" srcset="http://www.streamhead.com/wp-content/uploads/2007/12/sonos_zoneplayer_120.png 510w, http://www.streamhead.com/wp-content/uploads/2007/12/sonos_zoneplayer_120-300x171.png 300w" sizes="(max-width: 510px) 100vw, 510px" />

I&#8217;m afraid there aren&#8217;t too many options in this category. If you&#8217;re only looking for an audio solution, [Sonos](http://www.sonos.com/experience/multiroom/Default.aspx?rdr=true&LangType=1033 "Sonos multiroom") is an extremely well designed and well reviewed option. It creates a wireless mesh network between its players. So there&#8217;s no need to run cables and if you already have an iDevice, you can use the app and skip their custom remote.

[The Squeezebox range](http://www.logitech.com/en-us/speakers-audio/wireless-music-systems "Squeezbox wireless music systems") is not as well integrated, but it is more affordable and they have some cool portable devices that you can take with you through the house (or for instance outside on the terrace).

Both the Sonos&#8217;s and Squeezebox&#8217;s are audio only. I couldn&#8217;t find anything in the video department. You might want to set up a uPNP server and check out devices such as [the Western Digital media players](http://www.wdc.com/en/products/homeentertainment/mediaplayers/ "Wester Digital Media Players"), but they are missing many of the properties of a true multiroom system (no centralized control for instance)

## Ghetto Rigging It Yourself

I wish I could say there&#8217;s a free and/or open source solution that allows you to re-purpose old PC hardware, but as far as I know, there isn&#8217;t.

So I&#8217;ve been thinking about creating something myself. I like Boxee because it is a well supported platform that is only going to grow in the future. I came up with the following idea (click to enlarge):

[<img class="aligncenter size-medium wp-image-3246" title="multiroom_concept" src="http://www.streamhead.com/wp-content/uploads/2007/12/multiroom_concept-300x220.png" alt="" width="300" height="220" srcset="http://www.streamhead.com/wp-content/uploads/2007/12/multiroom_concept-300x220.png 300w, http://www.streamhead.com/wp-content/uploads/2007/12/multiroom_concept-1024x753.png 1024w, http://www.streamhead.com/wp-content/uploads/2007/12/multiroom_concept.png 1045w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2007/12/multiroom_concept.png)There are a few issues:

  * I have no idea how to set up the streaming part. I&#8217;m not sure if Boxee can retransmit a live signal. In fact, I doubt it, so I&#8217;ll probably need to look into other solutions. It&#8217;s less important right now, so I&#8217;ll get to that when the time comes.
  * The web interface for remote control does not yet exist. Boxee itself exposes a very limited interface and I haven&#8217;t really found any third party ones. Unless I find something, this is going to be the bulk of the work and will require additional programming: A nice interface that can control multiple Boxee installations.

Has any one attempted a similar setup with cheap components and software? How did it go?

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->