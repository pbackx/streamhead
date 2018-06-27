---
id: 3722
title: 'Migrating Continuous Delivery to OpenShift &#8211; Part 2: Building Java Projects'
date: 2014-10-16T21:28:31+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3722
permalink: /migrating-continuous-delivery-openshift-part-2-building-java-projects/
pdrp_attributionLocation:
  - end
categories:
  - Java and JavaScript
---
[In part 1, I set up a Nexus Maven repository](http://www.streamhead.com/replacing-cloudbees-devcloud-part-1-repository/). In the second part, I wanted to build a number of Java projects on the OpenShift Jenkins instance. Sounds easy enough, but it wasn&#8217;t.

<!--more-->

I thought that this was going to be an easy task. How hard can it be to set up a Maven build on Jenkins? I&#8217;ve done it tens of times before and it was never more complicated than entering the correct repository URL.

OpenShift has a few roadblocks:

  * Because the small gear has limited CPU and memory, builds run on a slave. The OpenShift Jenkins plugin will automatically create build slaves that mirror the server to which you are going to deploy the app. That works fine for web apps that are deployed to OpenShift, but there&#8217;s no default slave available for generic Java builds.
  * Both Git and Maven prefer to put their configuration and temporary files in the user directory. This folder is not writable on the gears. You are supposed to put everything in app-root/data
  * If you run a Jenkins Maven job on a slave, it will try to open a port which it isn&#8217;t allowed.

## Creating a DIY build slave

The OpenShift plugin will automatically launch new gears when required. It will do this based on the &#8220;Application UUID&#8221; or &#8220;Builder Type&#8221; option.

The problem is that there isn&#8217;t a preexisting cartridge that has all the options we need for generic Java builds. So you have to create your own one.

[color-box]**Step 1**: set up a build slave

  1. Start by creating a do-it-yourself (diy-0.1) application. I named it &#8220;build&#8221;
  2. On your Jenkins application add a slave. Configure it as shown below (click for larger version).
  3. Verify that the slave is started and connected.[/color-box]<figure id="attachment_3727" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-3727" src="http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_one-300x108.png" alt="Things to note: the Remote FS Root should point to the data directory of your slave." width="300" height="108" srcset="http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_one-300x108.png 300w, http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_one-1024x369.png 1024w, http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_one-900x324.png 900w, http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_one.png 1053w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_one.png)<figcaption class="wp-caption-text">Things to note: the Remote FS Root should point to the data directory of your slave.</figcaption></figure> <figure id="attachment_3729" style="width: 300px" class="wp-caption aligncenter">[<img class="size-medium wp-image-3729" src="http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_two-300x84.png" alt="You need to explicitly set Java and Maven home since this is not part of the DIY config." width="300" height="84" srcset="http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_two-300x84.png 300w, http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_two-1024x288.png 1024w, http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_two-900x253.png 900w, http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_two.png 1063w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2014/10/slave_configuration_two.png)<figcaption class="wp-caption-text">You need to explicitly set Java and Maven home since this is not part of the DIY config.</figcaption></figure> 

## Making Git behave

If you want to use git to get your projects from repositories such as Github of Bitbucket, you&#8217;ll need to do some tweaking. Git puts its key and known host file in ~/.ssh, however this is not writable.

[There is already a cartridge that gets you part of the way there](https://github.com/smerrill/openshift-community-git-ssh), but it requires an extra tweak.

[color-box]**Step 2**: configure Git

  1. Add the OpenShift SSH cartridge by using this URL: https://cartreflect-claytondev.rhcloud.com/reflect?github=smerrill/openshift-community-git-ssh
  2. Change the git-ssh file in in /usr/bin to the one shown below.
  3. Add your private key to app-root/data/git-ssh/[/color-box]

<pre>#!/bin/bash

KEY="${OPENSHIFT_DATA_DIR}/git-ssh/id_rsa"
KNOWN_HOSTS="${OPENSHIFT_DATA_DIR}/git-ssh/known_hosts"

[ -f $KEY ] && {
  ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=$KNOWN_HOSTS -i$KEY $@
} || {
  ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=$KNOWN_HOSTS $@
}</pre>

## Always use freestyle jobs

It&#8217;s finally time to add a first build job. I started with a Maven job, but [apparently this doesn&#8217;t work. You need to use the free-style project](https://forums.openshift.com/jenkins-failed-to-build-maven-project).

[color-box]In Jenkins, create a freestyle project.

  1. Restrict it to run on your just created slave.
  2. As a build step, add whatever is required, including an &#8220;invoke top-level Maven targets&#8221; step.[/color-box]

## Custom settings.xml for local repo

If you run that build, you&#8217;ll get one final error. Maven puts its local repository in the user folder.

[color-box]The configure the local repository:

  1. In your job configuration, click on the advanced settings of the Maven step.
  2. As settings file choose &#8220;Settings file in filesystem&#8221;
  3. Enter &#8220;$OPENSHIFT\_DATA\_DIR/.m2/settings.xml&#8221;
  4. In app-root/data/.m2 create the below settings.xml[/color-box]

<pre>&lt;settings&gt;
 &lt;localRepository&gt;/var/lib/openshift/&lt;application-id&gt;/app-root/data/.m2/repository&lt;/localRepository&gt;
&lt;/settings&gt;</pre>

That should do it. Next up: deploying build artifacts to our Nexus.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->