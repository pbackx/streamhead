---
id: 636
title: 'How to Circumvent Your Cheap Webhost&#8217;s Restrictions: gzipping Without mod_deflate'
date: 2008-12-23T10:00:30+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=636
permalink: /gzipping-without-mod-deflate/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/12/gzip.png
dsq_thread_id:
  - "8764454"
image: /wp-content/uploads/2008/12/gzip.png
categories:
  - Java and JavaScript
tags:
  - recommended
---
An important rule for website optimization is to <a title="Gzip components" href="http://developer.yahoo.com/performance/rules.html#gzip" target="_blank">Gzip everything</a> you send over the wire. The practice of compressing web pages, CSS and JavaScript is supported by most modern browsers. This has two advantages: Smaller files will download faster and less bandwidth will be used on the server.

On most servers, modules exist that can gzip your pages fully transparent. On Apache, the mod_deflate module takes care of this. But what do you do if your server does not have that module installed and you can&#8217;t add it? You get creative.
  
<!--more-->


  
The trick I found on my <a title="Lunarpages - cheap and reliable web hosting" href="http://www.lunarpages.com/id/pbackx" target="_blank">Lunarpages</a> hosted sites, is to pipe all files through PHP, which has a gzip library (called zlib). It&#8217;s not too difficult to get this working, but you do need to know a few things about PHP and mod_rewrite.

## Check Zlib support in PHP

First things first, you&#8217;ll need to make sure that your PHP installation supports the Zlib library. You can do this by creating a small PHP file, as described <a title="Learning Journal - Compress Your Web" href="http://www.desilva.biz/php/zlib.html" target="_blank">in this post</a>.

## Create the PHP compress script

The idea is to pipe all files through this script. The file to compress will be passed as a parameter. Lets say you want to compress the file &#8220;js/myscript.js&#8221;, the URL to use would be: http://yoursite/gzip.php?file=js/myscript.js

Create the following gzip.php script on your server:

<pre lang="PHP"><?php

ob_start( 'ob_gzhandler' );

// this will only work for JS files
header('Content-Type: application/x-javascript');
readfile($_REQUEST['file']);

?></pre>

One thing to note, is that we have to set the &#8220;Content-Type&#8221; of the generated file. This will make sure that the browser correctly identifies the file. In this case we create a Javascript file. If you want to gzip more types, you&#8217;ll need to add some additional logic. For instance, you could check the file extension and generate a different Content-Type based on that.

## Piping the requests to the PHP file

To make everything work, we now need to redirect all requests for JS files to our PHP file. Luckily, there is an easy way to do this, it&#8217;s called mod_rewrite and this module is almost always enabled on Apache installs. It can be configured by creating a .htaccess file and putting it in the root of your site:

<pre lang="DOS">Options +FollowSymlinks
RewriteEngine on
RewriteRule ^/js/(.*js)$ http://yoursite/gzip.php?file=js/$1
</pre>

And that&#8217;s really all there is to it. For <a title="connect your PC to your TV" href="http://www.thecouchtv.com/cablepicker/" target="_blank">my cable picker application</a>, this resulted in a decrease from 3MB to only 800KB, about 30%.

If you have any other tips to circumvent weird restrictions by web hosters, feel free to share them in the comments.

[Image credit](http://flickr.com/photos/revjim/103779409/).

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->