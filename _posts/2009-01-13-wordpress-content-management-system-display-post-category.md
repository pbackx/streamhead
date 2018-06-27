---
id: 877
title: 'WordPress as a Content Management System: How to Display a Post from Every Category'
date: 2009-01-13T10:00:04+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=877
permalink: /wordpress-content-management-system-display-post-category/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/01/streamheadcover.png
dsq_thread_id:
  - "9459438"
categories:
  - Java and JavaScript
---
I&#8217;ve been reading a lot about using **<a title="WordPress as a CMS" href="http://www.graphicdesignblog.co.uk/wordpress-as-a-cms-content-management-system/" target="_blank">WordPress as a Content Management System</a>** (CMS), so I started researching a bit more. A CMS fits perfectly with my idea to change the frontpage to make it a bit more interesting for my visitors. I&#8217;m pretty happy with the way it turned out, <a title="Streamhead cover" href="http://www.streamhead.com" target="_blank">go take a look and let me know what you think</a>. Instead of just the latest post, it is now an entry point to the entire site.

My experience with this was a bit of a turndown. I expected it to be easy to create an index of my categories with a few posts from each of them. But it did take me longer than expected. **WordPress is a great blogging platform** and it makes it incredibly easy to customize and theme it. However, as it turns out, this has the disadvantage of making it a somewhat more complicated to do the more advanced stuff.

<div style="float:right;">
  <a title="Improved Inviolable Lock" href="http://www.flickr.com/photos/41143865@N00/285760616/" target="_blank"><img src="http://farm1.static.flickr.com/120/285760616_e61ab03e22_m.jpg" border="0" alt="Improved Inviolable Lock" /></a><br /> <small><a title="Attribution License" href="http://creativecommons.org/licenses/by/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="alisdair" href="http://www.flickr.com/photos/41143865@N00/285760616/" target="_blank">alisdair</a></small>
</div>

As a software developper, the one thing that bothered me the most is the use of **global variables** and sideeffects everywhere. For instance, inside <a title="The Loop - WordPress Codex" href="http://codex.wordpress.org/The_Loop" target="_blank">&#8220;The Loop&#8221;</a>, the method _query_posts()_ will influence how other methods like the _the_title()_ react. The results are, at first, very confusing if you want multiple loops. That&#8217;s why there is a large section dedicated to it on the loop page. In this regard, <a title="Template Tags/get posts - WordPress codex" href="http://codex.wordpress.org/Template_Tags/get_posts" target="_blank"><em>get_posts()</em></a> seems to solve a few problems, but until recently it had a different syntax than _query_posts()_ (not anymore, which is nice).

Before I show you the code, a few more things I ran into:

  * There is **no way to loop over all categories**. Unless you add a hardcoded list of categories, the only way to do this is take the output of _wp\_list\_categories_ and parse that to extract all categories. That&#8217;s where the regular expression magic comes into play.
  * If you query for posts the &#8220;category_name&#8221; parameter takes the &#8220;slug&#8221; or short name, not the &#8220;normal&#8221; name of the category. This is not clear in the codex.
  * (not in this part of the code, but) There&#8217;s an annoying bug you might run into if you want to query for posts on both categories and tags. <a title="Cannot combine category and tag queries in some cases" href="http://trac.wordpress.org/ticket/5433" target="_blank">It&#8217;s easily circumvented though</a>.

My next experiments:

  * what&#8217;s the **database load** of this new frontpage? I might need to take a look at caching.
  * allow multiple people to post in different categories. I&#8217;m not sure how fine-grained the access control is, but lets find out.

And finally, here&#8217;s the bit of **code** that will get all your categories and show the most recent post from every category. Just copy and paste it in one of your template files to see how it looks (index.php, page.php, etc.)

<pre lang="PHP"><?php
   $categories = wp_list_categories('echo=0&#038;exclude=44&#038;style=none&#038;title_li=');
   $catArray = split('<br />', $categories);
   foreach($catArray as $categoryWithLink) {
     if(trim($categoryWithLink) == '') break;
     ereg('^

<a href="(http.*/([^/]*)/)" title="(.*)">(.*)</a>$', trim($categoryWithLink), $regs);
     list($categoryWithLink, $categoryLink, $categoryShortName, $categoryDescription, $categoryName) = $regs;
 ?>
     

<div>
  <h2>
    <?=$categoryWithLink?>
  </h2>
         
  
  <?php
         $catLoop = new WP_Query();
         $catLoop->query('category_name='.$categoryShortName.'&showposts=1');
           while ($catLoop->have_posts()) {
             $catLoop->the_post();
             
  
  <a href="<?php the_permalink() ?>" title="<?php the_title(); ?>">
               <?php the_title(); ?>
             </a>
         
  
  <?php } ?>
       
</div>
     

<?php } ?>
 

<?php } ?>
</pre>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->