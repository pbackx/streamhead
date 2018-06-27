---
id: 2550
title: Generating PDF files on Google App Engine
date: 2010-08-27T10:00:46+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2550
permalink: /pdf-on-google-app-engine/
dsq_thread_id:
  - "134277104"
image: /wp-content/uploads/2010/08/itext_pdf_on_appengine.png
categories:
  - Java and JavaScript
---
A while ago, <a title="Creating PDF file on Google App Engine" href="http://www.streamhead.com/creating-pdf-file-google-app-engine/" target="_blank">I explained the way I was going to create PDF files on Google AppEngine</a>. Turns out that, once I started to really test this solution, there were a few holes in my strategy. Well actually, there was only one, but it was a major one: importing HTML files into Google Docs is a mess. Hardly any of the HTML formatting is preserved by Google Docs. You might get away with a little right align and bold here and there, but any table is completely ruined, as are some more advanced formatting options.

So I set out to find another solution.

<!--more-->Turns out there are 

<a title="Open Source PDF libraries in Java" href="http://java-source.net/open-source/pdf-libraries" target="_blank">quite a few Java libraries that support PDF</a>. Although none of them seems to be in widespread use or have any sizable community. Except for one: <a title="iText, a free and open source Java PDF library" href="http://itextpdf.com/" target="_blank">iText</a> and the reporting engine build on top, <a title="JasperForge: generate pdf reports" href="http://jasperforge.org/projects/jasperreports" target="_blank">JasperReports</a>.

I would have loved to use JasperReports as this would suite my need perfectly, but from my searches it appears there&#8217;s no way to get it to run on Google App Engine and there&#8217;s also little interest by the JasperReports developers to do so (at least, that was what I understood from <a title="JasperReports needs AWT" href="http://www.mail-archive.com/google-appengine-java@googlegroups.com/msg01023.html" target="_blank">this message</a>)

So my only option was to use the basics. iText has a number of issues on Google AppEngine, but those are mainly with inserting images into PDFs, something which I don&#8217;t yet have the need for. I ran a few tests and, if you don&#8217;t use the &#8220;offending&#8221; code, there&#8217;s no need to make custom builds of iText. You can just grab the one from <a title="iText downloads on SourceForge" href="http://sourceforge.net/projects/itext/" target="_blank">the iText jar from downloads page</a>.

Be warned, if you are going for the latest iText. There have been a few refactorings (recently?) that make many of the existing tutorials outdated. Most of them will still work upto a certain level. For instance, I found <a title="geek-tutorials - itext" href="http://www.geek-tutorials.com/java/itext/itext_index.php" target="_blank">these iText tutorials</a> very helpful to get me started. However, if you really want to get into the latest version of iText, it seems you&#8217;ll have to buy the early access version of the book.

BTW, if I should ever return to converting HTML to PDF, I think &#8220;<a title="xhtmlrenderer: xhtml to pdf" href="https://xhtmlrenderer.dev.java.net/" target="_blank">The Flying Saucer Project</a>&#8221; is a great start. Although it only supports xHTML and doesn&#8217;t seem to be very actively developed, all users agree that it&#8217;s a pretty great library.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->