---
id: 2803
title: Java PayPal IPN Servlet
date: 2010-11-12T10:00:55+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2803
permalink: /java-paypal-ipn-servlet/
amazon_post_template:
  - ""
dsq_thread_id:
  - "171255873"
image: /wp-content/uploads/2010/11/GAE_handle_PayPal_IPN.png
categories:
  - Java and JavaScript
---
For those following along <a title="PayPal Integration Guide" href="http://www.streamhead.com/paypal-integration-guide/" target="_blank">my adventure to integrate with PayPal</a>, here is the next step. I&#8217;ve created a Google AppEngine Java servlet that handles the Instant Payment Notification (IPN) messages PayPal sends your way. I&#8217;ve made <a title="PayPal IPN GAE/J servlet" href="https://github.com/pbackx/PayPalIPNServlet" target="_blank">the servlet freely available on GitHub</a> in the hope of fostering some cooperation.

<!--more-->

<p class="update">
  <strong>update</strong>: The project has been updated since this post and is now fully &#8220;Maven-ized&#8221;. <a href="http://www.streamhead.com/updated-paypal-appengine-servlet/" title="Updated PayPal AppEngine servlet">Please see this post to check out the changes and read about future plans</a>.
</p>

Sorry, no Maven this time. If you put the code in an Eclipse Vaadin/Google AppEngine project you only need to add <a title="Objectify" href="http://code.google.com/p/objectify-appengine/" target="_blank">the Objectify jar</a> in the war/lib directory and you&#8217;re ready to get started.

The servlet lives in the /ipn context. So if you use PayPal&#8217;s IPN developer tool to create messages, don&#8217;t forget to add it.

All IPN messages that PayPal sends your way need to be validated. I&#8217;ve implemented the validation by postback. There is one issue, though, the PayPal sandbox servers can be slow from time to time. As Google puts a timeout of 10 seconds on every request you make, you might run into trouble.

The code worked flawlessly until today, right now I&#8217;m only getting timeouts. The IPN messages are stored anyway, but they are flagged as not validated. This allows you to continue processing the payment, you just need to investigate the messages later on.

The project also contains a small Vaadin application to easily access the messages. I haven&#8217;t done much parsing, except for the transaction type. I leave this as an exercise to the reader 🙂

<p class="update">
  <strong>update</strong>: The project has been updated since this post and is now fully &#8220;Maven-ized&#8221;. <a href="http://www.streamhead.com/updated-paypal-appengine-servlet/" title="Updated PayPal AppEngine servlet">Please see this post to check out the changes and read about future plans</a>.
</p>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->