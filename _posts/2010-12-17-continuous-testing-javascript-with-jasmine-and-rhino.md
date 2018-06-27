---
id: 2894
title: Continuous Testing JavaScript with Jasmine and Rhino
date: 2010-12-17T16:00:12+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2894
permalink: /continuous-testing-javascript-with-jasmine-and-rhino/
dsq_thread_id:
  - "192751831"
image: /wp-content/uploads/2010/12/rhino_jasmine_javascript_bdd.png
categories:
  - Java and JavaScript
---
&#8220;I found the shift from thinking in tests to thinking in behaviour so profound that I started to refer to TDD as BDD, or behaviour driven development.&#8221; &#8211; [Dan North](http://blog.dannorth.net/introducing-bdd/)

Jasmine is a BDD framework for JavaScript. It is similar to [easyb, which I mentioned previously in my Eclipse plugins round-up](http://www.streamhead.com/eclipse-plugins/). It does have a few problems: running it involves opening a browser, which is cumbersome when doing continuous integration. The Build Doctor has a solution.

<!--more-->Behavior Driven Development is seeing a surge in popularity right now. And with good reason. It allows you to look at tests in a way that is also fairly understandable to people not directly involved with software development.

Jasmine is one framework that eases BDD for JavaScript. However, running Jasmine behaviors can be cumbersome. In its original configuration, Jasmine requires you to open an HTML page in a browser. If you&#8217;ve ever tried to automate that, you&#8217;ll know there are quite some issues.

In a little magic duct-taping session, [Julian Simpson @ The Build Doctor combines Jasmine and Rhino](http://www.build-doctor.com/2010/12/08/javascript-bdd-jasmine/) (Mozilla&#8217;s JavaScript for Java implementation) with a few choice libraries. The result is JavaScript tests without the browser. Brilliant.

Over the past few months, I&#8217;ve become increasingly interested in [writing good JavaScript](http://www.streamhead.com/javascript-mastery/). In part because I have a feeling JavaScript is going to be the language of the next decade. In a bizarre plot twist. JavaScript has become what Java always aspired to: Available everywhere in a fairly standardized manner. Obviously that means developers are also going to want some of the traditional tools to improve their code, including continuous integration, TDD and now BDD. Which is why I think this little trick could be an important step in increasing JavaScript code quality.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->