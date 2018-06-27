---
id: 1188
title: 'Multimedia on the Web: JW FLV Player JavaScript API Tutorial'
date: 2009-06-02T10:00:15+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1188
permalink: /jw-flv-player-javascript-api-tutorial/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/05/jw_flv_player.png
dsq_thread_id:
  - "18194527"
categories:
  - Java and JavaScript
---
If you&#8217;re creating a new media site, you will need a multimedia player rather sooner than later. There are many options available, the easiest is embedding something that already exists. For instance, if you want to put a movie on your site, you could go for a YouTube embedded player. If you want more options, even interactivity, you need something more flexible. You could do much worse than picking <a title="JW FLV Media Player" href="http://www.longtailvideo.com/players/jw-flv-player/" target="_blank">the JW FLV Player</a>.

Before you read on, go ahead and <a title="JW FLV Player Javascript API example" href="http://www.streamhead.com/examples/JWFLVplayer/" target="_blank">open the example</a> to take a look at what we will create.

The player is actually a Flash applet that you can embed in your page. The neat thing, is that it can be completely controlled from JavaScript. There&#8217;s a bunch of information on the website, but it&#8217;s not very clear how it all ties together.

First, you need to initialize the player:

<pre lang="javascript">var so = new SWFObject('jwflvplayer/player-viral.swf','mpl','300','300','9');
so.addParam('allowscriptaccess','always');
so.addParam('allowfullscreen','true');
so.write('player');</pre>

This will put a 300&#215;300 sized player in the div-element with id &#8220;player&#8221;. It won&#8217;t load any songs yet. This we will do in a later step. When the player is done loading, it will call the &#8220;playerReady&#8221; method.

<pre lang="javascript">function playerReady(obj) {
    player = document.getElementById(obj.id);
    player.addControllerListener("PLAYLIST", "playlistLoaded");
    player.addModelListener("ERROR", "error");
    player.addModelListener("STATE", "stateChanged");
};</pre>

In this method, we initialize a few listeners. One is listening to playlist events (fired when new songs are loaded), another will display error messages and the third is used as an example how to display the state of the player. <a title="JW Player events" href="http://developer.longtailvideo.com/trac/wiki/FlashEvents" target="_blank">The JW Player wiki has a full list of all events</a>.

Most of those methods themselves are plain JavaScript, so they are not that interesting, but you can take a look in the source of the example.

The final step to get the player to actually load up a song. It&#8217;s as easy as sending a &#8220;play&#8221; event:

<pre lang="javascript">player.sendEvent("LOAD", "music/"+event.target.innerHTML);</pre>

For all the details, <a title="JW FLV Player Javascript API example" href="http://www.streamhead.com/examples/JWFLVplayer/" target="_blank">take a closer look at the example</a>.

There are many things still missing, but this should get you started. For instance, the player will only play one song at a time and the viral code is not functional (the embedding). But those will be discusses in further posts. And if you have any questions, feel free to leave them in the comments.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->