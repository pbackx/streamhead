---
id: 3196
title: A Google Appengine Staging Server Howto
date: 2011-05-17T16:00:59+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3196
permalink: /google-appengine-staging-server/
amazon_post_template:
  - ""
dsq_thread_id:
  - "306062224"
categories:
  - Java and JavaScript
---
Out of the box, Google&#8217;s App Engine supports versioned deployments. You can switch back and forth between revisions very easily, which is a great feature for properly testing an application before going live. There is one major problem: All versions of the application share the same datastore. So if you&#8217;re migrating your data you run a serious risk of influencing your current production application. Hence the need for **a proper staging environment**.

<!--more-->It&#8217;s no secret, I am a fan of Google&#8217;s App Engine. 

[Once you get used to its peculiarities, it has a number of major advantageous](http://www.streamhead.com/google-appengine-practice/ "Google AppEngine in Practice"). Since I started incorporating some of the continuous integration/lean startup ideas in [my own project](http://www.streamhead.com/launching-my-first-vaadin-appengine-project/ "Launching my FCTR invoicing/bookkeeping project") I&#8217;ve run into the shared datastore issue and the need for a properly isolated staging environment has become apparent.

Here&#8217;s how I did it.

## Setting up the Staging Application

It&#8217;s possible to use namespaces to create an isolated datastore, however I didn&#8217;t want to create additional code for testing. So I took another approach, which I believe is a lot easier and less error-prone:

  1. In the appengine control panel, create a second application. You have 10 free ones so that shouldn&#8217;t be a problem. I added the &#8220;-staging&#8221; suffix to the name of the application under test, so I won&#8217;t mistake one for the other.
  2. If you want to start from a copy of the existing datastore, you can [export the entire datastore using the Python development kit](http://code.google.com/appengine/docs/python/tools/uploadingdata.html "Uploading and Downloading Data"). Even if you&#8217;re using the Java development kit, it&#8217;s worth setting this up. It allows you to make backups of your datastore, which might come in handy when something is really messed up.
  3. Next, import the database into your staging application using the same tool.
  4. And finally, deploy your application to the staging application. If you&#8217;re using Eclipse, just change the application id, if not, you can find the property in the appengine-web.xml.

A small note on using production data in your tests: Be very careful about it. You may want to anonymize some of the data and remove anything that could be remotely confidential.

That should be it. There really wasn&#8217;t much to it, but you now should have a fully functioning copy of your production application. Surf around a little to make sure everything is working swiftly.

When you&#8217;re happy, lets automate it.

## Automating Deployments

[I was about to throw out Maven](http://www.streamhead.com/maven-alternatives/ "Alternatives for Maven, Building with less Frustration"), but I&#8217;ve now created a setup that I&#8217;m pretty happy with. So Maven is here to stay for now. As are the Maven Eclipse plugin and the [GAE plugin for Maven](http://code.google.com/p/maven-gae-plugin/ "maven-gae-plugin").

It&#8217;s thanks to the maven-gae-plugin that I could automate the staging and production deployments. Which has given me a very reproducible build and deployment set up.

To seamlessly create a build for both the staging and production server, I&#8217;m using Maven profiles and its ability to [filter resources while copying them](http://maven.apache.org/plugins/maven-resources-plugin/examples/filter.html "Maven Resources plugin - Filtering").

In the appengine-web.xml I added a gae.application variable:

<pre lang="xml"><?xml version="1.0" encoding="utf-8"?>
&lt;appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
        &lt;application>${gae.application}&lt;/application>
...</pre>

Next up I enabled filtering of the appengine-web.xml (all of the next few bits go into the pom.xml):

<pre lang="xml">&lt;plugin>
    &lt;groupId>org.apache.maven.plugins&lt;/groupId>
    &lt;artifactId>maven-war-plugin&lt;/artifactId>
    &lt;configuration>
        &lt;webResources>
            &lt;resource>
                &lt;directory>src/main/webapp&lt;/directory>
                &lt;filtering>true&lt;/filtering>
                &lt;includes>
                    &lt;include>**/appengine-web.xml&lt;/include>
                &lt;/includes>
            &lt;/resource>
        &lt;/webResources>
    &lt;/configuration>
&lt;/plugin></pre>

In the properties section, I added the default application, which is the staging one. This gives me the assurance that I&#8217;ll always be deploying to the staging environment, unless I really want to go to production:

<pre lang="xml">&lt;properties>
    &lt;gae.application>myapp-staging&lt;/gae.application>
&lt;/properties></pre>

And for the production deployment I created a profile:

<pre lang="xml">&lt;profiles>
    &lt;profile>
            &lt;id>production&lt;/id>
            &lt;properties>
                    &lt;gae.application>myapp&lt;/gae.application>
            &lt;/properties>
    &lt;/profile>
&lt;/profiles></pre>

With this configuration, I can easily run the local development server:

<pre>> mvn gae:run</pre>

Deploy to the staging server:

<pre>> mvn gae:deploy</pre>

And when I&#8217;m happy, deploy it to the production server:

<pre>> mvn gae:deploy -Pproduction</pre>

In addition to the name of the application, you can also configure other properties that differ between a test setup and a production one. For instance, I use the PayPal development servers locally and on the staging server, but the real PayPal site in production.

## Conclusion

With a pretty simple Maven configuration, it&#8217;s possible to create a very reproducible build and deployment environment. Add a continuous integration server and you&#8217;re on your way to the perfect lean setup.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->