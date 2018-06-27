---
id: 3656
title: PayPal IPN Java AppEngine Servlet Gets an Update
date: 2013-08-23T10:41:48+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3656
permalink: /paypal-ipn-java-appengine-servlet-gets-update/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2013/08/wishes.jpg
categories:
  - Java and JavaScript
---
It&#8217;s has been over 6 months since I last touched my PayPal GAE integration servlet. This means it&#8217;s becoming pretty stable. However it was time to upgrade some of the libraries. Read on for the details.

<!--more-->

After [my major refactoring in August last year](http://www.streamhead.com/paypal-appengine-servlet-now-cloud-ready/), this update might seem minimal, but could break a few things, so be careful:

  * Again the AppEngine dependency was updated to the latest version.
  * Switch to [Google&#8217;s own Maven plugin.](https://developers.google.com/appengine/docs/java/tools/maven) It has finally reached a mature and well maintained state, so I&#8217;m switching all my GAE projects to it.
  * Upgrade to Vaadin 7. Because this is a **breaking upgrade**, I&#8217;ve changed the version to 0.0.2-SNAPSHOT.
  * Added two more transaction types: recurring\_payment\_suspended and recurring\_payment\_suspended\_due\_to\_max\_failed_payment. PayPal sends these to my application, however I can&#8217;t find any documentation on them (However, you can guess what they mean &#8230;)

To make my life easier, I&#8217;m no longer deploying to SonaType&#8217;s snapshot repositories. I just deploy them to my own private [CloudBees](http://www.cloudbees.com/) repository. Let me know if this is important to you.

&nbsp;

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->