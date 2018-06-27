---
id: 479
title: Remember Java Applets?
date: 2008-11-11T10:00:21+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=479
permalink: /remember-java-applets/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/11/appletloading.png
dsq_thread_id:
  - "6531793"
image: /wp-content/uploads/2008/11/appletloading.png
categories:
  - Java and JavaScript
---
This was originally a proposal for <a title="Quickies - Devoxx08" href="http://www.devoxx.com/display/JV08/Quickies" target="_blank">a Devoxx quickie</a> (Devoxx was formerly known as JavaPolis), but it did not get accepted. I don&#8217;t know why, but looking over the list of accepted quickies, I think they were looking for more hands-on things. In one or more follow up posts, I&#8217;ll be adding some examples and practical tips. So stay tuned.

## Remember Java applets?

Remember Java applets? The kind of Java that runs inside your browser. You might remember them from such useful features as blocking the browser while loading the VM, news tickers and wavy water effects.

<!--more-->They were launched in the nineties, they had their 15 minutes of fame and then Flash took over. Now, in almost any comparison of RIA toolkits, they are simply forgotten. Replaced by Flex, Silverlight, GWT and Java&#8217;s ugly stepbrother JavaScript. But if you take a closer look, what&#8217;s really the reason no one is using them?

The JRE after all, has **a large install base**, maybe not as large as Flash. But in many cases a JRE comes **preloaded** with your browser, unlike Flash. And it does use the **Java language**, not some kind of scripting derivate that looks like it, but not quite is. Java probably has **the largest developer community** of any language, so what&#8217;s keeping those people from trying out their hand at applets?

<div style="float:right;">
  <a title="VIDEO GAME CHAMPION WIN" href="http://www.flickr.com/photos/70285332@N00/2992817483/" target="_blank"><img src="http://farm4.static.flickr.com/3155/2992817483_bcce38e60e_m.jpg" border="0" alt="VIDEO GAME CHAMPION WIN" /></a><br /> <small><a title="Attribution-ShareAlike License" href="http://creativecommons.org/licenses/by-sa/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="Torley" href="http://www.flickr.com/photos/70285332@N00/2992817483/" target="_blank">Torley</a></small>
</div>

There is one niche, where Java applets seem to do well. But many enterprise developers seem too easily to forget about it: **games** and anything graphically intensive. Think of all the cool <a title="Processing" href="http://processing.org/" target="_blank">Processing</a> <a title="wordscapes by peter cho" href="http://www.typotopo.com/wordscapes/wordscapes.html" target="_blank">applets</a> out there. Java applets can directly access the underlying hardware. It&#8217;s not always easy, but the hard work has already been done for you. For instance, take a look at <a title="lwjgl:tutorials:applet-lwjglinstaller" href="http://lwjgl.org/wiki/doku.php/lwjgl/tutorials/applet-lwjglinstaller" target="_blank">LWJGL and its applet installer</a>. So you have **hardware accelerated 3D** out of the box. It&#8217;s not that Flash 3D frameworks are bad, they are in fact marvelous examples of engineering and getting the most out of the browser. But they are fighting a losing battle compared to hardware acceleration (I must admit, with version 10, <a title="gskinner.com: gBlog: Simple Flash Player 10 3D Demo" href="http://www.gskinner.com/blog/archives/2008/10/simple_flash_pl.html" target="_blank">Flash is catching up</a>).

So what&#8217;s keeping people from trying out applets for more general applications?

<div style="float:left">
  <a title="Question mark" href="http://www.flickr.com/photos/29638083@N00/2981195093/" target="_blank"><img src="http://farm4.static.flickr.com/3296/2981195093_a1c3b329ff_m.jpg" border="0" alt="Question mark" /></a><br /> <small><a title="Attribution License" href="http://creativecommons.org/licenses/by/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="lrargerich" href="http://www.flickr.com/photos/29638083@N00/2981195093/" target="_blank">lrargerich</a></small>
</div>

Could it be **version conflicts**? Possibly, but a little ingenuity and certainly the new <a title="Java SE 6 Update 10" href="http://java.sun.com/javase/6/6u10faq.jsp" target="_blank">Java Deployment Toolkit</a> will solve, or at least circumvent, the problem.

Could it be the **lack of a design tool**? Who knows, but I was always told real developers don&#8217;t use GUIs. It could help, and <a title="JavaFX" href="http://www.sun.com/software/javafx/" target="_blank">JavaFX</a> already goes a long way in simplifying the programmatic definition of interfaces.

Could it be the **lack of frameworks**? It could be, a decent framework to ease development has never done any technology harm.

But I don&#8217;t think it&#8217;s any of those, I believe it&#8217;s mostly the lack of “**coolness**”. The “**hip factor**” is missing. When did you see a high profile website or prolific author evangelize the use of Java applets? I thought so. There&#8217;s <a title="James Weaver's JavaFX Blog" href="http://learnjavafx.typepad.com/weblog/" target="_blank">one great blog</a>, and that&#8217;s about it.

What we need are guys like <a title="Filthy Rich clients" href="http://filthyrichclients.org/" target="_blank">Romain Guy and Chet Haase</a> doing filthy rich Java applets. What we could use is a high profile project using applets.

We need a Google Analytics entirely build on Java. It certainly would be a lot more responsive than the current mix of Flash, JavaScript, server-side rendering and some other miscellaneous ideas. We need a fancy eBay applet with lots of funky animations. Or why not a JavaFX version of <a title="Parleys" href="http://www.parleys.com/display/PARLEYS/Home" target="_blank">Parleys</a>?

So, who&#8217;s up for a challenge and wants to help out and develop a killer JavaFX applet?

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->