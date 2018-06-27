---
id: 3314
title: AZERTY Keyboard and jMonkeyEngine Quick Tip
date: 2011-08-31T16:00:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3314
permalink: /azerty-jmonkeyengine/
amazon_post_template:
  - ""
image: /wp-content/uploads/2011/08/jMonkeEngine_showcase.png
categories:
  - Java and JavaScript
tags:
  - jMonkeyEngine
---
If you&#8217;ve ever created anything using jMonkeyEngine&#8217;s SimpleApplication and you use something other than the American standard QWERTY keyboard, you might have had the same frustration as me: Why isn&#8217;t there quick way to switch the keyboard layout? The SimpleApplication base class is supposed to make your life easier, yet there you are, completely stuck with that unnatural keyboard layout. Read on for a quick copy-and-paste solution.

<!--more-->The keyboard mapping that SimpleApplication uses for its camera movement is defined in the FlyByCamera. The mapping is hardcoded and the mapping names don&#8217;t even use constant strings. Clearly, no one ever thought about international users. 

[jMonkeyEngine](http://jmonkeyengine.org/ "jMonkeyEngine.org") does so many things right, yet on this one, it really misses the ball.

Luckily, with a little searching, it&#8217;s fairly easy to redefine the correct mappings. It&#8217;s something I now do in all my experiments.

I just copy and paste the following at the start of every simpleInitApp:

<pre lang="Java">inputManager.deleteMapping("FLYCAM_Forward");
inputManager.deleteMapping("FLYCAM_Lower");
inputManager.deleteMapping("FLYCAM_StrafeLeft");
inputManager.deleteMapping("FLYCAM_Rise");
inputManager.addMapping("FLYCAM_Forward", new KeyTrigger(KeyInput.KEY_Z));
inputManager.addMapping("FLYCAM_Lower", new KeyTrigger(KeyInput.KEY_W));
inputManager.addMapping("FLYCAM_StrafeLeft", new KeyTrigger(KeyInput.KEY_Q));
inputManager.addMapping("FLYCAM_Rise", new KeyTrigger(KeyInput.KEY_A));
inputManager.addListener(flyCam, new String[] {"FLYCAM_Forward", "FLYCAM_Lower", "FLYCAM_StrafeLeft", "FLYCAM_Rise"});
flyCam.setMoveSpeed(10f);</pre>

(Note that I&#8217;ve also sped up the movement to more easily move around)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->