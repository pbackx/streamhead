---
id: 3569
title: PayPal AppEngine Servlet, Now Cloud-Ready
date: 2012-08-10T17:36:35+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3569
permalink: /paypal-appengine-servlet-now-cloud-ready/
pdrp_attributionLocation:
  - end
categories:
  - Java and JavaScript
tags:
  - paypal
---
I&#8217;ve just pushed a major extension to my [PayPal AppEngine Servlet](https://github.com/pbackx/PayPalIPNServlet). It&#8217;s now much more failsafe and takes the validation work out of your hands. Read on for an overview of the new architecture.

<!--more-->

A variation of the servlet that was included with the GitHub repo has been running for almost 2 years on [my own AppEngine application](http://www.fctr.be "eenvoudig boekhouden"). And over that time it has been remarkably reliable (given PayPal&#8217;s API), but has also shown some issues. Some minor ones that were easily fixed, but also one major:

Whenever PayPal was down or just a little slow, the serlvet would run into timeout exceptions and would not validate the IPN message and, what was worse, would not process it correctly.

Eventually, I realized this is just part of the day-to-day operations of any application deployed to the cloud, so I&#8217;d better clean up my act and start thinking like a cloud developer.

[tweetherder]Cloud development = make everything handle errors gracefully and retry on failure[/tweetherder].

The first part was easy enough and should have been part of the code from the start. The second required a rethinking of my architecture. I&#8217;ve now hooked everything into [task queues](https://developers.google.com/appengine/docs/java/taskqueue/overview "Task Queue Java API Overview"), which means every part is independent, can be easily retried and does not influence the other parts when it fails.

## Small independent parts

There are 3 servlets that interact as follows:

[<img class="aligncenter size-medium wp-image-3571" title="paypal_appengine_servlet_architecture" src="http://www.streamhead.com/wp-content/uploads/2012/08/paypal_appengine_servlet_architecture-265x300.png" alt="PayPal AppEngine Servlet Architecture" width="265" height="300" srcset="http://www.streamhead.com/wp-content/uploads/2012/08/paypal_appengine_servlet_architecture-265x300.png 265w, http://www.streamhead.com/wp-content/uploads/2012/08/paypal_appengine_servlet_architecture.png 413w" sizes="(max-width: 265px) 100vw, 265px" />](http://www.streamhead.com/wp-content/uploads/2012/08/paypal_appengine_servlet_architecture.png)

All interaction between the servlets is through a queue. If you haven&#8217;t used the task queues on Google&#8217;s AppEngine, it&#8217;s about time. I too waited too long, but the push queues are an incredible easy way to build fail safety into your application.

You don&#8217;t need to worry about retries, as long as the servlet returns anything but a 200-299 status code, AppEngine will keep retrying the call. You can specify how long it should wait before retries and when it should just give up.

## Transactions

Because 3 servlets are writing and reading data for the same entity, I also had to make sure every servlet has a consistent view.

Something that isn&#8217;t as easy as you might think in the DataStore. It only guarantees eventual consistency. Strong consistency can only be guaranteed in the same entity group. No problem for changing single IPN message, but duplicate checking requires a query over the entire table.

I could create one big entity group for all IPN messages, but that would sort-of defeat the entire purpose of cloud computing. I think I now have a good trade-off with only a very minor risk of duplicates entering the system. Which shouldn&#8217;t cause any major issues anyway if your program handles the messages in an idempotent way.

If you know a better way to deal with this, please have a look at the IPNValidationServlet and let me know.

## Conclusion

Every one&#8217;s feedback has really helped me to improve the previous version of the code, so I hope you try out the new one too and let me know what you think. [The readme has all the information to get you started](https://github.com/pbackx/PayPalIPNServlet "PayPal AppEngine IPN Servlet").

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->