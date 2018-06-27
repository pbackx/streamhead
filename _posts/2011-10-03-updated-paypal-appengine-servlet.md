---
id: 3322
title: Updated PayPal AppEngine Servlet
date: 2011-10-03T16:00:24+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3322
permalink: /updated-paypal-appengine-servlet/
amazon_post_template:
  - ""
categories:
  - Java and JavaScript
---
If you want to integrate PayPal with your Google AppEngine application, there are a limited number of options available. My own open source project offers a servlet that can parse and log IPN messages. This will quickly get you up and running with [PayPal Payments Standard](https://www.x.com/developers/paypal/development-and-integration-guides#wps "PayPal payments standard guides").

<!--more-->

[Since I launched the PayPal servlet](http://www.streamhead.com/java-paypal-ipn-servlet/ "Java AppEngine PayPal IPN servlet"), I&#8217;ve had many inquiries and I know of at least 2 production deployments of the code. It was about time that I started handling the project a little more professionally.

The first step in this process was completed last weekend: the project is now a Maven project and the Eclipse specific configuration has been removed. I have decided to make this part of my [Powered by Reindeer initiative](http://www.streamhead.com/vaadin-app-engine-in-5-minutes/ "Powered by Reindeer, quick appengine development"). Although it can be used completely independent and will remain so, I believe that there are going to be some nice synergies in the future that I&#8217;ll want to exploit.

My next step will be cleaning up the actual code. I&#8217;m not sure when I&#8217;ll get around to it, but this will involve changing the package names a little to be more in line with the Powered by Reindeer structure. If you think there&#8217;s a good reason to keep the old names, please let me know. Also let me know if you&#8217;d like to get a personal e-mail when the changes will take place.

[See the GitHub page for all details](https://github.com/pbackx/PayPalIPNServlet "Java AppEngine PayPal IPN servlet").

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->