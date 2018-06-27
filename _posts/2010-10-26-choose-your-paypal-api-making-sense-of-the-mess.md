---
id: 2753
title: Choose Your PayPal API, Making Sense of the Mess
date: 2010-10-26T10:00:36+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2753
permalink: /choose-your-paypal-api-making-sense-of-the-mess/
dsq_thread_id:
  - "162082662"
categories:
  - Java and JavaScript
---
<a title="launching my first vaadin appengine project" href="http://www.streamhead.com/launching-my-first-vaadin-appengine-project/" target="_blank">The invoicing and accounting web app</a> I&#8217;m building will require payment if it is used by larger companies. To facilitate this, I turned to the biggest online payment provider that I knew that also has integration options: PayPal. <a title="PayPal X Developer Network" href="https://www.x.com/index.jspa" target="_blank">On its developer website</a>, PayPal offers an immense amount of options with very little guidance on what to choose.

<!--more-->I&#8217;ve tried to go over the different options and figure out when you might want to use which API. Here&#8217;s a little flow chart (click to enlarge):

[<img class="alignnone size-medium wp-image-2754" title="Pick your PayPal API" src="http://www.streamhead.com/wp-content/uploads/2010/10/paypal-300x297.png" alt="Pick your PayPal API" width="300" height="297" srcset="http://www.streamhead.com/wp-content/uploads/2010/10/paypal-300x297.png 300w, http://www.streamhead.com/wp-content/uploads/2010/10/paypal.png 687w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2010/10/paypal.png)

Your most important choice will be whether you implement everything via the web services or you use many of the forms PayPal offers. I like the second option because seeing the familiar PayPal screens will give your users extra confidence. Paying via the Internet is always a case of trusting the other party.

I doubt any one will use the asynchronous Instant Payment Notification (IPN) as this doesn&#8217;t provide guarantees and, I believe, will also greatly complicate your code.

If you&#8217;re programming in Java, you will also notice most of the SDK code is pretty awkward (remember model 1? No? Good). So as soon as I noticed there is <a title="PayPal NVP Java library" href="http://paypal-nvp.sourceforge.net/index.htm" target="_blank">a pretty straightforward and seemingly robust Java library for the Express Checkout API</a>, that pretty much made the choice for me.

Do you have any experience with PayPal? I&#8217;d love to hear your view on their API jungle. I&#8217;m also open to corrections, as PayPal&#8217;s documents are far from clear and different names seem to apply to the same technology.

**update**: Today I actually wanted to try out Website Payments Pro. Turns out that this is only available in the US, UK and Canada. You&#8217;d think that this would be advertised in a large type somewhere on the front page. But it isn&#8217;t. The mess is even worse than I thought.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->