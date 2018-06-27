---
id: 8
title: Learn to Use DosBox in Space
date: 2007-12-15T11:41:57+00:00
author: Peter Backx
layout: post
guid: http://streamhead.com/willtell/?p=8
permalink: /dosbox-tutorial/
dsq_thread_id:
  - "5437728"
amazon_post_template:
  - ""
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2007/12/using_dosbox_tutorial.png
categories:
  - Tools
tags:
  - dosbox
---
## Introduction

[DOSBox](http://www.dosbox.com/ "DOSBox, an x86 emulator with DOS") is one of the greatest open source tools out there. It emulates an x86 computer, including the DOS operating system with all its very peculiar memory management options and various hardware configurations. It transports you back into time. When Personal Computers where not for the faint of heart. Playing the latest games involved messy configuration and hours of experimentation to get games to run correctly on your particular piece of hardware. And then Windows 95 came, and most of those old games just stopped working entirely.<figure id="attachment_7" style="width: 320px" class="wp-caption alignright">

<img class="size-full wp-image-7" title="wc4" src="http://www.streamhead.com/wp-content/uploads/2007/12/dosboxtutorial.png" alt="The price of freedom is eternal vigilance" width="320" height="240" /><figcaption class="wp-caption-text">The price of freedom is eternal vigilance</figcaption></figure> 

If you thought that old software was lost to the ages, DOSBox is here to save the day. It emulates all those DOS peculiarities. And it does this surprisingly well. Obviously, you need a computer that&#8217;s a hundred times more powerful than the one you originally played the game on. But don&#8217;t worry, most computers these days will suffice for even the most advanced 3D game of those heydays.

The trouble though, for those who have never had the joy of working in DOS or who have never seen a command line, is that a prompt can be a great source of mystery. There are a bunch of frontends available that make it easier to work with DOSBox. But if you&#8217;re interested in old technology, it&#8217;s really worth it to learn the basics of DOS.

To get you started this is what the prompt looks like (you might need to click on the image to get a clear view):

[![the command prompt](http://streamhead.com/wp-content/uploads/2007/12/dosbox_000.thumbnail.png)](http://streamhead.com/wp-content/uploads/2007/12/dosbox_000.png "the command prompt")

But lets not get ahead of ourselves. Here&#8217;s the entire tutorial of how to get that game you&#8217;ve always wanted to play, working on your machine. This tutorial is Windows centric, but DosBox runs on pretty much any operating system, so it should be useful for every one.

## Get and install DOSBox

This is the easy party, go to [the DOSBox download](http://www.dosbox.com/download.php?main=1 "download DOSBox") site and pick your flavor. Once the file is downloaded, install the program. In the case of Windows, you&#8217;ll have yourself an executable that can be double clicked to get the installation started.

Easy as pie.

<img class="alignnone size-full wp-image-3236" title="3455-wing-commander-iv-the-price-of-freedom-dos-screenshot-the-flight" src="http://www.streamhead.com/wp-content/uploads/2007/12/3455-wing-commander-iv-the-price-of-freedom-dos-screenshot-the-flight.jpg" alt="" width="640" height="480" srcset="http://www.streamhead.com/wp-content/uploads/2007/12/3455-wing-commander-iv-the-price-of-freedom-dos-screenshot-the-flight.jpg 640w, http://www.streamhead.com/wp-content/uploads/2007/12/3455-wing-commander-iv-the-price-of-freedom-dos-screenshot-the-flight-300x225.jpg 300w" sizes="(max-width: 640px) 100vw, 640px" />

## Basic setup (don&#8217;t worry it&#8217;s not rocket science)

To focus the thoughts, I&#8217;ll be showing how to get [Wing Commander IV](http://www.mobygames.com/game/wing-commander-iv-the-price-of-freedom "Wing Commander IV: The Price of Freedom") (WC4 from now on) running. The process will be the same for any game that comes on a CD.

First, you&#8217;ll want to write down the following information:

  * Put the game disc in a CD drive and make a note of the drive letter. If the game is somewhere on your harddrive, make a note of the entire directory name (so, starting with the drive letter, and all the way up)
  * Not strictly necessary, but if you like to keep your files tidy, it&#8217;s a good idea to create a directory which will be your virtual hard drive within DOSBox. This drive will hold all game related files such as savegames and configuration. You can just mount your entire drive, but it&#8217;s lot neater if you create a directory. Write down the name and location of that directory too.

As for my example, theWC4 game is on a CD in drive I, DosBox is installed on drive H and I&#8217;ve created a directory inside the DosBox installation:

[![setup](http://streamhead.com/wp-content/uploads/2007/12/dir.thumbnail.png)](http://streamhead.com/wp-content/uploads/2007/12/dir.png "setup")

(note that there is already a directory &#8220;WC4&#8221; created on a previous run of the application, you don&#8217;t need to create that one)

## Start DOSBox

If the installation did go right, this will be the easiest step. Find DosBox in the menu and execute it. You should see the startup screen:

[![DosBox startup](http://streamhead.com/wp-content/uploads/2007/12/dosbox_001.thumbnail.png)](http://streamhead.com/wp-content/uploads/2007/12/dosbox_001.png "DosBox startup")

Possibly, a second screen will have opened, depending on the startup option you choose (noconsole version or not). At any time, you can switch between full-screen and windowed mode by pressing alt-enter. Keep the screen windowed for now, but once a game is running, you probably want to switch.

## Mount the drives

DOSBox creates a virtual file system. A file system, like the thing you see in explorer, but one that only exists within the DOSBox program. By default, there is only a Z drive present, which is used for booting DOSBox and which has some tools present. Don&#8217;t worry about those for now.

The first thing we need to do now, is let DOSBox know which drives and directories we want to use. Let&#8217;s create 2 virtual drives. One C drive, which points to the empty directory we created in the previous step. And a D drive, which points to the CD drive where the game is.

Type in the following to mount the C drive:

<pre>mount C &lt;your C directory&gt;</pre>

Replace <your C directory> with the directory you created in step 2. In my case that would be:

<pre>mount C H:\_games\DOSBox-0.72\cdrive</pre>

You should receive a message that the directory was mounted. One important note: if you have a directory that contains a space, you have to put quotes around it. Eg:

<pre>mount C "C:\My documents\My C drive"</pre>

In general, DOS cannot deal with spaces in directory names very well. So try to avoid them completely inside DOSBox.

Next it&#8217;s time to mount the CD drive. To make sure DOSBox know this is a CD-ROM drive, you need to add an extra parameter:

<pre>mount D D:\ -t cdrom</pre>

In case the game is on your hard drive, you can skip the parameter:

<pre>mount D E:\mygame</pre>

This will probably be enough for most games, but if it&#8217;s not, try the &#8220;intro&#8221; command. Also take a look at the dosbox website if the game is supported and if you need special options. And you can always ask me, I like a challenge.

## Start the game

This is the trickiest part, because every game is different. In case of Wing Commander IV, I just had to switch to the D drive by typing:

<pre>D:</pre>

And start the game. For WC4 you just type:

<pre>WC4</pre>

If you don&#8217;t know the exact command, try to look in the manual, or execute &#8220;dir&#8221;. This will produce a list of files on the disc. All file names will be maximum 8 characters, a dot and another 3 characters. The ones that end in &#8220;.exe&#8221;, &#8220;.com&#8221; or &#8220;.bat&#8221; can be executed by typing the name of that file. Try a few of those and see what happens. Usually there&#8217;s an INSTALL or SETUP one that will configure the game and there&#8217;s one that resembles the name of the game to start it.

Enjoy the game!

## Screencast

[I recently added a new and improved screencast on YouTube, explaining most of what is in this article.](http://youtu.be/W9VB75N9bfs "DOSBox CDROM tutorial")

<img class="alignnone size-full wp-image-3237" title="98734-wing-commander-iv-the-price-of-freedom-dos-screenshot-flying" src="http://www.streamhead.com/wp-content/uploads/2007/12/98734-wing-commander-iv-the-price-of-freedom-dos-screenshot-flying.jpg" alt="" width="640" height="480" srcset="http://www.streamhead.com/wp-content/uploads/2007/12/98734-wing-commander-iv-the-price-of-freedom-dos-screenshot-flying.jpg 640w, http://www.streamhead.com/wp-content/uploads/2007/12/98734-wing-commander-iv-the-price-of-freedom-dos-screenshot-flying-300x225.jpg 300w" sizes="(max-width: 640px) 100vw, 640px" />

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->