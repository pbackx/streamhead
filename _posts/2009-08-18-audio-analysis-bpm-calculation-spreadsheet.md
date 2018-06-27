---
id: 1499
title: Audio Analysis and BPM Calculation in a Spreadsheet
date: 2009-08-18T10:00:27+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1499
permalink: /audio-analysis-bpm-calculation-spreadsheet/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/08/bpm.png
dsq_thread_id:
  - "30104320"
categories:
  - Music
---
<a title="Audio Analysis Architecture on JLayer" href="http://www.streamhead.com/audio-analysis-jlayer-excel/" target="_blank">Last week I showed the beginnings of my audio analysis program</a>. This week it&#8217;s time to talk about the goals. My final goal is to do BPM calculation on various music sources. It should be fairly fast, but there&#8217;s no need for a realtime readout. I did some Google-ing, but couldn&#8217;t find any freely available Java implementation. So I ended up reinventing the wheel.

I did however look for a little help. <a title="GameDev.net - Beat Detection Algorithms" href="http://www.gamedev.net/reference/articles/article1952.asp" target="_blank">Yov408&#8217;s explanation on GameDev</a> is an exceptionally well tutorial and introduction into beat detection. If you read the article, you&#8217;ll notice that the first thing you need is the energy of the music file. So I added an energy calculating filter to my architecture.

<a title="Post Office" href="http://www.flickr.com/photos/42139271@N00/3809103141/" target="_blank"><img src="http://farm4.static.flickr.com/3476/3809103141_1c2770e049_m.jpg" border="0" alt="Post Office" /></a>
  
<small><a title="Attribution-NonCommercial-NoDerivs License" href="http://creativecommons.org/licenses/by-nc-nd/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="wenzday01" href="http://www.flickr.com/photos/42139271@N00/3809103141/" target="_blank">wenzday01</a></small>

<a title="audio analysis - BPM" href="http://spreadsheets.google.com/ccc?key=0AimAxoLiivAfdGhjNE1VZG12ZGJEQ19samtDanJoZUE&hl=en" target="_blank">See the Google Docs spreadsheet with a visual representation</a>.

Afterward, I wanted to get some insight into the algorithm, so I took some random samples and put them in a spreadsheet. My test song is one with a very very clear beat, so if my beat detection algorithm works on anything, this will be it.

I did have to expand the algorithm a little, to calculate the actual BPM. The document only describes beat detection, but once you got that far, BPM calculation is fairly trivial (just count the beats and divide by the time).

If you open the spreadsheet, you&#8217;ll notice that I got lucky with my first sample. Immediately I calculated a pretty good BPM of the song (it is about 128 BPM), however, when I tried another sample of the same song, the result was completely wrong. But you might notice that if I did not use the adaptive algorithm to calculate the threshold value C.

<a title="audio analysis - BPM" href="http://spreadsheets.google.com/ccc?key=0AimAxoLiivAfdGhjNE1VZG12ZGJEQ19samtDanJoZUE&hl=en" target="_blank">See the Google Docs spreadsheet with a visual representation</a>.

I tried to implement that, and although the theory sounds good, the results were even worse. I&#8217;m pretty sure I need to go over it one more time to figure out the best values for the constants (I have a different input range then the article). But it&#8217;s a start.

Next week, I&#8217;ll try to tune that adaptive algorithm and hopefully publish my code. If you have some experience in BPM calculation, I&#8217;d love to hear what algorithm you used. Because there are as many theories out there as there are people calculating BPM counts.

<a title="THE FATMAN on Flickr" href="http://www.flickr.com/photos/puhatek/3769115283/in/photostream/" target="_blank">Image credit</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->