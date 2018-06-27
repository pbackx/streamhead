---
id: 2757
title: PayPal, a Useful Integration Guide
date: 2010-11-02T10:00:34+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2757
permalink: /paypal-integration-guide/
dsq_thread_id:
  - "165636615"
image: /wp-content/uploads/2010/11/paypal_integration_guide.png
categories:
  - Java and JavaScript
---
This post goes into the different steps I&#8217;ve taken to get started with integrating PayPal in my AppEngine Java application. I couldn&#8217;t find a clear list of steps to take in the PayPal documentation, so I&#8217;m sure other developers will find the following summary very useful.

<!--more-->As I progress with my PayPal integration, you&#8217;re probably going to see a few more posts like these. These help me clarify what needs to be done and hopefully they&#8217;ll help others. The PayPal documentation is a mess, it&#8217;s all there, it&#8217;s just very very hard to find the things relevant to you. I hope this post gives some insight.

<a title="Choose your PayPal API" href="http://www.streamhead.com/choose-your-paypal-api-making-sense-of-the-mess/" target="_blank">My previous post tried to summarize all the PayPal APIs available</a>. If your business is outside of the United States, it&#8217;ll be a whole lot easier:

[<img class="alignnone size-medium wp-image-2777" title="International choices for PayPal integration" src="http://www.streamhead.com/wp-content/uploads/2010/11/paypal_international-300x94.png" alt="International choices for PayPal integration" width="300" height="94" srcset="http://www.streamhead.com/wp-content/uploads/2010/11/paypal_international-300x94.png 300w, http://www.streamhead.com/wp-content/uploads/2010/11/paypal_international.png 427w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2010/11/paypal_international.png)

There are no choices to make. All the &#8220;pro&#8221; APIs are for United States businesses only and, sometimes, a few choice countries (usually UK and Canada, but be careful, it depends).

So most of the world will have to do with:

  *  **Payment Data Transfer (PDT) messages** when users are redirect to your page. This is fairly unreliable, because your user might close down his browser and you&#8217;d have no idea that he paid.
  * **Instant Payment Notification (IPN) updates** send directly to your server from the PayPal servers. Messages will always be sent, although I don&#8217;t think there is a guarantee on how long delivery could take.
  * **Supporting both of the above**. Which I believe is the only solution that is foolproof and will always give your users immediate access to the services they paid for.

The basic webpage flow and server-to-server communications look like this (click for a larger version):

[<img class="alignnone size-medium wp-image-2779" title="paypal communications flow" src="http://www.streamhead.com/wp-content/uploads/2010/11/paypal_flow-300x192.png" alt="paypal communications flow" width="300" height="192" srcset="http://www.streamhead.com/wp-content/uploads/2010/11/paypal_flow-300x192.png 300w, http://www.streamhead.com/wp-content/uploads/2010/11/paypal_flow.png 687w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2010/11/paypal_flow.png)

The steps you&#8217;ll need to take to get this working are as follow. I haven&#8217;t completed the full integration process, so the last few are a bit less detailed:

  1. Set up at least **one buyer and a business account on the PayPal sandbox** environment. You&#8217;re best bet is to skip the wizard and create fully customized accounts. <a title="PayPal sandbox user guide" href="https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_Sandbox_UserGuide.pdf" target="_blank">There&#8217;s minimal guide available to get you started with the sandbox</a>.
  2. Build a **IPN handling servlet**. PayPal just sends a bunch of name/value parameters which you have to interpret. <a title="IPN Guide" href="https://cms.paypal.com/cms_content/US/en_US/files/developer/IPNGuide.pdf" target="_blank">This document has an appendix with all the variables</a>.
  3. <a title="PayPal Order Management Integration Guide" href="https://cms.paypal.com/cms_content/en_US/files/developer/PP_OrderMgmt_IntegrationGuide.pdf" target="_blank">Take a close look at the IPN chapter in this guide</a>. It&#8217;ll explain how to **validate notification**. PayPal doesn&#8217;t force you to do this but for the safety of your site and users, you&#8217;d better do. Also see the guide for item 2 if you want additional information.
  4. **Test your servlet with the developer tools**. You can make PayPal send pretty much any IPN notification you want. Although it&#8217;s fairly difficult to exactly reconstruct the ones you&#8217;ll actually receive, at least it will take care of obvious bugs in the servlet and you can also verify that validations is working.
  5. With your business account, log in to the system and **create the payment button(s)** you need. <a title="Website Payment Standard" href="https://www.x.com/docs/DOC-1448" target="_blank">There are many guides available for </a>creating just the right button, but if you got this far, you probably don&#8217;t need them.
  6. Put the buttons on your test site and try them out with your buyer account (_this is about where I am right now_).
  7. **Configure autoreturn** and PDT with the business account.
  8. **Implement PDT** in your application. <a title="PayPal Order Management Integration Guide" href="https://cms.paypal.com/cms_content/en_US/files/developer/PP_OrderMgmt_IntegrationGuide.pdf" target="_blank">See the guide mentioned in item 3</a> or see <a title="PayPal X Developer Network: Payment Data Transfer" href="https://www.x.com/community/ppx/pdt" target="_blank">the Payment Data Transfer pages</a>.
  9. **Configure your IPN receiver** (you do this in the properties of your business account).
 10. **Test your application**.
 11. Set up everything the same in a production environment.
 12. Go live

If you have any other resources, I&#8217;d love to hear about them. Or if you want a little more information on any of the items, let me know and I&#8217;ll elaborate.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->