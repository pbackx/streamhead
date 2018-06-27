---
id: 1512
title: Easy BPM Calculation in Java
date: 2009-08-25T10:00:22+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1512
permalink: /easy-bpm-calculation-in-java/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/08/waveform.png
dsq_thread_id:
  - "31014913"
categories:
  - Java and JavaScript
---
<a title="Audio Analysis and BPM Calculation in a Spreadsheet" href="http://www.streamhead.com/audio-analysis-bpm-calculation-spreadsheet/" target="_blank">After last weeks mixed success</a>, I started implementing the more advanced techniques <a title="GameDev.net - Beat Detection Algorithms" href="http://www.gamedev.net/reference/articles/article1952.asp" target="_blank">Yov408 describes in his article</a>. However, nothing seemed to improve the calculated beats per minute. I was about to go and implement the Fourier Transform, something which I wanted to avoid in order to keep the algorithm zippy. But I went back to <a title="audio analysis - BPM" href="http://spreadsheets.google.com/ccc?key=0AimAxoLiivAfdGhjNE1VZG12ZGJEQ19samtDanJoZUE&hl=en" target="_blank">the spreadsheet</a> and discovered a much simpler solution.

<a title="BeatIt 0.1 NetBeans project" href="http://www.streamhead.com/wp-content/uploads/2009/08/BeatIt_v0.1.zip" target="_blank"><img title="download" src="../wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />Download the NetBeans example project</a>

The second sample I tried has about 3 or 4 beats too much. Upon closer inspection of those misses, those are all instances where the energy went above the threshold during for only one sample.

Once I understood the nature of the problem, it was easy to implement a solution that only detects a beat when the energy is high enough for a few more samples. I put this into code and was amazed by the results. Pretty much any song I used resulted in a BPM count withing 5 BPM of the actual count.

The adapted algorithm is:

**Every 1024 samples:**

  * Compute the instant sound energy &#8216;e&#8217; on the 1024 new sample values taken in (an) and (bn) using the formula **(R1)**
  * Compute the average local energy <E> with (E) sound energy history buffer: <p align="center">
      <img src="http://www.gamedev.net/reference/programming/features/beatdetection/formula3.png" border="0" alt="" width="173" height="53" /><br /> (R3)</li> 
      
      <li>
        Shift the sound energy history buffer (E) of 1 index to the right. We make room for the new energy value and flush the oldest.
      </li>
      <li>
        Pile in the new energy value &#8216;e&#8217; at E[0].
      </li>
      <li>
        <em>If &#8216;e&#8217; > &#8216;C*<E>&#8217; we detect a possible beat. If a possible beat was not detected in the previous calculation, we start counting, N = 0.  Otherwise, N is increased by one.</em>
      </li>
      <li>
        <em>If N equals a threshold (3 is a pretty good value),  a true beat is detected.</em>
      </li></ul> 
      
      <p>
        Given the simplicity of the algorithm I think this is an incredible result and good enough to move into the next step of the project: Porting this to small devices.
      </p>
      
      <p>
        To be continued &#8230;
      </p>
      
      <p>
        <a title="BeatIt 0.1 NetBeans project" href="../wp-content/uploads/2009/08/BeatIt_v0.1.zip" target="_blank"><img title="download" src="../wp-content/uploads/2008/11/download.png" alt="download" width="30" height="24" />Download the NetBeans example project</a>
      </p>
      
      <p>
        BTW for those following along via e-mail or the RSS feed, <a title="Streamhead - new media analysis and trials" href="http://www.streamhead.com" target="_blank">come visit the site and let me know what you think of the new logo</a>.
      </p>
      
      <p>
        <a title="#3 in the Fading Waveform Series" href="http://www.flickr.com/photos/collinmel/2118785753/" target="_blank">Image credit</a>
      </p>
      
      <!-- AddThis Advanced Settings generic via filter on the_content -->
      
      <!-- AddThis Share Buttons generic via filter on the_content -->