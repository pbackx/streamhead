---
id: 2439
title: GWT vs Handcrafted JavaScript
date: 2010-07-23T10:00:23+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2439
permalink: /gwt-vs-handcrafted/
dsq_thread_id:
  - "120607338"
image: /wp-content/uploads/2010/07/tuning.png
categories:
  - Java and JavaScript
---
It&#8217;s something I&#8217;d been wondering for a while: how does GWT&#8217;s JavaScript code stack up to code created and optimized by hand? I hadn&#8217;t really seen any exact data, until now.

<!--more-->It&#8217;s the age-old question: are you better to handcraft detailed instructions, or do you just let a compiler handle it for you? Assembler vs C? Write your own memory manager or let the garbage collector do that for you?

And now there&#8217;s generated JavaScript versus rolling your own. I love the simplicity of writing front-end in the same language as your back-end, but what about performance?

Turns out it&#8217;s not too bad. <a title="GWT JS vs handcrafted JavaScript" href="http://flax.ie/google-web-toolkit-javascript-vs-hand-crafted-javascript-benchmark/" target="_blank">Ciaran McCann did some tests</a> and found out only FireFox had some serious troubles running the GWT code. The test isn&#8217;t complete yet, I&#8217;m very interested in the stats for Windows.

**update**: <a title="GWT JS vs handcrafted JavaScript - part 2" href="http://flax.ie/google-web-toolkit-javascript-vs-hand-crafted-javascript-benchmark-part-2/" target="_blank">Ciaran has updated his tests with Windows results</a>. I already knew Chrome was great at executing JavaScript, but it appears it&#8217;s even better at executing GWT generated JavaScript.

(<a title="Tuning Racing VW" href="http://www.flickr.com/photos/willvision/3315214914/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->