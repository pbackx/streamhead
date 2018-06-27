---
id: 2672
title: Powered by Reindeer, Vaadin-Engine Gets a New Name
date: 2010-09-21T10:00:50+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2672
permalink: /powered-by-reindeer/
dsq_thread_id:
  - "144772023"
categories:
  - Java and JavaScript
---
<p class="update">
  <strong>update</strong>: There&#8217;s now <a href="http://www.streamhead.com/vaadin-app-engine-in-5-minutes/">a quick reference card that will get you started with Vaadin and App Engine in 5 minutes</a>
</p>

Last week, I proudly announced the release of <a title="Vaadin Engine, Vaadin, Spring and AppEngine in a web framework" href="http://www.streamhead.com/vaadin-engine-security-release/" target="_blank">Vaadin Engine, a high-level web application framework integrating Vaadin, Spring and Google AppEngine</a>. It seems I didn&#8217;t do my homework right, because the Vaadin guidelines forbid the usage of the Vaadin name in such a way (there probably are a few laws involved too). The Vaadin developers kindly reminded me of this, so it is with no hard feelings that I present the new name: **Powered by Reindeer**, or **POW** for short.

<!--more-->Because it&#8217;s so early in the project, I&#8217;ve also renamed the 

<a title="Powered By Reindeer GitHub repo" href="http://github.com/pbackx/PoweredByReindeer" target="_blank">GitHub repository to PoweredByReindeer</a>. It might inconvenience a few of you, but in the long run it&#8217;s just cleaner. The Java packages have been renamed to com.pow, but I haven&#8217;t yet expanded the functionality. So you&#8217;re basically getting the exact same thing, except in a new package.

If you want to try it out, I&#8217;ve updated <a title="Vaadin Engine, Vaadin, Spring and AppEngine in a web framework" href="http://www.streamhead.com/vaadin-engine-security-release/" target="_blank">the getting started instructions</a>.

One more thing I&#8217;m currently working on is getting the project on a Maven repository. It wouldn&#8217;t be very useful to have a fully Maven-ized project but not being able to use it as a dependency. I could&#8217;ve hosted a private Maven repo on GitHub, but decided to go for the real deal. <a title="Sonatype OSS Maven Repository" href="https://docs.sonatype.org/display/repository/sonatype+oss+maven+repository+usage+guide" target="_blank">Sonatype offers a free Maven repository for OSS</a>. Furthermore it is also possible to automatically republish your project to the Maven central repo. Your project has to comply with a number of guidelines, but I think I&#8217;ll be able to comply once I have a real release.

I should be able to give you the project details shortly, so stay tuned.

<p class="update">
  <strong>update</strong>: There&#8217;s now <a href="http://www.streamhead.com/vaadin-app-engine-in-5-minutes/">a quick reference card that will get you started with Vaadin and App Engine in 5 minutes</a>
</p>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->