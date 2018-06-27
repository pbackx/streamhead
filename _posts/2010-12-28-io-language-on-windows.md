---
id: 2914
title: Building the Io Language on Windows
date: 2010-12-28T16:00:28+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2914
permalink: /io-language-on-windows/
dsq_thread_id:
  - "198969462"
amazon_post_template:
  - ""
image: /wp-content/uploads/2010/12/io_building_on_windows.png
categories:
  - New Media and the World
---
Trying out new programming languages is fun, building Io on Windows is not. The Io language is developed on Mac OS X and it shows. There are no binary builds and you need a fairly standard *nix based system to compile it. Here are the steps to get Io running on Windows (and why you might want to).

<!--more-->

<p class="update">
  <strong>update</strong> (11/8/2011): If you want to get started right away, <a href="http://iobin.suspended-chord.info/" title="Io Binaries and Installers">there are now up-to-date binaries available</a> so you don&#8217;t need to compile anything (although it&#8217;s a nice exercise)
</p>

If you like to try out new programming languages, there are many options. <a title="io" href="http://www.iolanguage.com/" target="_blank">Io</a> is a language that is certainly different than most of the others. Its prototype nature (everything is an object, no classes) makes you think a little different about many programming issues. And the absence of syntactic sugar is a nice contrast with language such as Ruby.

Unlike many smaller languages, Io can hardly be called experimental at this point. It has been around since 2002 and is in use by a growing group of enthusiasts. The main disadvantage for me was the lack of any kind of Windows support. Now, I absolutely do not hold this against the author (Steve Dekorte). I&#8217;m sure he has much better things to do than support whiny Windows users.

So let me show you how you can get started with Io and Windows (Windows 7 in my case). You&#8217;ll have a working installation that should at least get you acquainted with the language. My current build isn&#8217;t 100% correct. The correctness test failed on deleting directories and I haven&#8217;t really researched the reason why. If deleting directories is important to you, you might need to do a little more work to get started.

I&#8217;m going to assume you know Windows pretty well (adding stuff to your path, using the command prompt). If you don&#8217;t, I don&#8217;t think you&#8217;ll have much fun trying out Io.

## 1. Getting the Tools: MinGW and CMake

I initially tried to build with Cygwin. That didn&#8217;t work out very well because Cygwin includes a GCC that is terribly old. You could try upgrading the GCC but it looks like people have had mixed experiences with this. And really, why bother, MinGW does have a modern GCC.

