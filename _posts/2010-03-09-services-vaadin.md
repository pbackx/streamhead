---
id: 2040
title: Obtaining Services and Repositories in Vaadin
date: 2010-03-09T10:00:28+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2040
permalink: /services-vaadin/
dsq_thread_id:
  - "73962001"
image: /wp-content/uploads/2010/03/data_processing.png
categories:
  - Java and JavaScript
---
One problem that you&#8217;ll face in practically any application, including a Vaadin-powered one, is getting hold of data or external services. Usually this functionality is put in some kind of <a title="Service Facade pattern" href="http://www.corej2eepatterns.com/Patterns2ndEd/ServiceFacade.htm" target="_blank">service facade</a>, or for instance a <a title="P of EAA: Repository" href="http://martinfowler.com/eaaCatalog/repository.html" target="_blank">repository</a>. Vaadin presents a problem in this regard, because it uses classes on both client (compiled to JavaScript) and server. You can&#8217;t (and don&#8217;t want to) execute service methods on the browser. Luckily, thanks to modern frameworks and good old Java, this turns out to be incredibly easy.

<!--more-->

If you want to decouple service from client classes, there used to be a time when you would either go for some static factory pattern (please, don&#8217;t) or use some kind of JNDI lookup to get a hold of the service objects or repositories.  In modern times, you&#8217;re probably going for a **dependency injection** container (I like Spring, but the latest JEE6 beans have similar possibilities).

Using Spring, it&#8217;s as simple as defining a service in the Spring configuration and injecting it with the **@Autowired annotation**. With <a title="Maven, Spring, Vaadin and AppEngine, all working together" href="http://www.streamhead.com/maven-spring-vaadin-appengine/" target="_blank">a little setup</a>, <a title="Spring Integration - Vaadin" href="http://vaadin.com/wiki/-/wiki/Main/Spring%20Integration" target="_blank">this works perfectly in Vaadin</a>.

I don&#8217;t think I&#8217;m telling anything new here, neither is the next part, but the combination makes for very non-intrusive, clean code.

If you start adding @Autowired annotations everywhere, you&#8217;ll soon end up with errors: **Vaadin requires that any Java class is serializable**. This is necessary to transmit information between the JavaScript web browser client application and the Java server code. Serialized object are sent between the two, to keep the internal states in sync.

However, many service classes won&#8217;t be serializable. A typical JPA repository will depend on an **entity manager, which is not serializable**.

The solution, is to mark those fields as &#8220;**transient**&#8220;, an often forgotten Java keyword that excludes fields from being serialized (among other things). The great thing about the @Autowired annotation is that it will inject dependencies every time a Java object is constructed. Also when it is de-serialized.

So each time the client sends an object, when it is constructed on the server, it will get autowired with your services.

It&#8217;s just that easy:

  1. Mark your dependencies toward services with **@Autowired**.
  2. Make them **transient** so that they don&#8217;t get serialized.

(<a title="Flickr - data processing" href="http://www.flickr.com/photos/mwichary/2297142523/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->