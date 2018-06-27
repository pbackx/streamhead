---
id: 2062
title: Spring Security Authentication Inside a Vaadin Application
date: 2010-06-01T10:00:26+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2062
permalink: /spring-security-vaadin/
dsq_thread_id:
  - "103071607"
image: /wp-content/uploads/2010/03/spring_security.png
categories:
  - Java and JavaScript
---
Securing Vaadin applications isn&#8217;t as straightforward as it looks. There are a few options already available: The <a title="AppFoundation Vaadin add-on" href="http://vaadin.com/directory#addon/76" target="_blank">AppFoundation add-on</a> provides an authentication module, but it uses statics to access its functions, which I don&#8217;t like and it uses EclipseLink, a technology I have no experience with (and I don&#8217;t think <a title="Will it play in App Engine" href="http://groups.google.com/group/google-appengine-java/web/will-it-play-in-app-engine" target="_blank">it works with the Google AppEngine</a>). A second option is to use <a title="Vaadin incubator SpringApplication" href="http://dev.vaadin.com/browser/incubator/SpringApplication" target="_blank">the Vaadin Spring integration example</a> that shows how to integrate Spring Security. Yet that one only has very course authentication (you&#8217;re either have access to everything or nothing).

So I rolled my own solution.

<!--more-->What I&#8217;d like to have in a security solution:

  1. Build as much as possible on top of existing technology (I choose <a title="Spring Security" href="http://static.springsource.org/spring-security/site/index.html" target="_blank">Spring Security</a>)
  2. Let a user access the application, even if he&#8217;s not logged in.
  3. Provide a popup login window inside the application (no ugly redirects)
  4. Only show items that are available for the user&#8217;s authorization level.
  5. If possible configure this in one central location.

This blog post only goes into how to set up Spring Security and log in a user inside the application (numbers 1 to 3 above). I&#8217;ll do a follow up post in the future with details on point 4 and 5 (but I&#8217;m still struggling with a few bugs between Google AppEngine and Spring Security, see point 4).

Here&#8217;s what you need to do to get started. Some Spring Security knowledge will be necessary to implement this.

## 1. Set up anonymous access to the application servlet

Although this might seem a bit superfluous, the reason I&#8217;m doing this is to make sure I&#8217;m enjoying all the benefit of the default filter chain that Spring Security offers for HTTP integration. Most importantly, the HttpSessionContextIntegrationFilter will manage the SecurityContext for me. This means I don&#8217;t have to worry about clearing it at the end of the request and (possibly) storing it for &#8220;remember me&#8221;-like functionality.

Also, using the &#8220;standard&#8221; way of doing HTTP integration will make sure I can keep up with new Spring Security releases. For instance, I first wanted to roll my own security context invalidation filter, but I noticed the HttpSessionContextIntegrationFilter has been deprecated in favor of the SecurityContextPersistenceFilter. So I ended up going through the slightly more complicated way of setting up anonymous access.

Anonymous access is as easy as setting up an auth-config HTTP security with an intercept URL &#8220;/**&#8221; set to access &#8220;IS\_AUTHENTICATED\_ANONYMOUSLY&#8221;. <a title="Security Namespace Configuration" href="http://static.springsource.org/spring-security/site/docs/3.0.x/reference/ns-config.html#ns-form-and-basic" target="_blank">See the Spring Security documentation for all the dirty details</a>.

## 2. Authentication in code

It&#8217;s fairly easy to do the authentication by yourself. I created a nice Vaadin form for username and password input and used <a title="Using Spring Security in a Swing Desktop Application" href="http://sacrephill.wordpress.com/2009/06/12/using-spring-security-in-a-swing-desktop-application/" target="_blank">this post</a> to authenticate the user. I used the Spring annotation based injection to get to my authentication provider. <a title="Obtaining services and repositories in Vaadin applications" href="http://www.streamhead.com/services-vaadin/" target="_blank">I&#8217;ve detailed this method in a previous post</a>.

This worked like a charm, until I combined it with the anonymous access mentioned above.

## 3. Don&#8217;t use an authentication provider directly, use the manager

Adding anonymous access will cause 2 security providers to be available: one you have defined which connects to whatever you want, and an anonymous one. This meant the dependency injection stopped working, because there were now 2 available implementations and, obviously, the program couldn&#8217;t decide which one to use.

I was glad to encounter this problem, because it actually showed a fault in my logic: in every Spring Security application, there is one authentication manager which will manage the different providers for you, so you really should authenticate via the manager.

Implementing this change was as easy as replacing one variable. The dependency injection did the rest (the authentication manager takes the same arguments as the authentication provider)

## 4. Spring Security & AppEngine

This is not related to Vaadin at all, but you might also be reading my Vaadin posts because I want to deploy everything to Google AppEngine. If you are using AppEngine and Spring Security, don&#8217;t use the latest 3.0.2 release, <a title="Google App Engine - security problem" href="http://jira.springframework.org/browse/SEC-1434" target="_blank">there is a show stopping issue</a>. For now, version 3.0.1 works almost perfectly (<a title="Spring beans annotated with @Secured not serializable" href="https://jira.springsource.org/browse/SEC-1387" target="_blank">you can&#8217;t use @Secured for now</a>).

Example code will be forthcoming once I get all those kinks sorted out. In the meantime, feel free to share any additional tips you might have.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->