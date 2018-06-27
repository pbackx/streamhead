---
id: 2728
title: Google Analytics and Vaadin
date: 2010-10-22T10:00:46+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2728
permalink: /google-analytics-and-vaadin/
dsq_thread_id:
  - "160161908"
categories:
  - Java and JavaScript
---
Whether you think about it from the start or not, every web application needs some kind of user monitoring. Questions such as &#8220;Do users have trouble registering?&#8221;, &#8220;Why don&#8217;t they buy product x?&#8221; need clear answers in order to move your site forward. A typical Vaadin application can not be used with some of the most popular web site analytics tools such as Google Analytics. A Vaadin application runs on one page, so it&#8217;s impossible to track users in the &#8220;old-fashioned&#8221; way.

There is however a user friendly Vaadin component that allows you to track user actions. It&#8217;s called <a title="GoogleAnalyticsTracker add-on for Vaadin" href="http://vaadin.com/addon/googleanalyticstracker" target="_blank">GoogleAnalyticsTracker</a> and this post goes into an important issue you might face when you try it out.

<!--more-->As you might have noticed, this week is Vaadin week on Streamhead.

If you follow the instructions that come with the add on, you already know everything you need to know. Instantiate the tracker and call the measurement function whenever you want to log an action.

That&#8217;s all good and well, but it won&#8217;t work locally. It took me a while (too long) to figure out, but it turns out the Google Analytics JavaScript code verifies the domain you give the tracker with the actual domain the site runs on.

On localhost, this doesn&#8217;t work.

You can enter &#8220;none&#8221; as a host though, this will allow you to see the analytics request and verify everything is working as expected. So you might want to write a small helper function to set the correct domain. Something like this:

<pre lang="Java">new GoogleAnalyticsTracker("UA-XXXXXXXX-1", getDomain());
...
private String getDomain() {
        final URL url = getURL();
        if(url == null)
                return "none";
        final String host = url.getHost();
        if(host == null)
                return "none";
        return host.contains("mydomain.com") ? "mydomain.com" : "none";
}
</pre>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->