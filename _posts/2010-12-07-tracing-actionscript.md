---
id: 2864
title: Three Ways to Trace in ActionScript 3
date: 2010-12-07T16:00:25+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2864
permalink: /tracing-actionscript/
dsq_thread_id:
  - "186373403"
image: /wp-content/uploads/2010/12/actionscript_tracing.png
categories:
  - Flash and ActionScript
---
It&#8217;s been a while since I mentioned the all important discipline of tracing in ActionScript to get an inside look at what your application is doing. Getting feedback from your program at important points can mean the difference between hours of debugging and a quick analysis of the issue at hand. <a title="Quick tip: ActionScript trace statement" href="http://www.streamhead.com/quick-tip-actionscript-trace-statements/" target="_blank">Previously there was the FDTracer plugin</a>, but this is no longer needed. There are actually three much better ways that suite different situations.

<!--more-->Outputting information to a debug log can help you tremendously when struggling with annoying problems. Depending on the situation, there are a few options you can try out.

<a title="ActionScript tracing FlashDevelop example project" href="http://www.streamhead.com/wp-content/uploads/2010/12/ASTracing.zip" target="_blank">You might want to follow along in this FlashDevelop project</a>.

## Plain old trace()

ActionScript  already has a trace statement. It&#8217;s probably not so well known because you need to have the right Flash player for this to work. You either need to use the standalone player or the debug player. If you&#8217;ve <a title="Setting up FlashDevelop to embed images" href="http://www.streamhead.com/embedding-images/" target="_blank">installed FlashDevelop correctly</a>, you should be fine. Keep in mind that an automatic Flash upgrade might have replaced your manually installed debug vesion.

## FlashDevelop&#8217;s FlashConnect

If you&#8217;re developing with FlashDevelop, you can also use the build-in org.flashdevelop.utils.FlashConnect. The FlashConnect.trace directive connects to your running FlashDevelop instance and sends trace information directly to the console. If you have a Flash debug player installed this looks exactly like the previous statement.

It is useful if you don&#8217;t have a debug player, because it will work with any Flash player.

## Firebug tracing

Both of the above options won&#8217;t be very handy when you are developing for the web. You can try to <a title="Flash log file" href="http://livedocs.adobe.com/flex/3/html/help.html?content=logging_04.html" target="_blank">find your Flash log file</a>, but wouldn&#8217;t is be much easier to see trace information directly in our favorite web debugging tool, Firebug?

It&#8217;s actually possible and fairly easy to get trace output to Firebug:

<pre lang="actionscript">ExternalInterface.call("console.log", "tracing in firebug");</pre>

That&#8217;s all there is to it. Keep in mind that, due to security restrictions, this will only work when you deploy the Flash file to a remote server and use swfobject.js to start the program. FlashDevelop creates this configuration by default for you.

<a title="ActionScript tracing FlashDevelop example project" href="../wp-content/uploads/2010/12/ASTracing.zip" target="_blank">FlashDevelop example project<br /> </a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->