---
id: 2691
title: WordPress Plugin HTML Customization Hack
date: 2010-09-28T10:00:35+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2691
permalink: /wordpress-plugin-customization-hack/
dsq_thread_id:
  - "148031824"
categories:
  - Graphics, Visuals and Texts
---
Plugins are a great way to enhance WordPress. However, visually those plugins don&#8217;t always work well with your theme. They tend to place their graphical elements all over the place. Most of them offer only little control over their location and visual appearance. Here&#8217;s a trick to move them to the spot you like.

<!--more-->For a while I&#8217;ve been adding a few features to my blogposts through WordPress plugins. Most importantly, I&#8217;m using and loving the Outbrain rating plugin and the Sociable social bookmarking and sharing plugin. One thing I didn&#8217;t like was the way those plugins integrated on the webpage. They just add a bunch of stuff to the end of the post that you have no control over.

Until now.

This is a fairly advanced topic, but not that complicated once you get the hang of it. Plugins add HTML code to your site by adding filters to the WordPress rendering. For instance, by adding a filter to the &#8220;the_content&#8221; execution, it is possible to influence the output of the blog post details.

Outbrain and Sociable work exactly like this. When the content of the post is rendered they add a filter to it that adds their own widgets. What I wanted to achieve was to have more influence over the placement of those plugins.

If you go to a post detail now, you&#8217;ll notice that both widgets are now inside their own div (to which I added a border). It&#8217;s something that is not possible if you respect the plugins standard placement.

So how do you go about it? Well there&#8217;s three steps:

  1. First you need to figure out the name of the filter that the plugin uses. You&#8217;ll need to open up the plugin source code and find a line that looks like &#8220;add\_filter(&#8220;the\_content&#8221;, &#8220;xxxxxx&#8221;);&#8221;. For Outbrain it&#8217;s &#8220;outbrain\_display&#8221;; for Sociable it&#8217;s &#8220;sociable\_display_hook&#8221;. You might need to experiment a little with your plugin.
  2. Next you remove the filter in your functions.php
  3. And finally you add your own filter, exactly where you want to display the plugin. Or you could execute the function where you want it to. There are a wealth of possibilities here. This also happens in functions.php.

For instance, if I wanted to move the Sociable plugin from the bottom of the post content area to one of Thematic&#8217;s designated areas, called &#8220;thematic\_post\_footer&#8221;, I&#8217;d add the following code to my themes functions.php:

<pre lang="php">function remove_filter_from_the_content() {
  remove_filter('the_content', 'sociable_display_hook');
}
add_action('init', 'remove_filter_from_the_content');

function my_postfooter() {
  echo '

<div id="social_footer">
  ' . sociable_display_hook('') . '
</div>';
}	
add_filter('thematic_postfooter','my_postfooter');
</pre>

This will remove the Sociable executions from the content area, move it to Thematic&#8217;s post footer and wrap it in a div that can be used to style it.

Feel free to share your WordPress hacks in the comments.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->