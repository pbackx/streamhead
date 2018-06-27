---
id: 3780
title: The future of forums, civilized Discourse
date: 2015-06-19T18:11:52+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3780
permalink: /the-future-of-forums-civilized-discourse/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2015/06/14595403070_c2eb9f080d_z.jpg
categories:
  - New Media and the World
---
Forums have been around for a long long time. However, it hasn&#8217;t been until fairly recently that we&#8217;ve seen some people trying to improve on the old formula. [Discourse](http://www.discourse.org/) is one such project, which I recently used to upgrade an old Simple Machines Forum installation.

<!--more-->

I&#8217;ve been running the [Build Your Own Personal Video Recorder](http://forum.byopvr.com/) forums for a while now. Sadly, I hadn&#8217;t been putting much energy into the forum and on top of that there&#8217;s a diminishing interest in actually recording video. Streaming is taking over the world: either Netflix if you want to pay a little bit or Popcorn Time if you really must pirate.

Anyway, the forum had become a mess and was overrun by spammers. It was so bad I had to disable registration entirely, because the automated bots were so good at circumventing all anti-spam measures.

So at the beginning of the year, I decided to move the forum to a Discourse installation to experiment and try out new things. Around the end of February I actually pulled the switch.

## The good

  * Although it&#8217;s beta, the forum has run **very stable** on a [1GB Digital Ocean droplet](https://www.digitalocean.com/?refcode=6f086f001f5e) (yes, I&#8217;m happy customer of them).
  * Installation was a breeze. I really like how they **packaged everything in a Docker container**.
  * **No more spam**. And if there is, it&#8217;s almost automatically taken care of.
  * The forum UI itself is **well thought out**.

<span class="embed-youtube" style="text-align:center; display: block;"></span>

## The slightly less good

  * Although installation was easy. When I wanted to import everything and keep all old links working, some extra work was needed. This easily took up 90% of the time needed to **migrate the existing forum**. The Discourse meta forum was very helpful! [I also created and open sourced some utility code to redirect your old links](https://github.com/pbackx/smfmapper).
  * While the UI is clever, it&#8217;s **a pretty big change** from the very structured organizing of most other forums. I didn&#8217;t have many regulars on the forum, but I believe the change was a bit too big for them.
  * **Customizing** the forum&#8217;s look is not very well documented, which is one of the reasons the forum still looks very &#8220;stock&#8221; (the most import reason being other priorities)
  * There&#8217;s **no easy way to integrate AdSense**. Some one who can come up with a good solution is bound to make money with that.

## Conclusion

I&#8217;m a happy user. I like how Discourse integrates some of the StackOverflow concepts to get rid of spam. I will keep running Discourse and I hope to report back with some of the customizations I&#8217;ve done and neat ways I&#8217;ve found to use the forum.

[Don&#8217;t forget: if you want to migrate from a Simple Machines Forum and want to redirect your old links, don&#8217;t forget to check out my code (get in touch if you need help)](https://github.com/pbackx/smfmapper)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->