---
id: 145
title: 'Microsoft does the mashup &#8211; howto get started with Popfly'
date: 2008-07-01T10:00:31+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=145
permalink: /microsoft-does-the-mashup-howto-get-started-with-popfly/
dsq_thread_id:
  - "5437925"
categories:
  - Java and JavaScript
---
[<img class="aligncenter size-medium wp-image-146" title="Popfly mashup editor" src="http://www.streamhead.com/wp-content/uploads/2008/06/popfly-300x225.png" alt="" width="300" height="225" srcset="http://www.streamhead.com/wp-content/uploads/2008/06/popfly-300x225.png 300w, http://www.streamhead.com/wp-content/uploads/2008/06/popfly.png 1024w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2008/06/popfly.png)

Note: Microsoft has retired Popfly. It was only a short lived project that never really got traction. Although there were some advantageous over other mashup toolkits (but also disadvantages).

<a title="Microsoft Popfly" href="http://www.popfly.ms/" target="_blank">Microsoft Popfly</a> consists a few components, the latest they added is a game builder that lets you easily create games. But this post is about the mashup editor. If you don&#8217;t yet know what <a title="Mashup on Wikipedia" href="http://en.wikipedia.org/wiki/Mashup_(web_application_hybrid)" target="_blank">a mashup</a> is in the Web 2.0 vocabulary, it is the combination of several web application (Google Maps, del.icio.us, Flickr, etc.) into a new application. The idea is that you use basic building blocks to create a bigger and better application.

There&#8217;s some competition in the area, among others the <a title="Yahoo! pipes experiments" href="http://www.streamhead.com/?p=94" target="_blank">previously mentioned (and approved)</a> <a title="Yahoo! pipes" href="http://pipes.yahoo.com/pipes/" target="_blank">Yahoo! Pipes</a> and Google also has <a title="Google mashup editor" href="http://editor.googlemashups.com/" target="_blank">a mashup editor</a>. Although that last one doesn&#8217;t seem to be too popular. It might be because it doesn&#8217;t offer a graphical interface as the others do.

<div class="alignleft">
  <a title="I Just Dropped In To See What Condition My Condition Was In" href="http://www.flickr.com/photos/87373143@N00/2339721086/" target="_blank"><img src="http://farm3.static.flickr.com/2207/2339721086_5e74b0d743_m.jpg" border="0" alt="I Just Dropped In To See What Condition My Condition Was In" /></a><br /> <small><a title="Attribution License" href="http://creativecommons.org/licenses/by/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="Hryckowian" href="http://www.flickr.com/photos/87373143@N00/2339721086/" target="_blank">Hryckowian</a></small>
</div>

If you know Yahoo! Pipes, you&#8217;ll know what to expect from the Popfly mashup editor. It&#8217;s basically the exact same concept, but with a few twists:

  * You need the **Microsoft Silverlight** plugin to run everything. Overly generalized, Silverlight is the Microsoft version of Adobe&#8217;s Flash or Sun&#8217;s Java applets.
  * It runs **client side**. Data is stored on the server, but the execution is on your computer. The advantage is that it will respond a lot quicker than Yahoo! Pipes. The disadvantage is that you can&#8217;t use your mashup outside of Popfly.
  * You can **customize** **existing** **components** and **create** your own in JavaScript and XAML. This is a major advantage over Pipes. Because everything runs client side, you&#8217;re basically allowed to do anything. You can view the source of any component and change it. Or you can just start from scratch. You can even publish them. Be careful when you use components by others, they might do stuff you don&#8217;t want them to.
  * Usually the mashups are a bit easier compare to Pipes, because you **don&#8217;t need to have a loop** around any of the blocks. They already have looping inside them.

In order to show you how it works, here&#8217;s a little tutorial where I take my list of Recipe Book 2.0 ingredients and try to get a nice Flickr picture for them:

  * [<img class="alignright size-medium wp-image-148" title="flickr options" src="http://www.streamhead.com/wp-content/uploads/2008/06/flickroptions-300x221.png" alt="" width="300" height="221" srcset="http://www.streamhead.com/wp-content/uploads/2008/06/flickroptions-300x221.png 300w, http://www.streamhead.com/wp-content/uploads/2008/06/flickroptions.png 867w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2008/06/flickroptions.png)From the &#8220;News & RSS&#8221; item, click the **RSS block** to create a new instance.
  * Double click on the red cube or select it and click the wrench icon to enter the **options screen**.
  * If you&#8217;re interested in the code behind this block, then click on &#8220;Switch to an advanced view&#8221;. For now take a look and click the button again to go back to the simple view.
  * You want the &#8220;getItems&#8221; operation. Now enter an URL that generates an interesting RSS feed. For instance, I took <a title="RSS feed with a bunch of ingredients" href="http://pipes.yahoo.com/pipes/pipe.run?_id=7Lxs970t3RGOzUHQy6ky6g&_render=rss" target="_blank">the ingredient feed</a> that was used in my <a title="Recipe Book 2.0 prototype" href="http://www.recipebook20.com/" target="_blank">Recipe Book 2.0</a>.
  * Now create a **flickr block** from the &#8220;Images & Video&#8221; menu.
  * **Connect** both blocks: click once on the RSS block and ones on the flickr one. There should be an arrow connecting both.
  * Change the settings of the flickr block to &#8220;getPhotos&#8221;, text to &#8220;rss:title&#8221;, number to &#8220;custom:1&#8221; and sort to &#8220;custom:relevance&#8221;.
  * That&#8217;s it. Click **Run** to see the result.

[<img class="aligncenter size-full wp-image-147" title="Run result" src="http://www.streamhead.com/wp-content/uploads/2008/06/run.png" alt="" width="499" height="260" srcset="http://www.streamhead.com/wp-content/uploads/2008/06/run.png 866w, http://www.streamhead.com/wp-content/uploads/2008/06/run-300x156.png 300w" sizes="(max-width: 499px) 100vw, 499px" />](http://www.streamhead.com/wp-content/uploads/2008/06/run.png)

The major problem remains: you are stuck in the Microsoft ecosystem. There&#8217;s no way to integrate your Popfly mashups in other systems. You can embed a widget on your blog, but that&#8217;s about it. I don&#8217;t think Microsoft did this on purpose, it&#8217;s just the way it works. Maybe there is a way to interact with it via JavaScript, but I haven&#8217;t found it yet. It&#8217;s a bit sad, because Popfly&#8217;s mashup editor has tremendous potential.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->