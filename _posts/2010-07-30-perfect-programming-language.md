---
id: 2447
title: The Perfect Programming Language
date: 2010-07-30T10:00:01+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2447
permalink: /perfect-programming-language/
dsq_thread_id:
  - "123256327"
categories:
  - Java and JavaScript
---
While learning Python, I&#8217;ve also been thinking about what the perfect programming language should look like. So Rob Pike&#8217;s talk at OSCON on the reasons behind <a title="The Go Programming Language" href="http://golang.org/" target="_blank">Google&#8217;s Go</a> came at the perfect time.

<!--more-->It&#8217;s a short 12 minute talk, so you might want to first take a look before reading on.



One of the main things that struck a chord with me in the talk was about type safety. Defining and initializing variables feels like bureaucracy. It&#8217;s like triple filling a credit card application form. And really, why is that necessary? Can&#8217;t the compiler deduce this duplicate information? Programming Java in a modern IDE makes that abundantly clear. Over half of what you type is generated by the IDE (autocompleted initializers and calls; getters, setters, who writes those by hand these days?)

If you take a look at <a title="Parsing Bank Statements in Python" href="http://www.streamhead.com/parsing-bank-statements-in-python/" target="_blank">my first Python program</a>, it&#8217;s a different world. It&#8217;s a fully functional CSV parser in 55 lines and only three of those lines are longer than 80 characters. It does print out the parsed data in a readable way (I could have gone seriously wild in the printed format without making the program any longer) and it&#8217;s fairly easy to read and comprehend. It is pretty much the minimal program you need to get the desired functionality.

If you wrote the same in Java, you might be able to do it in 55 lines, but I can imagine a number of unnecessary complicated constructs in there (file I/O any one? formatting strings?)

I&#8217;m not claiming Python or Go will be our saviors, but it sort of makes you wonder why you&#8217;re wasting half of your time entering characters that are only boiler plate code to make the compiler&#8217;s life easier. It&#8217;s time that could be used to create better designs or add documentation for those that will have to maintain your code.

As an aside, I also started thinking about the patterns quote in the talk. The gist of it was that software patterns are an indication of issues with the programming language you&#8217;re working with. I&#8217;m not sure if this is always the case, but it made me think about the builder pattern. A pattern I like to use when constructors  have too many and too similar arguments (see <a title="Effective Java Second Edition" href="http://java.sun.com/docs/books/effective/index.html" target="_blank">Effective Java, Item 2</a>) However the code you need to write (or generate) to solve such a simple solution is staggering and is often enough to keep me from implementing this feature that makes code a lot more readable. Python&#8217;s keyword arguments and default values are a godsend. I&#8217;m sure you won&#8217;t see any builders in Python to solve this particular issue.

So what do you think is the route to take? Fix up Java with closures and other new bits? Or do we need a new &#8220;standard&#8221; language? And if so, does it even exist?

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->