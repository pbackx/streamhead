---
id: 3853
title: 'The Jekyll migration cheat sheet (make #3)'
date: 2016-02-15T21:07:22+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3853
permalink: /the-jekyll-migration-cheat-sheet-make-3/
dsq_thread_id:
  - "4582051289"
image: /wp-content/uploads/2016/02/wordpress-to-jekyll-825x510.png
categories:
  - Tools
tags:
  - 2016 Maker Challenge
---
Jekyll is a static site generator. It allows you to run a blog on a minimal server with minimal security worries and no spamming. Because it&#8217;s all based on files, it tends to be a bit more technical than blogging in WordPress. [I&#8217;ve previously written about Jekyll](http://www.streamhead.com/static-site-generator-shootout-jbake-vs-jekyll/), but now it was time to actually migrate a site from WordPress to Jekyll.

<!--more-->

[For those who are following, this is make #3 of the 2016 maker challenge](http://www.streamhead.com/tag/maker-challenge/). There are at least two more ideas for more makes in this post. Let me know if you want to team up 🙂

Last month, I migrated the marketing site of my old side project, [FCTR.be](http://www.fctr.be/).

  1. Everything combined, it took me about 8 hours, spread over 2 weeks. If you do this in one go, it will be quicker.
  2. **Finding a theme** was the major hurdle. The community is much smaller. Even if you want to pay, the options are limited. (Some one should create a WP theme to Jekyll converter)
  3. Migrating content, even custom post types was **smooth**.
  4. **Square bracket special tags** that are used by images and some plugins, were not automatically converted and had to be adapted manually.
  5. Jekyll itself is **well documented**. The template language Liquid also has ok documentation. The interaction between the two was not-so-well documented.
  6. **Permalinks** in Jekyll are very flexible. I didn&#8217;t need to create any rewrites.
  7. **Pagination** in Jekyll is messy. Unless you start developing a Ruby plugin, you can&#8217;t page by category or tags. Because there are a limited number of posts on the site, I resorted to a client-side jQuery plugin.
  8. Free hosting on GitHub has limitations that you may not want to live with.
  9. Why isn&#8217;t there a desktop or web app that wraps Jekyll in a nice UI? It&#8217;s dirt cheap to host and scale Jekyll sites.
 10. Here&#8217;s an overview of the migration process (click for full size):

<a href="http://www.streamhead.com/wp-content/uploads/2016/02/wordpress-to-jekyll-migration.png" rel="attachment wp-att-3854"><img class="aligncenter size-large wp-image-3854" src="http://www.streamhead.com/wp-content/uploads/2016/02/wordpress-to-jekyll-migration-426x1024.png" alt="Wordpress to Jekyll Migration" width="426" height="1024" srcset="http://www.streamhead.com/wp-content/uploads/2016/02/wordpress-to-jekyll-migration-426x1024.png 426w, http://www.streamhead.com/wp-content/uploads/2016/02/wordpress-to-jekyll-migration-125x300.png 125w, http://www.streamhead.com/wp-content/uploads/2016/02/wordpress-to-jekyll-migration-768x1846.png 768w, http://www.streamhead.com/wp-content/uploads/2016/02/wordpress-to-jekyll-migration.png 1200w" sizes="(max-width: 426px) 100vw, 426px" /></a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->