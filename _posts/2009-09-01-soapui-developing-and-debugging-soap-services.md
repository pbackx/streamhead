---
id: 1529
title: SoapUI, developing and debugging SOAP services
date: 2009-09-01T10:00:17+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1529
permalink: /soapui-developing-and-debugging-soap-services/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/08/soapUI.png
dsq_thread_id:
  - "32062144"
categories:
  - Java and JavaScript
---
This isn&#8217;t quite my usual fair, but a good tool is a good tool. If you are working on your new web 2.0 application, integrating various services, there&#8217;s always a moment when you just can&#8217;t seem to get 2 services to work together. For some reason, on service is requesting the wrong data, or is it the other service that&#8217;s replying with the wrong answer?

Only one solution to get to the heart of the problem: You need to isolate both services and test your assumptions. There are various tools that will help you test pure HTML based REST services, but when dealing with a SOAP service, I found the options pretty limited.

Until I encountered <a title="the Web Service, SOA and SOAP Testing Tool - soapUI" href="http://www.soapui.org/" target="_blank">soapUI</a>. soapUI is a tool that allows you to import WSDL files and separate client and server. You can create automated tests for the server, but you can also construct SOAP requests by hand. This allows you to play with the parameters and figure out what works and what doesn&#8217;t. Once you&#8217;ve got what you want, you can automate tests that regularly verify your assumptions of the service (you know, when documents fail).

For the client, you can create a mock implementation of the web service. So even if you&#8217;re offline or the server is offline, you can continue developing.

It&#8217;s a win-win for both sides.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->