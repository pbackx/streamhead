---
id: 120
title: 'Recipebook 2.0 &#8211; fast prototyping with JavaScript and JSON services'
date: 2008-06-04T10:00:49+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=120
permalink: /recipebook-20-fast-prototyping-with-javascript-and-json-services/
dsq_thread_id:
  - "5437901"
categories:
  - Java and JavaScript
---
<img class="aligncenter size-full wp-image-121" title="recipes" src="http://www.streamhead.com/wp-content/uploads/2008/06/good_health_recipe_book.jpg" alt="" width="285" height="286" srcset="http://www.streamhead.com/wp-content/uploads/2008/06/good_health_recipe_book.jpg 285w, http://www.streamhead.com/wp-content/uploads/2008/06/good_health_recipe_book-150x150.jpg 150w" sizes="(max-width: 285px) 100vw, 285px" />

In a minor revelation, I saw the future of recipes and cook books. Yes, really. However, it&#8217;s so basic I can&#8217;t believe no one has done this before. The <a title="LazyWeb, now closed" href="http://www.lazyweb.org/" target="_self">LazyWeb</a> is long gone, so it looks like I&#8217;m going to have to do it myself.

What I would like is a list of ingredients where I can pick whatever I have left in the fridge and just start cooking. So that&#8217;s how I ended up with <a title="Recipebook 2.0 prototype" href="http://www.recipebook20.com/" target="_blank">my Recipebook 2.0 prototype</a>. Click careful because this really is just a prototype, with many loose nuts and bolts. But it should get the idea across. The building of the prototype might be even more interesting for some. The entire site took me about 5 hours to build, from idea to execution. Honestly, this is much faster than the usual speed at which this kind of stuff is developed in the companies I work(ed).

I am using <a title="my del.icio.us recipes" href="http://del.icio.us/pbackx/recipes" target="_blank">del.icio.us</a> as my database. Added some <a title="Yahoo! helper pipe" href="http://pipes.yahoo.com/streamhead/7Lxs970t3RGOzUHQy6ky6g" target="_blank">Yahoo! Pipes</a> processing in there. And glued it all together with some <a title="Ext.js JavaScript library" href="http://extjs.com/" target="_blank">Ext.js</a>. There&#8217;s no server code at all. Most of the development time went into finding out how to correctly use the <a title="Ext.js api reference on ScriptTagProxy" href="http://extjs.com/deploy/dev/docs/output/Ext.data.ScriptTagProxy.html" target="_blank">ScriptTagProxy</a>. It&#8217;s pretty straightforward, but a little confusing at first. The JavaScript, in general, is not very nice and needs to be cleaned up. But there&#8217;s a lot missing anyway, I really wanted to get a proper recipe submit popup but couldn&#8217;t get it to work without serverside code.

As always, suggestions welcome.

<a title="my Elance profile" href="http://www.elance.com/php/profile/main/eolproviderprofile.php?view_person=pbackx&rid=1B2IO" target="_blank">Services now available via Elance</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->