For MinGW: <a title="Getting Started MinGW" href="http://www.mingw.org/wiki/Getting_Started" target="_blank">follow the getting started instructions</a>. The GUI based installer worked fine for me. Make sure to install GCC and I also added the developer tools (I believe &#8220;make&#8221; is in there, although I&#8217;m not sure). Afterward, add the MinGW bin directory to your path. In my case that was C:\MinGW\bin

Next up is CMake. I didn&#8217;t know about this tool, but it looks like something very useful. It worked great for me. I went with <a title="CMake - Cross Platform Make" href="http://www.cmake.org/cmake/resources/software.html" target="_blank">the Windows installer that can be found on the downloads page</a>.

## 2. Getting the IoLanguage source

Now it&#8217;s about time to get the source for Io. There are two ways. You can <a title="Io Language site" href="http://www.iolanguage.com/" target="_blank">download it from the Io homepage</a> or <a title="GitHub Io" href="https://github.com/stevedekorte/io" target="_blank">get it straight from GitHub</a>. You&#8217;re getting exactly the same thing, so pick whatever you like.

On my local drive, I created a directory C:\Io. And I put all the source files in C:\Io\sources. Next I also added a C:\Io\build directory where I will be building Io in the next steps.

## 3. Configure the build

Start the CMake gui, pick C:\Io\sources as your source directory and C:\Io\build as your build dir. Well duh.

The next step is to **click the &#8220;configure&#8221; button**. This will load the makefiles and scan for variables that need to be filled. But first it will ask you which generator to use. Pick MinGW:

<img class="alignnone size-full wp-image-2915" title="cmake_generator_config" src="http://www.streamhead.com/wp-content/uploads/2010/12/cmake_generator_config.png" alt="" width="500" height="390" srcset="http://www.streamhead.com/wp-content/uploads/2010/12/cmake_generator_config.png 500w, http://www.streamhead.com/wp-content/uploads/2010/12/cmake_generator_config-300x234.png 300w" sizes="(max-width: 500px) 100vw, 500px" />

This will take some time. But you now should see a long list of name &#8211; values. Most of them in red. You&#8217;ll notice that many values were not found. I&#8217;m going to guess this means this functionality will not work. I&#8217;m not yet far enough into my Io experiments to know for sure. So I&#8217;ll probably return to this part later on.

I did change one value: the **CMAKE\_INSTALL\_PREFIX**. This is where Io will be installed. I changed this to C:/Io

After installation, you&#8217;ll have a C:\Io\bin and C:\Io\lib with all binaries installed.

When you&#8217;ve changed the install prefix to your liking. **Click &#8220;configure&#8221; a second time**.

<img class="alignnone size-full wp-image-2916" title="cmake_io_config" src="http://www.streamhead.com/wp-content/uploads/2010/12/cmake_io_config.png" alt="" width="716" height="538" srcset="http://www.streamhead.com/wp-content/uploads/2010/12/cmake_io_config.png 716w, http://www.streamhead.com/wp-content/uploads/2010/12/cmake_io_config-300x225.png 300w" sizes="(max-width: 716px) 100vw, 716px" />

Now **the &#8220;Generate&#8221; button** will be available. If you&#8217;re happy with the configuration, click it. This will generate the MinGW build files in C:\Io\build but it will not yet build Io. That&#8217;s next.

## 4. Building Io

This is the good part, it&#8217;s also probably the easiest:

  * Open a command prompt
  * CD into C:\Io\build
  * Execute **mingw32-make**
  * Wait

If everything went well, you might see a few warnings, but you&#8217;ll have a fully built Io.

Now you can run **mingw32-make install** to install all the files in C:\Io

## 5. Finetuning Io for Windows

There are just a few small changes left to make your life easier:

  * Add C:\Io\bin to your path
  * If you want to run the dynamically linked version of Io, you also need to add C:\Io\lib to your path (I don&#8217;t think there&#8217;s a difference between the two if you don&#8217;t install extra addons)
  * In Windows explorer go to C:\Io\sources\libs\iovm\tests\correctness and double click on run.io. Windows will not know how to open the file, so choose &#8220;select a program from list&#8221;. Next click on Browse and select io.exe. The test should run but will probably give a lot of warnings and (for me) one error when trying to delete the test directories.
  * You can also run from the command line: Open a command prompt, cd to C:\Io\sources and run &#8220;**io libs\iovm\tests\correctness\run.io**&#8220;. You don&#8217;t even need to specify the Io interpreter &#8220;libs\iovm\tests\correctness\run.io&#8221; works too. Oddly enough, those give me different results, I&#8217;m not sure what&#8217;s going on there.

Currently the tests give me the following result:

<pre>C:\Io\sources&gt;io libs\iovm\tests\correctness\run.io
..E...................................E...............................
......................................................................
.....................
 Exception: error removing file 'testDir/testSubDir'
 ---------
 remove                              Directory.io 143
 Directory remove                     [unlabeled] 0
 List mapInPlace                      [unlabeled] 0
 List map                             DirectoryTest.io 124
 Call relayStopStatus                 A4_Exception.io 24
 Call delegateToMethod                A0_List.io 176
 DirectoryTest tearDown               UnitTest.io 74
 Date secondsToRun                    UnitTest.io 65
 Call relayStopStatus                 Date.io 18
 TestRunner run                       UnitTest.io 113
 DirectoryCollector run               run.io 18
 CLI doFile                           Z_CLI.io 140
 CLI run                              IoState_runCLI() 1
</pre>

As far as I can interpret the results, this means there are at least two errors with Io core functionality. At least directory removal doesn&#8217;t work, I&#8217;m unsure what the other error is.

## Help needed

Most of my initial experiments seem to work fine on this build, but clearly there are some issues that still need to be resolved. If you have any tips or ideas, please let me know and I&#8217;ll keep updating the post until we have a proper Windows build for Io.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->