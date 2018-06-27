---
id: 1995
title: Alternatives for Maven, Building With Less Frustration
date: 2010-03-02T10:00:03+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1995
permalink: /maven-alternatives/
dsq_thread_id:
  - "71658467"
image: /wp-content/uploads/2010/03/zome_build_system.png
categories:
  - Java and JavaScript
---
Reader <a title="The 90the percentile" href="http://icoloma.blogspot.com/" target="_blank">Nacho Coloma</a> got me thinking. A few weeks ago <a title="Google AppEngine, Vaadin, Spring, a Match Not Made in Heaven" href="http://www.streamhead.com/google-appengine-vaadin-spring-match-heaven/#comment-33273947" target="_blank">he mentioned Gradle as an alternative for Maven</a>. Now I&#8217;m not ready to throw out Maven, but the alternatives are at least interesting. Most popular alternatives have one thing in common: they shy away from XML in favor of domain specific languages (DSLs). Those DSLs are in many cases a subset of some of the more popular scripting languages.

Read on for more about Gradle, Gant, Rake, Raven and Buildr.

## <!--more-->

<a title="Gant" href="http://gant.codehaus.org/" target="_blank">Gant</a>

<img class="alignnone size-full wp-image-1997" title="gant_medium" src="http://www.streamhead.com/wp-content/uploads/2010/03/gant_medium.png" alt="" width="203" height="100" />

_Groovy Ant scripting, no dependency management or extras._

If you&#8217;re still used to Ant build files and presumably doing most of the dependency management by hand, than Gant is probably a great choice for you. It hides the Ant XML that can become very unwieldy and syntax heavy in favor if more focussed Groovy.

That&#8217;s all there is to it. And that&#8217;s the attraction.

## <a title="Gradle" href="http://www.gradle.org/" target="_blank">Gradle</a>

_An up-and-coming star in the build world. Groovy, Ant and Ivy combined._

Wherever you go, Gradle is on the lips of many developers. <a title="Gradle: building with bliss" href="http://technicallypossible.blogspot.com/2010/01/gradle-building-with-bliss.html" target="_blank">Aaron explains it a lot better</a>, but if you like the Groovy syntax and want a little more substance to your build tool than Gant, this might be your best choice.

The result are very small, condensed build files. Reading them feels natural, most of the things I see in the documents, I can guess what it will do. I&#8217;m not sure if writing the files is just as easy (but than again, Maven is difficult both reading and writing the files)

## <a title="Rake - Ruby Make" href="http://rake.rubyforge.org/" target="_blank">Rake</a>

_Ruby Make_

Personally, I must confess, that I found Rake the most inaccessible of the bunch of tools I describe here. I&#8217;m sure it&#8217;s not because of the documentation (<a title="Ruby Rake docs" href="http://docs.rubyrake.org/" target="_blank">there is a lot and most of it pretty clear</a>). <a title="Using the Rake Build Language" href="http://martinfowler.com/articles/rake.html" target="_blank">Even Martin Fowler seems to like it</a>, although the linked document is fairly old.

I think it&#8217;s because Rake files are not only written in Ruby, but it&#8217;s also very focused on Ruby development. I haven&#8217;t really developed much in Ruby, so I think that&#8217;s why some of the most basic constructs look slightly outlandish to me.

I also didn&#8217;t look too deep, because if you want to use Ruby to build Java, there are better options.

## <a title="Raven" href="http://raven.rubyforge.org/" target="_blank">Raven</a>

<img class="alignnone size-full wp-image-1999" title="raven-125x125" src="http://www.streamhead.com/wp-content/uploads/2010/03/raven-125x125.jpg" alt="" width="125" height="125" />

_Java building with Rake_

As the site proclaims, this is really Rake adapted for Java building. It further combines this with Ruby Gems. At its most basic, you could compare this with Maven&#8217;s dependency management. In fact, there is an adapter available that allows you to convert a Maven repository to a Ruby Gem one.

Raven has specific tasks for Java development (javac, war, etc.) which makes it easier to use than plain Rake.

## <a title="Apache Buildr" href="http://buildr.apache.org/" target="_blank">Buildr</a>

<img class="alignnone size-full wp-image-2000" title="buildr" src="http://www.streamhead.com/wp-content/uploads/2010/03/buildr.png" alt="" width="278" height="150" />

_Ruby Java building with Maven repositories_

Buildr is the second Rake spin-off for Java development. For me, it has one major advantage, it uses the Maven repositories directly and also has the &#8220;Maven style&#8221; of specifying dependencies (group, artifact, version, scope). Buildr claims on the front page, it&#8217;s a drop in replacement for Maven. That is a very powerful selling point.

Buildr too is built on Rake, so it&#8217;s pure Ruby, which will take a little getting used to. However loosing the endless xml-tags is something you&#8217;ll probably get used to right-away.

## Conclusion

I think I summed up the most important innovations in Java building, as always, please correct me! If you like Groovy, I&#8217;d suggest Gradle. If you prefer Ruby, go for Buildr (especially if you already have Maven repositories set up). But mind you, none of the others are bad choices, they just serve slightly different purposes than what I am currently looking for in a build tool.

Feel free to use the comments and share your personal preferences.

(<a title="zome tool" href="http://www.flickr.com/photos/shannonpatrick17/2237172765/in/photostream/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->