---
id: 3547
title: 'My First Android App Now Available: Discogs Scan'
date: 2012-08-06T17:54:17+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3547
permalink: /discogs-scan/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2012/08/discogs_scan.png
categories:
  - Java and JavaScript
tags:
  - android
---
After last weeks review of [Android in Action](http://www.streamhead.com/android-in-action-second-edition-review/ "Android in Action second edition review"), it was inevitable: I just released [my first Android app: Discogs Scan](https://play.google.com/store/apps/details?id=com.peated.discogs.scan "Discogs Scan in the Play store"). Discogs Scan is a small Android 2.1+ application that allows you to quickly scan the barcodes of all your CDs and records and add it to your discogs.com collection.

<!--more-->

It&#8217;s my first endeavor into mobile apps and I immediately got hit by some device specific bugs. After a round of debugging I think the application is now fairly stable and ready for general usage.

## Discogs Scan

The application itself allows you to quickly scan all your CDs and vinyl. It uses the [discogs.com](https://www.discogs.com/) database to find all the details. Once everything is scanned, you can upload it to your personal discogs.com collection, where you can organize it as you see fit.

In my own experiments it has a hitrate of about 85%, which I thought was pretty impressive. Depending on how rare the items in your music collection are, your mileage may vary.

## Android Development

<img class="alignleft  wp-image-3558" title="The Android attack !" src="http://www.streamhead.com/wp-content/uploads/2012/08/the_android_attack_.jpg" alt="" width="233" height="310" />In general, I found Android to be very well documented. Even though things tend to move quickly.

Android does carry some of the Java overhead with it. For instance, multi-threaded code can be a hassle because anonymous inner classes aren&#8217;t exactly easy on the eye. The Eclipse plugin does help with a few things (like managing resource id&#8217;s)

There were a few exceptions were the documentation failed, most notably the &#8220;strict mode&#8221;. This mode exists to force you to make your code behave better (for instance, it forces you to do all operations it considers resource intensive in threads). According to the official documentation, it&#8217;s a development only feature, but it turns out it is enabled on production devices such as the latest Samsung Galaxy&#8217;s.

The developer&#8217;s console on the Play store was instrumental in debugging this. It gathers crash information. Definitely a big plus to have this available.

## Conclusion

I&#8217;m definitely planning a few more Android apps. Most of which will be more general and less niche than this one.

But in the meantime, try out [Discogs Scan](https://play.google.com/store/apps/details?id=com.peated.discogs.scan) and let me know what you think.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->