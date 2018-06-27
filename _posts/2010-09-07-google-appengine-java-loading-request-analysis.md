---
id: 2602
title: Google AppEngine for Java Loading Request Analysis
date: 2010-09-07T10:00:10+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2602
permalink: /google-appengine-java-loading-request-analysis/
dsq_thread_id:
  - "138534861"
categories:
  - Java and JavaScript
---
I&#8217;ve continued work on my Vaadin example project and am trying to make it reusable for new projects. There&#8217;s already <a title="Vaadin Engine - sample Vaadin project on Google AppEngine" href="http://github.com/pbackx/Vaadin-Engine" target="_blank">some code for the Vaadin on Google AppEngine project on GitHub</a>, but for now it&#8217;s just a &#8220;Hello World&#8221; type application. Before I continued, I wanted to see how performance is affected by the different features I&#8217;m using in this project. Turns out there is a fairly major penalty to be paid on the loading request, but once loaded, applications tend to not be impacted that much.

<!--more-->Before we get started, a small disclaimer: I wouldn&#8217;t want to publish this experiment in a peer-reviewed magazine, but I did my best to create fairly reproducible experiments. I conducted all experiments several times to avoid one-off peaks in the results. At the very least, they should give a good general hint on what might be slowing down an application on Google AppEngine.

For this test, I created the most basic Vaadin application that simply shows a &#8220;Hello World&#8221; label. These are the variants I tested:

  * A Vaadin only version, no Spring at all.
  * A Vaadin only version in which I extracted the Vaadin resources (in the VAADIN folder). This is a suggested practice as otherwise all requests for theme resources have to go through the Vaadin servlet.
  * An application that gets its message from a simple Spring bean. Everything is configured via a Spring xml config file.
  * A similar application, but now the bean is injected via annotations and there is no direct access to the Spring application context in the Vaadin application. <a title="Obtaining Services and Repositories in Vaadin" href="http://www.streamhead.com/services-vaadin/" target="_blank">I explained this technique for obtaining Spring beans in a non-Spring-managed object earlier</a>.
  * Exactly the same application as above, only now I wrapped a Spring Security filter around the entire app. There was no actually user involved as I only used anonymous access. <a title="Spring Security and Vaadin" href="http://www.streamhead.com/spring-security-vaadin/" target="_blank">My Vaadin Spring Security setup is explained in this post</a>.
  * Last but not least, I also tried the very first application with all jar libraries needed by the last application. About halfway through I got the impression that performance was directly proportional to the amount of jar files. So I had to try this out.

As far as response times when the application is fully loaded and active, I noticed virtually no difference between any of the scenarios. The very first version seemed a little slower, but given the number of times I ran the experiments I&#8217;m not going to draw any conclusions. The example only uses one stylesheet and the loading indicator JPG. So I didn&#8217;t expect to see a huge difference anyway.

I was happy with this result. For &#8220;normal&#8221; use of the application, you can use all those fancy Spring features. It won&#8217;t perform worse than on any other application server.

However, when I measured the CPU load for <a title="Google App Engine for Java Loading Request" href="http://www.streamhead.com/app-engine-loading-requests/" target="_blank">loading requests</a>, the story was entirely different. I measured the following times (average of only 3 runs, those take a long while to do):

<img class="alignnone" title="AppEngine Loading Request measurements" src="http://chart.apis.google.com/chart?chxl=1:|minimal+Vaadin+app|resources+unpacked|all+libraries|Spring+injection|Annotation|Spring+Security&chxp=1,5.5,4.5,3.5,2.5,1.5,0.5&chxr=0,6,7500|1,0,6&chxt=x,y&chbh=a&chs=440x220&cht=bhs&chco=4D89F9&chds=0,7500&chd=t:3384,3360,3359,4432,5236,7310&chdl=cpu_ms&chtt=Loading+request" alt="" width="440" height="220" />

I think that chart speaks for itself. Clearly, the more stuff I enabled, the longer the loading request became. The final one takes over 7 seconds, which is worrisome. For a popular application this won&#8217;t matter, but a lot of users might run into it when the application is becoming popular.

Also important: it seems it doesn&#8217;t matter whether superfluous JAR files are present in the lib directory or not. If they are not used, they are not loaded and do not impact the loading request time. So my initial plan to weed through all the dependencies Maven pulled in and remove the ones that weren&#8217;t needed, is useless.

I tried looking for other solutions to speed up the loading request, but it seems there are none except removing libraries (and ease of development). With <a title="Spring adds GWT and Google App Engine integration" href="http://www.springsource.org/node/2595" target="_blank">the recent announcement of App Engine integration in Spring</a>, I expected to find more information on this, but it seems there isn&#8217;t much, apart from a few Roo tutorials. Maybe later?

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->