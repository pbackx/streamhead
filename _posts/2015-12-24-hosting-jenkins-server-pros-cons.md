---
id: 3802
title: 'Hosting your own Jenkins server &#8211; pros and cons'
date: 2015-12-24T14:52:49+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3802
permalink: /hosting-jenkins-server-pros-cons/
pdrp_attributionLocation:
  - tag
image: /wp-content/uploads/2015/12/hacksgiving-platter.png
categories:
  - Java and JavaScript
---
Using a hosted version of Jenkins can be fairly expensive. Especially if you&#8217;re looking to continuously integrate your hobby project. [A $5 Digital Ocean server](https://www.digitalocean.com/?refcode=6f086f001f5e) and an afternoon of configuration can seem tempting. In this post I&#8217;ll look at the pros and cons of selfhosting Jenkins.

<!--more-->

I&#8217;ve always been a very happy CloudBees user, but over the years they&#8217;ve taken away more and more. Initially, there was a free plan, they removed that at the beginning of 2014 (IIRC). The starter plan was still good value, but at the beginning of this year, they removed support from that plan and replaced it with &#8220;have fun with Google&#8221;. And right now, you have to speak to their sales team to even get a quote from them.

Clearly, CloudBees had decided it was no longer a good fit for me and my small hobby projects. So I started to look for alternatives. Halfway through the year, I switched to a Digital Ocean droplet (a $10/month one)

5 reasons to get a VPS and **install and maintain Jenkins on your own**:

  1. It&#8217;s a lot cheaper. The cheapest plan I had was $60/month. But that one probably no longer exists and it also doesn&#8217;t include their awesome support. I think it&#8217;s safe to assume that the current cheapest rate is at the very least $100+/month.
  2. With a VPS, you don&#8217;t have a complicated and fairly unpredictable cost structure. CloudBees charged for build-minutes and the cost depends on the type of slave configured.
  3. You have complete flexibility. You can install whatever you want.
  4. Need Windows? You can.
  5. Jenkins is fairly user friendly and easy to setup and maintain, so it only takes an afternoon to get the basics configured and running.

Reasons why **CloudBees still rocks**:

  1. I&#8217;ve always had great customer service with people who knew Jenkins and the addons.
  2. They are the maintainers of Jenkins. So they really know what they are doing.
  3. Scaling is available any time you need it on any plan. So no worries if your hobby project suddenly becomes a billion dollar enterprise.
  4. CloudBees hosting comes with integrated services that you&#8217;ll need anyway, like Git and a Maven repository.
  5. CloudBees has a lot of useful add-ons, some free-with-limits (Saucelabs), some fairly expensive (Sonar)

## Conclusion

Your choice will depend on your personal preference and your environment. If you&#8217;re in an enterprise and have 10 or more developers. Go for CloudBees. You won&#8217;t regret it and it&#8217;s a lot easier then setting up everything yourself and making sure the builds are quick.

If you want a Jenkins server for your hobby projects. Rolling your own will be your only option. But don&#8217;t fear, it&#8217;s not very complicated.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->