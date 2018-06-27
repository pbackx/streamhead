---
id: 1714
title: Maven Simplifies Seam and Facelets Development, if You Can Handle the XML
date: 2009-12-15T10:00:20+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1714
permalink: /maven-simplifies-seam-facelets-development-handle-xml/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/12/BuildWithMaven.png
dsq_thread_id:
  - "51256814"
image: /wp-content/uploads/2009/12/BuildWithMaven.png
categories:
  - Java and JavaScript
---
As part of <a title="Scanning Documents: Lessons Learned" href="http://www.streamhead.com/scanning-documents-lessons-learned/" target="_blank">my digitization and cleanup effort</a>, I&#8217;m going through a lot of documents. One document I discovered is an old printout of <a title="Coffeecrew.org documents" href="http://coffeecrew.org/documents.html" target="_blank">a Coffeecrew tutorial</a>. The document on Facelets, Seam, NetBeans and Glassfish was their first and last foray into English howto&#8217;s. Which is too bad, because it is high quality and has very good writing.

While reading and trying out the tutorial, I couldn&#8217;t help but think that using Maven could really simplify some of the steps. So I tried it out:
  
<!--more-->

  1. I downloaded and installed the latest <a title="NetBeans" href="http://netbeans.org/" target="_blank">NetBeans Java EE development environment</a>. This comes with Maven support out of the box.
  2. Within the IDE, I created a new project. More specifically a **Maven enterprise application**. If the plugin executes correctly, you will now have 4 projects (ear, ejb, pom and war)
  3. I like to use dependency management in Maven, so I added the following to the pom.xml inside the **pom project**: <pre lang="xml">&lt;repositories>
        &lt;repository>
            &lt;id>jboss-snapshot&lt;/id>
            &lt;name>The JBoss maven repo&lt;/name>
            &lt;url>http://snapshots.jboss.org/maven2&lt;/url>
        &lt;/repository>
        &lt;repository>
            &lt;id>java.net-m1-releases&lt;/id>
            &lt;name>Java.net Maven1 Repository - for javax.faces, javax.el, com.sun.el, and com.sun.facelets releases&lt;/name>
            &lt;url>http://download.java.net/maven/1/&lt;/url>
            &lt;layout>legacy&lt;/layout>
        &lt;/repository>
    &lt;/repositories>

    &lt;dependencyManagement>
        &lt;dependencies>
            &lt;dependency>
                &lt;groupId>org.jboss.seam&lt;/groupId>
                &lt;artifactId>jboss-seam&lt;/artifactId>
                &lt;version>2.2.1-SNAPSHOT&lt;/version>
            &lt;/dependency>
            &lt;dependency>
                &lt;groupId>com.sun.facelets&lt;/groupId>
                &lt;artifactId>jsf-facelets&lt;/artifactId>
                &lt;version>1.1.14&lt;/version>
            &lt;/dependency>
        &lt;/dependencies>
    &lt;/dependencyManagement>
</pre>

  4. Next, it&#8217;s easy to configure the EAR project and its application.xml from within Maven. There&#8217;s no need to write it manually. Add this to the maven-ear-plugin configuration inside the pom.xml of the **ear**: <pre lang="xml">&lt;plugin>
                &lt;groupId>org.apache.maven.plugins&lt;/groupId>
                &lt;artifactId>maven-ear-plugin&lt;/artifactId>
                &lt;version>2.3.2&lt;/version>
                &lt;configuration>
                    &lt;version>5&lt;/version>
                    &lt;modules>
                        &lt;webModule>
                            &lt;groupId>com.streamhead&lt;/groupId>
                            &lt;artifactId>seamhelloworld-web&lt;/artifactId>
                            &lt;contextRoot>/seamhelloworld&lt;/contextRoot>
                        &lt;/webModule>
                        &lt;jarModule>
                            &lt;groupId>org.jboss.seam&lt;/groupId>
                            &lt;artifactId>jboss-seam&lt;/artifactId>
                            &lt;includeInApplicationXml>true&lt;/includeInApplicationXml>
                        &lt;/jarModule>
                    &lt;/modules>
                &lt;/configuration>
            &lt;/plugin>
</pre>

  5. And also add the Seam dependency in both the pom file of the **ear and ejb project**: <pre lang="xml">&lt;dependency>
            &lt;groupId>org.jboss.seam&lt;/groupId>
            &lt;artifactId>jboss-seam&lt;/artifactId>
        &lt;/dependency>
</pre>

  6. You will still need to create the **ejb-jar.xml inside the ejb project** as described in the howto. I don&#8217;t think there&#8217;s a Maven plugin for that. I&#8217;m not sure if that would be very helpful anyway.
  7. Add the Facelets dependency to the **war pom**: <pre lang="xml">&lt;dependency>
            &lt;groupId>com.sun.facelets&lt;/groupId>
            &lt;artifactId>jsf-facelets&lt;/artifactId>
        &lt;/dependency>
</pre>

  8. And that&#8217;s it as far as setup goes. Everything else is 100% development of your application.

The main advantage is that you don&#8217;t have to go around hunting for releases. You don&#8217;t have to extract them and add them to libraries in your IDE. You can just go ahead and start developing.

I think Maven is a great solution for dependency and configuration issues. It does take some getting used to the XML syntax, but once you get through that initial hurdle, Maven is a tool that belongs in any Jave developer&#8217;s tool belt.

Note: Seam doesn&#8217;t work on GlassFish v3, so you will have to stick to v2.1 for the time being.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->