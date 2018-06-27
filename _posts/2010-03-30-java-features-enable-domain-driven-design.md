---
id: 2125
title: New Java Features Enable Domain-Driven Design
date: 2010-03-30T10:00:52+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2125
permalink: /java-features-enable-domain-driven-design/
dsq_thread_id:
  - "80432112"
image: /wp-content/uploads/2010/03/software_design.png
categories:
  - Java and JavaScript
---
Java has (fairly) recently seen the addition of many new features, whose power is sometimes overlooked. If you have avoided Domain-Driven Design because it involved specific and sometimes archaic editors and clumsy code generation. Now might be the time to take a second look. Annotations, JPA, dependency injection are here to make things a lot easier and with less overhead.

<!--more-->

If you&#8217;re an experienced software developer who follows and experiments with the latest Java features, you might want to skip this post. Basically, a few pieces of a larger puzzle have come together that, I believe, have given Java a better future compared to some of the new languages/frameworks. But you already knew that.

## Java, revitalized

If you look at some &#8220;new&#8221; Java code, annotations are probably the most striking change in comparison to older Java code. Yet for their prevalence, they are easily written off as just a way to add some meta-data. If you don&#8217;t look much further, you&#8217;ll easily overlook their true power, which is the insertion of crosscutting concerns in your programs. Typical crosscutting concerns you&#8217;ll encounter in an enterprise app are logging, security and transactions.

In the past, if you wanted to factor out a crosscutting concern, there were aspects and there was some nasty juggling with static helper classes. Spring&#8217;s dependency injection improved that a bit.

Now most of this is built into Java Enterprise Edition itself. It&#8217;s all been streamlined, improved and made ready for mass consumption.

## Domain Driven Design

Again, in the past if you wanted to do <a title="Domain-driven design - Wikipedia" href="http://en.wikipedia.org/wiki/Domain-driven_design" target="_blank">domain driven design</a> and keep it manageable, there weren&#8217;t many options. MDA tools are one, but I&#8217;ve never really found one that clicked with me. You could do it by hand, but those crosscutting concerns I previously mentioned would interfere. There were things like xDoclet, which helped a lot.

But right now, you can just start from your pojo and build from there. You want persistence? Add JPA annotations. You want some domain logic, you can just start programming (no need to first build a UML model, than generate, than code). Security? There are annotations for that. Need dependencies, like helper classes, injected? Spring does it elegantly without interfering in your code, either via XML or annotations.

If you&#8217;re getting started, <a title="The Java EE6 Tutorial" href="http://java.sun.com/javaee/6/docs/tutorial/doc/javaee6tutv1.html" target="_blank">it&#8217;s a lot</a>, but a JEE6 technology a day keeps the frustrated developer away.

And now we just need to get rid of those getters, setters and other boilerplate (<a title="Project Lombok" href="http://projectlombok.org/" target="_blank">tip</a>).

## The New Style

Basically what it comes down to is this: In the past there were layers, layers and than some layers. In the minimal configuration, you had DAO classes to load your data, service/manager classes to process the data, controllers/actions to prepare and process the view and finally JSPs or whatever view technology your using.

If you program something in Vaadin or many other new component-based frameworks you have your domain objects and your view. The great thing with Vaadin (and others) is that almost everything is written in the same language. Domain objects are even reusable as form data sources. No need for JSP tags, EL expressions, SQL queries (sadly there still is JPAQL), even the XML configuration has been reduced to minimal proportions.

It&#8217;s liberating to be able to focus on just one thing and do it well.

(<a title="method acting in software" href="http://www.flickr.com/photos/dreamsister/2226968084/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->