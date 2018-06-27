---
id: 3655
title: Upgrading to Vaadin 7 Step by Step
date: 2013-10-11T11:46:25+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3655
permalink: /upgrading-vaadin-7/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2013/10/pegasus_xl_20120611_01.jpg
categories:
  - Java and JavaScript
---
After my review of the [Vaadin 7 Cookbook](http://www.streamhead.com/vaadin-7-cookbook-review/ "Vaadin 7 Cookbook review"), I decided it was time to upgrade [my own application](http://www.streamhead.com/launching-my-first-vaadin-appengine-project/), that had been running on Vaadin 6 for quite some time to Vaadin 7. In this post I share my experience and a guide on how to do it yourself and what to watch out for (there are quite a few gotchas)

<!--more-->

## Upgrading FCTR.be

I wanted to start the upgrade process in August, but after reading the cookbook and going over the Vaadin documentation, it quickly became clear that this was not something I could do on my own in my spare time, so I hired an elancer.

The [SPEC INDIA team](https://www.elance.com/s/specindia/) was great to work with and especially Sankit was a very knowledgeable developer. They were the only ones that gave me a good idea and also provided me with a realistic estimate. All the other bidders promised me they would do it in one fifth of the time. Something which I don&#8217;t believe would have been possible.

After scoping down the project a little (see below), Sankit ended up working 85 hours on the upgrade, while I took about 20 hours for testing and to fix some of the issues that weren&#8217;t apparent if you don&#8217;t understand Dutch.

So, for your own project, **expect to spend at least 100 hours on any reasonably sized Vaadin 6 application**.

The end result has been running in production for about 2 weeks now with very little issue. There were some IE9 users that had to clear their browser cache manually, but that was it.

## Do It Yourself

Sometimes the upgrade will be easy, a matter of replacing the JAR file and updating the Application to a UI object. For instance, [my PayPal project](http://www.streamhead.com/paypal-ipn-java-appengine-servlet-gets-update/) was completely forwards compatible.

In most cases though, it&#8217;s going to take more effort.

First and foremost, you should start with [Vaadin&#8217;s own migration guide](https://vaadin.com/wiki/-/wiki/Main/Migrating+from+Vaadin+6+to+Vaadin+7). If you go through these steps and comment out anything that doesn&#8217;t compile, you should be able to get something up-and-running fairly quickly. That&#8217;s when the real work starts.

### Forms

If you were hacking your way around the old forms implementation, there&#8217;s good news and bad news.

The good news: the new forms are way better, much more versatile and the code is well designed.

The bad news: you&#8217;re going to be in pain upgrading everything from FormFieldFactories to CustomFields. The Vaadin developers were kind enough to leave in some deprecated legacy components, so that you can keep using most of your old form code (which is what I did).

### Session

This was the part I did not expect and that took me the most effort to get right.

Vaadin 6 stored the complete state of your application in the session. So if you opened the application, then opened another site in that window. When you returned to the application you&#8217;d still see the old state. This was both good and bad and my application used that feature in a few interesting ways. For instance, when redirecting to PayPal and back, it was convenient to have the same UI still there.

That&#8217;s no longer the case. If you want things in the session, you need to store them there yourself. You can use the @PreserveOnRefresh annotation, but it does not work exactly the same way that Vaadin 6 worked. It uses the window.name DOM element, which turns out to be pretty unreliable if you redirect to banking sites (including PayPal)

So I would advise any one to just skip @PreserveOnRefresh and implement things properly. What I ended up doing was to explicitly store the user ID in the session, but not all the other things. It does mean, that if the user goes to PayPal to make a payment, all of his open windows will be closed and some information may be lost. If you don&#8217;t want that, you need to take special precautions.

<img class="aligncenter size-full wp-image-3665" alt="Monome DIY Kit: Tactile Keypads" src="http://www.streamhead.com/wp-content/uploads/2013/10/monome_diy_kit_tactile_keypads.jpg" width="1024" height="681" srcset="http://www.streamhead.com/wp-content/uploads/2013/10/monome_diy_kit_tactile_keypads.jpg 1024w, http://www.streamhead.com/wp-content/uploads/2013/10/monome_diy_kit_tactile_keypads-300x199.jpg 300w" sizes="(max-width: 1024px) 100vw, 1024px" />

### Themes

Initially we decided to use the legacy theme support, which means you don&#8217;t really have to do much, except change one path in your own custom theme.

But it turns out to be fairly easy to migrate to the new SASS based themes. It took my about an hour, but most of that was spend learning SASS and figuring out how to include the 960.gs CSS file.

### Widgets

Early on, it became clear that the custom widgets I was using were going to be difficult to port and would be much easier to just rewrite from scratch.

Since all my custom widgets were for user tracking and other optional tasks, I decided to simply not have any custom widgets for now and take care of them later.

I did try to reintroduce the Google Analytics widget and stumbled upon [a show-stopping bug](http://dev.vaadin.com/ticket/12532) when using the new JavaScript support in Vaadin in conjunction with Google AppEngine. So I&#8217;m waiting for that fix before I continue.

### Tips

Don&#8217;t forget that the book also comes with [a large set of examples](http://demo.vaadin.com/book-examples/book/) (that aren&#8217;t always mentioned or linked in the actual book).

The Vaadin Pro account gives you access to support, but you have to pay extra to actually get it. It&#8217;s clearly mentioned on Vaadin Pro pages, but it&#8217;s easy to read over it. The Pro account does come with free bugfix prioritization and access to a bunch of awesome libraries.

## What&#8217;s Next

Over the next weeks (and possibly months) I will gradually remove all the deprecated code. Those are mostly the old forms, but I expect to run into one or more tricky things.

I&#8217;m also going to start incorporating some of the new Vaadin stuff, which is exactly why I decided to upgrade. Most importantly I&#8217;m looking forward to introducing the new navigation and making good use of JavaScript integration once that&#8217;s fixed.

And since I now have a Pro account, I&#8217;d also love to get started with the TouchKit.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->