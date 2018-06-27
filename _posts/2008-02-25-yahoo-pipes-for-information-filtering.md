---
id: 55
title: Yahoo! Pipes for information filtering
date: 2008-02-25T04:27:35+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=55
permalink: /yahoo-pipes-for-information-filtering/
dsq_thread_id:
  - "5437815"
categories:
  - Java and JavaScript
---
If you&#8217;re not intimidated by this screenshot, please read on.

[![example pipe](http://www.streamhead.com/wp-content/uploads/2008/02/pipes.thumbnail.png)](http://www.streamhead.com/wp-content/uploads/2008/02/pipes.png "example pipe")

[Yahoo! Pipes](http://pipes.yahoo.com/pipes/) allows you to visually design a transformation on web resources. You define input sources for pretty much anything that is available on the web. And transform that data into any form you want. You can filter data you don&#8217;t need, merge different sources and many more.

What I wanted, was a number of album review sites as input (Resident Advisor for starters) and add some sources of samples for those albums. [This is what I came up with right now](http://pipes.yahoo.com/streamhead/ralatest). Yahoo doesn&#8217;t show you the links in the preview, so you might want to take a look at [the RSS version](http://pipes.yahoo.com/pipes/pipe.run?_id=8gi_2QDi3BG_q_b_oeNLYQ&_render=rss).

Take a look at the source to see how visual and easy this process is. The RSS is loaded and truncated at 5 items. For each entry, the entire article is downloaded and the cover image is extracted. The album is then searched on the Amazon site and a link is added to the image.

Currently, not every album is found on Amazon, although it is usually available, so I have some work there. I would also like to add a better sample source, as Amazon doesn&#8217;t have samples for most of this new stuff. I&#8217;m thinking Beatport, but there were some ready-made components available for Amazon.

So, keep your eye on the feed, it will get better in the near future.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->