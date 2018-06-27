---
id: 278
title: 'The Beginner&#8217;s Guide to Using Ext with Delicious and Obtaining a Beautifully Interactive Site in no Time'
date: 2008-09-16T10:00:45+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=278
permalink: /integrate-ext-with-delicious/
Image:
  - http://www.streamhead.com/wp-content/uploads/2008/09/integratingextanddelicious1.png
dsq_thread_id:
  - "5437994"
categories:
  - Java and JavaScript
---
In two relatively easy steps I will show you how you can integrate <a title="Delicious, social bookmarks" href="http://delicious.com/" target="_blank">Delicious</a> bookmarks into your sites. A little HTML and JavaScript knowledge is useful. If you have questions, feel free to leave a comment or <a title="mail Peter Backx" href="mailto:peter.backx@gmail.com" target="_blank">mail me</a>. First take a look at my improved prototype site: <a title="Recipebook 2.0 a new way to manage recipes" href="http://recipebook20.com/" target="_blank">Recipebook 2.0</a>. The grid featuring recipes is what we&#8217;ll be creating in this post. <a title="Creating interactive web applications - recipebook 2.0 case study" href="http://www.streamhead.com/build-an-highly-interactive-web-application-in-no-time/" target="_blank">Previous coverage of the site&#8217;s architecture can be found here</a>.

[<img class="alignleft size-full wp-image-286" title="1 hour" src="http://www.streamhead.com/wp-content/uploads/2008/09/1hour.png" alt="" width="20" height="20" />](http://www.streamhead.com/wp-content/uploads/2008/09/1hour.png)Time required: about an hour if you want to try and experiment

As I mentioned, the whole process involves 2 steps:

  1. Getting the data
  2. Displaying the data

There are many ways to do both, so I encourage experimentation.

**Step 1. Getting the data**

[<img class="alignnone size-medium wp-image-280" title="Ext.data usage" src="http://www.streamhead.com/wp-content/uploads/2008/09/extdata-300x155.png" alt="" width="300" height="155" srcset="http://www.streamhead.com/wp-content/uploads/2008/09/extdata-300x155.png 300w, http://www.streamhead.com/wp-content/uploads/2008/09/extdata.png 542w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2008/09/extdata.png)

The data we want is a list of recipes stored as delicious bookmarks. <a title="recipes tag for pbackx on delicious" href="http://delicious.com/pbackx/recipes" target="_blank">You can find the &#8220;normal&#8221; delicious page with my recipes right here</a>. To use this data inside an Ext application, we use <a title="Ext API documentation" href="http://extjs.com/deploy/dev/docs/" target="_blank">the Ext.data package</a> whose usage is shown in the image above. Don&#8217;t panic just yet, it looks complicated, but it really isn&#8217;t.

The store needs 2 components, firstly a proxy to get the data from the Internet and secondly, a reader that knows how the data is structured, and can parse it. For this the reader needs a record definition. All of this, boils down to only a few lines of code:

<pre lang="javascript">deliciousStore = new Ext.data.Store({
        proxy: new Ext.data.ScriptTagProxy({
          url : 'http://feeds.delicious.com/v2/json/pbackx/recipes'
        }),
        reader: new Ext.data.JsonReader({
          }, Ext.data.Record.create([
              { name : 'url',   mapping : 'u' },
              { name : 'title', mapping : 'd' },
              { name : 'description', mapping : 'n'}
          ])
        )
      });</pre>

A few things worth noticing:

  * The ScriptTagProxy is used. This is important because this avoids cross domain warnings in your application. This is a long subject, so I&#8217;m keeping this for later, or you can Google it yourself. Basically if you plan to use any URLs that are not withing your own domain (in this case I use delicious.com from recipebook20.com), you need a ScriptTagProxy.
  * I build the URL based on <a title="Delicious feeds" href="http://delicious.com/help/feeds" target="_blank">the Delicious feed page</a>. It will get the first 15 bookmarks from user &#8220;pbackx&#8221; (me) with tag &#8220;recipes&#8221; and return it in the JSON format.
  * The reader is a JsonReader, exactly because the format downloaded from Delicious is JSON.
  * The record contains the mappings. I figured this out by entering the URL in a browser and looking at the output. It&#8217;s <a title="JSON feed for my recipe bookmarks" href="http://feeds.delicious.com/v2/json/pbackx/recipes" target="_blank">not the most beautiful code</a> in there, but it is pretty straightforward to figure it out. I mapped the fairly nonsensical name &#8220;u&#8221;, &#8220;d&#8221;, and &#8220;n&#8221; onto &#8220;url&#8221;, &#8220;title&#8221;, and &#8220;description&#8221;. If I use the store in my application, I can use the much more meaningful versions.

Now it&#8217;s just a matter of calling

<pre lang="javascript">deliciousStore.load()</pre>

to get all the data into your application.

**Step 2. Using the data.**

Once you got data in a store, there are many things to do with it, here I&#8217;ll show you how to get it in a GridPanel. Here is a simplified version of the GridPanel I use:

<pre lang="javascript">recipesGrid = new Ext.grid.GridPanel({
        height:300,
        width:300,
        title:'recipes',
        store: deliciousStore,
        cm: new Ext.grid.ColumnModel([{
          header: 'Link',
          dataIndex: 'url',
        },{
          header: 'Recipe name',
          dataIndex: 'title',
        }])
      });
      recipesGrid.render('recipeContent');</pre>

When this piece of code is executed, it will create a GridPanel that uses the store we defined as its datasource. There are 2 columns, one showing the URL and another the title (the mapping was also defined in the store). Obviously there are many parameters to tweak the display, but I will leave that up to you.

**See it in action.**

If you want to watch all this in action, I suggest you install Firefox and the <a title="Firebug" href="http://getfirebug.com/" target="_blank">Firebug extension</a>. Open the Firebug display and go to <a title="Recipebook 2.0 a new way to manage recipes" href="http://recipebook20.com/" target="_blank">recipebook20.com</a>. The tabs with interesting information are &#8220;Net&#8221;, where you will see exactly which Delicious feeds are loaded and &#8220;Script&#8221;, which allows you to look at the full JavaScript code.

If you want to get started from a blank slate, <a title="the example" href="http://www.streamhead.com/wp-content/uploads/2008/09/example1.zip" target="_blank">here&#8217;s a zip file with only the code that was discussed in this post</a>. This file does not include the Ext library, you will have to download that one yourself <a title="Download Ext JS" href="http://extjs.com/products/extjs/download.php" target="_blank">on the Ext site</a> and you might need to adapt the path in the index.html to get it to work.

Happy experimenting.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->