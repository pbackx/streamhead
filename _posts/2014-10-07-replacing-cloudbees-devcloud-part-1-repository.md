---
id: 3717
title: 'Replacing Cloudbees DEV@cloud &#8211; part 1: the repository'
date: 2014-10-07T21:52:17+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3717
permalink: /replacing-cloudbees-devcloud-part-1-repository/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2014/10/Nexus2371-730x305-672x305.jpg
categories:
  - Java and JavaScript
---
I&#8217;m currently using the free DEV@cloud services that CloudBees offers to build and deploy my small side-project. This free service is going away, so I&#8217;m now migrating everything. This is the first small step: setting up a new repository.

<!--more-->

On September the 11th, CloudBees announced that it would be terminating the RUN@cloud service at the end of the year. In small writing in that same mail, they also announced that the free version of DEV@cloud would be discountinued. On September 26, I was moved into the free trial that will end on October 13.

I have two choices: pay for a &#8220;starter&#8221; plan, which, given my usage will be about $65/month. Or move my builds somewhere else.

Since I&#8217;m planning to move my app to OpenShift anyway, I&#8217;m currently trying to migrate everything to that platform. It&#8217;s quite possible that I will fail, but since I want to write a little more on the blog, I want to take you on this journey.

I started simple: setting up a replacement for the CloudBees Maven repositories.

[This tutorial contains about 3 lines of commands that you can just copy and paste and you are done](https://blog.openshift.com/nexus-repository-manager-in-the-cloud-for-free-with-openshift/).

Startup time was very slow, so I&#8217;m not quite sure if the small gear will be able to properly serve Nexus.

Currently I have set up a Jenkins server using the provided Jenkins cartridge, but it looks like this is not aimed at building simple JAR files. It seems to exist specifically for building and deploying to other OpenShift application servers. I hope I can fix this and post about it soon.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->