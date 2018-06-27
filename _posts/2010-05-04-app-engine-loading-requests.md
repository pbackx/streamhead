---
id: 2251
title: Google App Engine for Java Loading Requests
date: 2010-05-04T10:00:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2251
permalink: /app-engine-loading-requests/
dsq_thread_id:
  - "92084707"
image: /wp-content/uploads/2010/05/triple_nine_clock.png
categories:
  - Java and JavaScript
---
If you&#8217;ve been programming Java on Google App Engine, you&#8217;ll encounter them sooner rather than later: <a title="Google App Engine for Java Questions" href="http://code.google.com/appengine/kb/java.html#What_Is_A_Loading_Request" target="_blank">the loading request</a>. A loading request to your application is a request that forces an initialization of the environment that runs your application. Depending on your application, the libraries you use, the size and the usage a loading request can take a long long time (over 20 seconds) and happen frequently. It&#8217;s something to be aware of. But what to do about them?

<!--more-->Loading requests happen more often when your application isn&#8217;t used very frequently. This seems logical: Keep an application in memory only if the chance is high that it will be used again in the very near future. In practice this means an application is swapped out after only a few minutes of inactivity.

If you&#8217;re application is fairly new with few users, there&#8217;s really no way around it: you have to either reduce the loading time or work around it.

## Reducing loading time

Improving the time that loading requests will quickly lead you to <a title="Google App Engine Cold Start Guide for Java" href="http://www.answercow.com/2010/03/google-app-engine-cold-start-guide-for.html" target="_blank">this blog post</a> and its sobering conclusion: your best bet for huge gains is to get rid of as many libraries as possible, especially the larger ones.

I haven&#8217;t tried it yet, but I fear <a title="New Java Features Enable Domain-Driven Design" href="http://www.streamhead.com/java-features-enable-domain-driven-design/" target="_blank">my fancy architecture based on annotation driven Spring configuration and aspects </a>isn&#8217;t going to be the best performer. For now, I don&#8217;t want to give up on the great flexibility and clean separation of concern it gives me.

There&#8217;s also a trick to avoid loading requests altogether by repeatedly pinging your application. <a title="Tragedy of the Commons and Cold Starts" href="http://groups.google.com/group/google-appengine/browse_thread/thread/22692895421825cb/" target="_blank">However, according to this thread it is frowned upon and might even result in a ban if you overdo it</a>.

## Working around the loading request

So I ended up trying to work around the loading time. For now I&#8217;ve placed a static HTML file on another domain, which shows a nice loading message and does a JavaScript redirect to my actual application. It&#8217;s ugly but I do happen to have to separate domains for now (a landing page and a beta domain), so I&#8217;m ok with it for the time being.

At first I thought you&#8217;d need to domains to make this work (one with the static files, one with the Google App Engine application), but it turns out that&#8217;s not necessary. Also from the thread mentioned above:

&#8220;Google App Engine already serves static resources without intervening requests to application VMs. This means that, for example, you could serve a page that was entirely static content, with a small amount of JS to ping your VM with an asynchronous dynamic request to wake it up. That page would be served instantly to the user. You need to ensure though, that the resources are indeed specified as static content in your app.yaml or appengine-web.xml.&#8221;

In fact, <a title="Using Static Files - Google App Engine Java" href="http://code.google.com/appengine/docs/java/gettingstarted/staticfiles.html" target="_blank">all files except JSP and everything in WEB-INF is served statically</a>.

Feel free to share more tips in the comments.

(<a title="triple nine clock" href="http://www.flickr.com/photos/lwr/1378672867/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->