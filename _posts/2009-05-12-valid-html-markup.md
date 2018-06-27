---
id: 1313
title: Valid (X)HTML Markup in 6 Steps, Like Correct Spelling
date: 2009-05-12T10:00:30+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1313
permalink: /valid-html-markup/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/05/html_can_not_do_that.png
dsq_thread_id:
  - "17933227"
categories:
  - Java and JavaScript
---
The last hour, I&#8217;ve been busy trying to get my site&#8217;s markup valid. <a title="HTML validation" href="http://validator.w3.org/check?uri=http%3A%2F%2Fwww.streamhead.com%2F&charset=(detect+automatically)&doctype=Inline&group=0" target="_blank">The frontpage now validates</a>, but there&#8217;s till work to be done to the other pages. So after reading <a title="HTML Purity, does it matter?" href="http://www.yafla.com/dforbes/HTML_Purity__Does_it_matter/" target="_blank">Dennis Forbes&#8217; post</a>, I noticed I&#8217;ve been running for the past year or so with invalid markup and nobody ever pointed that out. One might rightfully wonder: does it actually matter?

Personally, I think it does and I feel I need to fix the remaining problems as soon as possible. I might even go from the &#8220;XHTML transitional&#8221; to the &#8220;strict&#8221; doctype, just for kicks (<a title="Transitional vs. Strict Markup" href="http://24ways.org/2005/transitional-vs-strict-markup" target="_blank">and other advantages</a>). Not only will good XHTML give a tidy impression to visitors, but it is also one of the most reliable ways to make sure your site looks the same on all browsers and operating systems. And if you go for <a title="HTML versus XHTML" href="http://www.webstandards.org/learn/articles/askw3c/oct2003/" target="_blank">XHTML instead of HTML</a> is will also be able to use neat stuff like XSL.

In order to get my pages in order (still a work in progress), there were actually only 6 errors that keep repeating. Because I&#8217;m running WordPress, it isn&#8217;t always easy to find the source. It could be a plugin that inserts some HTML somewhere or part of the header, or was it in the sidebar?

  1. If you copy from webpages, **make sure you are copying code pieces without layout**. The build in TinyMCE editor is great, but if you copy a piece of code from a webpage, it sometimes pickes up HTML codes that you can&#8217;t see, but that will mess up your pages. For instance, I had problems with HTML comments (two dashes were copied as one long).
  2. **Close your tags**. This is the most basic rule of them all if you are creating XHTML, but it is very important. It&#8217;s easy to write <br> instead of <br/>, but only the last one is correct.
  3. Put **alt tags on images**. And don&#8217;t just put in some random piece of text. Try to make it descriptive, because blind people need them to fully enjoy your website. As do people with slow connections (they are still out there)
  4. **Encode special characters**. This is again a XHTML requirement. Probably the most popular special character you&#8217;ll run across is the ampersand (&), you should write it as &#8220;&&#8221; Don&#8217;t worry about your blog posts, the build in editor will take care of it. This is just for the templates.
  5. **Uppercase and lowercase matter**. Tag names should all be lower case, so <META &#8230;> is not the same as <meta &#8230;> Obviously the actual text can be any case you wish.
  6. If you give **id&#8217;s** to div&#8217;s (or other elements), they **should be unique**. This is not only a requirements, but if you plan on adding JavaScript to your site, you will save yourself a lot of headaches if you keep this in mind from the start.

If you want to test your own site, you can do so, entirely free of charge, at <a title="W3C Markup Validation Service" href="http://validator.w3.org/" target="_blank">the W3C Markup Validation Service</a>. Good luck with those tweaks.

<a title="Flickr Photo: html can not do that" href="http://www.flickr.com/photos/thefangmonster/490423135/" target="_blank">Image credit</a>.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->