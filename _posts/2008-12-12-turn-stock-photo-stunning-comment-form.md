---
id: 610
title: Turn a Stock Photo into a Stunning Comment Form
date: 2008-12-12T10:00:22+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=610
permalink: /turn-stock-photo-stunning-comment-form/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/12/contactme.png
dsq_thread_id:
  - "8044187"
image: /wp-content/uploads/2008/12/contactme.png
categories:
  - Java and JavaScript
---
Inspired by <a title="Turn postcard photo into a stunning comment form using CSS" href="http://www.jankoatwarpspeed.com/post/2008/09/15/Turn-postcard-photo-into-a-stunning-comment-form-using-CSS.aspx" target="_blank">this great article</a>, I got working. I found <a title="Old Hebrew Sign on Flickr" href="http://flickr.com/photos/bright/77014812" target="_blank">a nice picture on Flickr</a> and <a title="Contact Peter" href="http://www.streamhead.com/contact/" target="_blank">this is the result</a>. Now let me tell you, the article makes it look dead easy to get such a nice form. In reality, it is in fact not that hard, but it&#8217;s a lot of pixel hunting, trying out colors and positions. Especially since I wanted to integrate this with the <a title="cforms II" href="http://www.deliciousdays.com/cforms-plugin" target="_blank">incredible cForms plugin for WordPress</a>.

I&#8217;m still not entirely happy, but for now, it&#8217;s good enough. Here&#8217;s how I did it (beware, it&#8217;s probably not for the HTML and CSS newbie):

  * I created my form in the cforms control panel. This form has been online for a while, I didn&#8217;t really change a thing.
  * The entire code for the form was copied to a local HTML file and I added the style sheet from Janko&#8217;s tutorial to it.
  * Using Firebug, I figured out which fields I needed and changed the correct names in the CSS file.
  * When I was happy, I created a new style in the cforms _styling_ folder and selected that style to be used.
  * I also created <a title="Pages - WordPress Codex - Creating your own page templates" href="http://codex.wordpress.org/Pages#Creating_Your_Own_Page_Templates" target="_blank">a special WordPress template</a> for the contact form. That way I could disable the normal heading.

The major caveat here, is that cforms only allows you to select one style for all your forms. So if you have multiple forms, I&#8217;m affraid you&#8217;re out of luck. You could put the style sheet link in your page template, I guess. But I haven&#8217;t tried it yet.

One more &#8220;to do&#8221; for my form is to correct the error handling and get rid of the extra white that is inserted when hovering over the fields. But I&#8217;m going to leave it like it is for now. This 5 minute project has already taken enough evenings as it is.

_update_: this form was featured on the previous Streamhead design. For now it has been replaced by a fairly generic version. When I get around to it, I&#8217;ll be replacing it with something even better.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->