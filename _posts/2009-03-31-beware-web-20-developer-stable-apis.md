---
id: 1161
title: 'Beware Web 2.0 Developer: How Stable Are Those APIs?'
date: 2009-03-31T10:00:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1161
permalink: /beware-web-20-developer-stable-apis/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/03/reliable.png
dsq_thread_id:
  - "14757110"
categories:
  - Java and JavaScript
---
Have you ever been working on something, **you&#8217;ve made great plans**, you put the foundation in place, you&#8217;re already halfway and you will be **finished well before the deadlines**. But then, suddenly, it appears the ground you build on is quicksand and half of **your building is tumbling down**.

It&#8217;s exactly the same with **Web 2.0 mashups**. Beware of the ground you build on. Make sure it&#8217;s stable and reliable.

This post is actually a replacement post, to make up for a sudden change of a Web 2.0 service I won&#8217;t be naming (to protect the innocent). I wanted to bring you another neat shiny little toy that combines a few free services and tools.

However, just as I was going to publish my prototype for all of you to enjoy, it stopped working. **One of the public APIs changed**. I don&#8217;t earn money with this, but if you are, you might want to keep in mind that service providers have no obligation to you if you don&#8217;t pay them. Even if you do pay, you might want to read this post on how to be prepared for this and limit your exposure to such changes.

## Choice of services

First of, you might want to check the services you&#8217;re planning to use. There are many many to choose from, some have been around for a while, some are backed by big names and some are just neat.

A **paying service** always carries a little extra weight, so if possible, see if it is available, if the price they are charging seems possible ($1/month for infinite storage usually has a catch) and what the **license agreement** looks like. Are there terms of service? Do they offer a service level agreement.

If you want to offer a commercial service, you&#8217;ll need all of that and paying a little is certainly worth it. If you just want to build up a free web presence with a few nice twists and tweaks, I wouldn&#8217;t worry too much about.

You might want to take a look at **who&#8217;s behind the service**. A name like &#8220;Google&#8221; offers more peace at night then a run-of-the-mill web startup by a guy in his garage. Although Google has been known to shut down services, so your mileage may (and will) vary.

## API changes

Is the service still in **beta**? If  yes, you should be prepared for API changes and a lot of headaches, when suddenly the company offering the service decides to change some API details overnight.

The word &#8220;beta&#8221; has been hollowed out a bit, due to stuff like Gmail being in beta forever.

## Backup

As always, make sure you have a <a title="The perfect backup" href="http://www.streamhead.com/backups/" target="_blank">backup</a>. If you&#8217;re <a title="recipe book 2.0: integrating ext with delicious" href="http://www.streamhead.com/integrate-ext-with-delicious/" target="_blank">storing data on a free host</a>, you&#8217;re best of to keep a copy on your own PC and backup medium. If ever the hosts goes out of business, you can always set up the data elsewhere or on your very own server.

If you have that backup, you&#8217;ll still need a bit of development time to switch. If possible, try to make it pluggable in your code, so that you can easily change it (for once this _could_ be a good use for XML)

If the host also offers some kind of data processing or specialised data delivery of which you can not easily make a copy (or you aren&#8217;t allowed to, legally), it might not be that easy. But at worst, you should carefully analyse to which risks you are exposed:

  * What portion of your application will stop functioning?
  * Are there other providers you can use?
  * Can you build it yourself? Or do expect to have the money to hire some one?

## Conclusion

But don&#8217;t let that stop you! Web 2.0 services and mashups are great. There&#8217;s some brilliant people out there making incredibly cool stuff. Just know the risks if you&#8217;re betting your life on that service.

<a title="Reliable Drugs Liquors on Flickr" href="http://www.flickr.com/photos/dogwelder/34646237/" target="_blank">Image credit</a>.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->