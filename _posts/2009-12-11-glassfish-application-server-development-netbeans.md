---
id: 1707
title: GlassFish Application Server Development with NetBeans
date: 2009-12-11T10:00:36+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1707
permalink: /glassfish-application-server-development-netbeans/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/12/glassfish_logo.png
dsq_thread_id:
  - "51126209"
categories:
  - Java and JavaScript
---
The GlassFish v3 preview offers a glimpse at Java EE 6 and some of the benefits it will bring. <a title="Top reasons for lightweight GlassFish 3" href="http://blogs.sun.com/alexismp/entry/lightweight_glassfish" target="_blank">Fast redeployment</a> alone is worth taking a look at this new server. But Java EE 6 also standardizes many features that make life of a developer a lot easier. Most of those have been available in one way or another in different frameworks and libraries, but it&#8217;s nice to see them integrated into the java standards.

If you download and install the latest <a title="NetBeans" href="http://netbeans.org/" target="_blank">NetBeans 6.7</a> with GlassFish server, you&#8217;ll get a very quick start. Everything is preconfigured and ready to go. There&#8217;s one thing to watch out for though. The package includes GlassFish v3 **Prelude**. This version does not support EJBs and many Java EE technologies. I&#8217;m not entirely sure, but I think it&#8217;s pretty much the EE &#8220;web profile&#8221; (give or take a few features).

If you want everything but the kitchen sink, you need to download GlassFish v3 **Preview**. This is a more recent version of the server and it also allows you to test all EE 6 features. While the download will require a little extra work, luckily, you can easily integrate it into NetBeans and have all the great debug features.

Just add a server from the Tools menu:

[<img class="alignnone size-medium wp-image-1708" title="adding_glassfish_v3_preview_to_netbeans" src="http://www.streamhead.com/wp-content/uploads/2009/12/adding_glassfish_v3_preview_to_netbeans-300x185.png" alt="adding_glassfish_v3_preview_to_netbeans" width="300" height="185" srcset="http://www.streamhead.com/wp-content/uploads/2009/12/adding_glassfish_v3_preview_to_netbeans-300x185.png 300w, http://www.streamhead.com/wp-content/uploads/2009/12/adding_glassfish_v3_preview_to_netbeans-1024x632.png 1024w, http://www.streamhead.com/wp-content/uploads/2009/12/adding_glassfish_v3_preview_to_netbeans.png 1162w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2009/12/adding_glassfish_v3_preview_to_netbeans.png)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->