---
id: 2639
title: Vaadin Engine, High-Level Framework for Vaadin Applications on Google App Engine, the Security Release
date: 2010-09-14T10:00:52+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2639
permalink: /vaadin-engine-security-release/
dsq_thread_id:
  - "141544803"
categories:
  - Java and JavaScript
---
For those who&#8217;ve been following my GitHub activity, you might have noticed I pushed some big updates on my Vaadin Engine project. The project will become a fully functioning starting point to develop Vaadin and Spring powered applications on Google App Engine. Right now it has integrated most of the Spring Security bits you&#8217;ll need in most projects and it has a basic but very functional approach at internationalization (i18n). All you need to get started is Maven and Eclipse.

<!--more-->This post is a follow up and addition to 

<a title="Spring Security Authentication Inside a Vaadin Application" href="http://www.streamhead.com/spring-security-vaadin/" target="_blank">my previous post on Spring Security in a Vaadin application</a>.

The intent of the project is to create a high-level framework for developing a general <a title="CRUD" href="http://en.wikipedia.org/wiki/Create,_read,_update_and_delete" target="_blank">CRUD</a> Vaadin applications on Google AppEngine. The problem with such frameworks is that they tend to be too tailored at one application. I hope I can avoid that, but please let me know if there&#8217;s functionality missing and I&#8217;ll see what I can do. I know there are a few Vaadin frameworks available that offer lower level functions. I&#8217;ve decided not to use them for various reasons (not compatible with AppEngine, my intended application architecture was too different, etc.).

## Application architecture

Vaadin-Engine is split into two parts:

  * The core which has all the functionality and is your dependency if you want to use the project.
  * A demo application to show how to use everything.

The architecture of the application is based on rich domain objects and you&#8217;ll find the following parts:

  * A domain model (currently only has a User object)
  * A GUI layer, consisting of Vaadin components (currently the most basic main window and a login popup)
  * The Vaadin application that handles some of the crosscutting concerns (i18n and user management)

## Vaadin Engine Security

I&#8217;ve chosen to go with Spring Security because it allows you to plug in a number of existing security providers. It also allows many Java developers to work with familiar API&#8217;s. The application uses a very simple Spring config and handles the authentication internally:

  * Login is done programmatically so the login form can be a nice Vaadin form inside the application.
  * The Vaadin user object of the application is filled to nicely integrate into Vaadin&#8217;s application structure.
  * Role- and user-based authentication is done via function objects that guard different functionality.

Note: initially I wanted to use Spring Security&#8217;s annotation driven security, but this turned out to be too much a hassle. A second advantage is that the security function objects also allow for a better and stronger typed interface.

## Try it out

To try it out yourself, you&#8217;ll need Git (<a title="Windows Git installation" href="http://help.github.com/win-git-installation/" target="_blank">GitHub&#8217;s tutorial is short but very clear</a>), Eclipse and the Google AppEngine plugins for Eclipse.

Next up open Git bash in a directory where you want to get the project:

  1. > git clone git@github.com:pbackx/PoweredByReindeer.git
  2. > cd PoweredByReindeer/
  3. > mvn clean install
  4. > mvn eclipse:eclipe

Start Eclipse and import the existing projects (there should be two projects imported, you won&#8217;t see the parent project).

Right click on the vaadin-engine-demo project and Run As > Web Application (*).

When the server is started point your browser to <http://localhost:8888/> and you should see a login button.

Two logins are available: jimi / jimispassword and bob / bobspassword. Jimi is an admin and will have an admin function (that does nothing but show a message), Bob isn&#8217;t able to see this function (right now he can only log out of the application).

Enjoy, and please comment with suggestions and problems.

(*) The first time you run the application, AppEngine will ask for a webapp directory. You can permanently solve this by going into the demo project properties. Choose Google > Web Application. Select &#8220;This project has a WAR directory&#8221;. Now click on the &#8220;Browse &#8230;&#8221; button and select src > main > webapp. This should permanently solve this pop-up. If any one knows how to set this property via the Maven build file, please let me know how.

## Next up

I am going to eat my own dogfood and integrate this in <a title="FCTR.be eenvoudige vereenvoudigde boekhouding" href="http://www.fctr.be/" target="_blank">my own Vaadin powered application for Flemish entrepreneurs</a>.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->