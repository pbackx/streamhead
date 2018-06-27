---
id: 3148
title: Recreating the Ticket to Ride Game in ActionScript 3
date: 2011-04-05T16:00:47+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3148
permalink: /actionscript-3-ticket-to-ride/
dsq_thread_id:
  - "271642909"
image: /wp-content/uploads/2011/04/license-to-journey.jpg
categories:
  - Flash and ActionScript
---
> Creating an ActionScript 3 game: it&#8217;s all fun and games until it actually has to work.

Over the last 3 weeks, I&#8217;ve been trying to recreate Ticket to Ride, one of my favorite board games, in Flash. It&#8217;s been a voyage of triumphs and, ultimately, defeat. In this article, I&#8217;d like to share the code and my experiences with ActionScript 3.

<!--more-->If one is talking about creating a casual online game, there isn&#8217;t much discussion. ActionScript is the language. The most obvious reason is that it compiles to Flash, which runs on any desktop PC in the world and on many mobile devices. iPhone/iPad being the sole major exception, although even that is changing.

I wanted to figure out whether there were other reasons to use ActionScript. And I did find some. <a title="Github License to Journey, a Ticket to Ride clone" href="https://github.com/pbackx/License-to-Journey" target="_blank">But first, let me give you the code. It&#8217;s far from perfect, but you&#8217;re free to extend on it.</a>

What I really liked about ActionScript was the **impressive speed** with which you can **build graphical interfaces**. It&#8217;s very clear that this language is focused on building graphical applications. It was designed for it and you feel that in every possible way. Although the interface of my game isn&#8217;t very advanced, it also didn&#8217;t take any time to program. It just grew out of the way I structured the code.

What I didn&#8217;t like too much was the **absence of more advanced data structures** and ways to process them. It felt pretty awkward to have static typing for everything but the collection types. The contents of those is all dynamically typed. Compare it to Java before generics. Furthermore, I really missed a lot of the more advanced collection operation that a language like Python has.

Overall, I worked about 10 to 12 hours on this game in FlashDevelop. It was a great and motivating experience on the GUI side, but frustrating for the back-end code. In the end, I just couldn&#8217;t convince myself to push on and finish the scoring system for the game. Which is the only thing that&#8217;s really missing. That and much error handling.

I might come back to it later, until then, <a title="License to Journey, inspired by Ticket to Ride" href="https://github.com/pbackx/License-to-Journey" target="_blank">here&#8217;s the code. Have fun with it!</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->