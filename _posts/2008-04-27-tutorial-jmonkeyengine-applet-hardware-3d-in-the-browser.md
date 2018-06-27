---
id: 91
title: 'Tutorial: jMonkeyEngine applet – hardware 3D in the browser'
date: 2008-04-27T23:57:30+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=91
permalink: /tutorial-jmonkeyengine-applet-hardware-3d-in-the-browser/
dsq_thread_id:
  - "5437871"
amazon_post_template:
  - ""
image: /wp-content/uploads/2008/04/jmecube.png
categories:
  - Java and JavaScript
tags:
  - jMonkeyEngine
---
Before I continue any Sandy3D or Flash tutorials, I&#8217;d like to go into another method of getting multimedia content in the browser: **Java applets**. One major advantage of applets is the possibility to use hardware acceleration inside the browser. This will tremendously increase the capabilities, quality and speed of the displayed pictures. None of the Flash 3D engines even come close.

As always, there is a drawback. Access to hardware requires more security privileges and is operating system dependant. Java solves a little, but at some point you need to go to the hardware. Enter <a href="http://www.lwjgl.org/" target="_blank">Lightweight Gaming Library (LWJGL)</a>. It allows crossplatform access to the OpenGL library. Combine this with some of the Java security features and you&#8217;ve got a winner.

If you click on the image above, a new window should open that loads the applet. After everything&#8217;s done loading, you should get a security warning. I haven&#8217;t paid for a certificate, so you will have to trust me that the applet won&#8217;t mess with your system. Let me know if you see any errors. If you get a red cross, right click and open the Java console. I&#8217;m very interested in seeing how well everything performs across different browsers and OS&#8217;s.

OpenGL is still pretty lowlevel so to make things a little easier, I&#8217;ve added <a href="http://www.jmonkeyengine.com/" target="_blank">jMonkeyEngine</a> into the mix. At the core jME is a scenegraph based 3D engine, but it adds many more libraries that are useful for 3D and game development, such as the physics library.

jME already has <a href="http://www.jmonkeyengine.com/wiki/doku.php?id=writing_a_jme_applet" target="_blank">a nice tutorial on the WIKI</a>, however there are a few things mising. If you want to get the tutorial running, you can just follow along with the example right until you&#8217;ve build the example and packaged it into a jar file (using a IDE like <a href="http://www.netbeans.org" target="_blank">NetBeans</a> or <a href="http://www.eclipse.org/" target="_blank">Eclipse</a> will make this very easy). Now lets assume you have the jar file with your applet class. Copy it into your &#8216;release&#8217; directory. This is the directory you will upload to your site. To get it running, you need a few libraries (most of these you probably already have downloaded during the development of the applet):

  * <a href="https://sourceforge.net/project/showfiles.php?group_id=58488" target="_blank">LWJGL applet libraries</a>: From that link, download from release 1.1.4, the file **lwjgl_applet-1.1.4.zip**. Unzip it and copy **lwjgl.jar**, **lwjg\_applet\_util.jar** and **natives.jar** into your release directory.
  * <a href="https://jme.dev.java.net/servlets/ProjectDocumentList?folderID=418&expandFolder=418&folderID=0" target="_blank">JME libraries</a>: Download and unzip version 1.0 and copy **jme.jar** and **jme-awt.jar** in the directory.
  * <a href="https://jme.dev.java.net/servlets/ProjectDocumentList?folderID=148&expandFolder=148&folderID=418" target="_blank">JME test libraries</a> (give you easy access to a few images and objects): Again get version 1.0 and copy **jmetest.jar** and **jmetest-data-images.jar** into the directory.

Because jME needs to access the texture file, the applet needs to be signed. LWJGL is alrady signed, so no problem, however, the jar file you created yourself also needs to be signed. Open a command prompt window:

  * If you don&#8217;t have a certificate, create one:  **keytool -genkey -alias key_name**
  * Change to the path where the jar file is located
  * Sign the file: **jarsigner my\_jar.jar key\_name**

Now you can go ahead and create the **index.html**. You can take the one from the tutorial, however, you need to add a few libraries to the &#8220;archives&#8221; parameter. Make sure all jar files mentioned above are referenced:

**archive=&#8221;lwjgl\_util\_applet.jar,lwjgl.jar,natives.jar,jme.jar,jme-awt.jar,jmetest.jar,jmetest-data-images.jar,my_jar.jar&#8221;**

And that should do it. Load the index page in your browser to see the result. Here&#8217;s a screenshot of what you should see:

[<img class="alignnone size-thumbnail wp-image-93" title="jME in a browser" src="http://www.streamhead.com/wp-content/uploads/2008/04/jmerunning-150x150.png" alt="" width="150" height="150" />](http://www.streamhead.com/wp-content/uploads/2008/04/jmerunning.png)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->