---
id: 2385
title: Creating PDF File on Google App Engine
date: 2010-07-06T10:00:39+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2385
permalink: /creating-pdf-file-google-app-engine/
dsq_thread_id:
  - "114558477"
image: /wp-content/uploads/2010/07/PDF_on_AppEngine.png
categories:
  - Java and JavaScript
---
As part of an application I&#8217;m working on, I&#8217;d like to create documents in PDF format. I&#8217;ve mentioned this before, but it wasn&#8217;t until last weekend that I actually got started <a title="Java Client for Google Data API" href="http://www.streamhead.com/java-client-google-data/" target="_blank">implementing my solution</a>. The solution consists of generating HTML documents, exporting them to Google Docs and finally, exporting that newly created document to a PDF. Sounds complicated, but it turns out it was actually fairly easy.

<a title="test project using gdata on appengine" href="http://dl.dropbox.com/u/2497061/Examples/test_gdata_appengine.zip" target="_blank"><img class="alignnone size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="" width="30" height="24" />download an example project</a>

<!--more-->The example application consists of three parts:

  * There&#8217;s an RPC servlet that reacts to the user&#8217;s input. It will first use Apache Velocity to create a HTML file based on a template. There are a few things to take care of when running Velocity on App Engine, but nothing showstopping as with many of the other PDF and template libraries. I&#8217;ve used <a title="Combining GAE, Apache Velocity and jQuery" href="http://jvdkamp.wordpress.com/2010/02/12/combining-gae-apache-velocity-and-jquery/" target="_blank">Jurgen van de Kamp&#8217;s explanation and classes</a>. It worked flawlessly.
  * Together with the creation of the HTML, the RPC servlet will also create a new Google Document and send the HTML to the document. You&#8217;ll need to fill in a Google Docs user and password before this part works. Because of Google&#8217;s well documented API&#8217;s, this is a breeze:

<pre lang="java">public DocumentListEntry createNewDocument(String title, String content) throws ServiceException {
	try {
		URL feedUrl = new URL("https://docs.google.com/feeds/default/private/full/");
		DocumentListEntry newEntry = new DocumentEntry();
		newEntry.setTitle(new PlainTextConstruct(title));
		newEntry = client().insert(feedUrl, newEntry);
			
		newEntry.setMediaSource(new MediaByteArraySource(content.getBytes(), "text/html"));
		newEntry = newEntry.updateMedia(true);
		return newEntry;
	} catch (MalformedURLException e) {
		throw new RuntimeException(e);
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}</pre>

  * The final part is a normal (not GWT RPC) servlet that exports the PDF from Google Docs and returns it. I had to use a second servlet because the RPC format is limited. Again this code is very compact:

<pre lang="Java">public InputStream getPdfInputStream(DocumentListEntry document) throws ServiceException {
	String exportUrl = ((MediaContent)document.getContent()).getUri() + "&exportFormat=pdf";
	MediaContent mc = new MediaContent();
	mc.setUri(exportUrl);
	try {
		MediaSource ms = client().getMedia(mc);
		return ms.getInputStream();
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}</pre>

A few things to note:

  * I&#8217;ve only shown a few highlights, you should really download the code to see how little there is to get such a fairly complicated result.
  * I haven&#8217;t really thought too hard about architecture and stuff like exception handling. So you might want to do some tuning if you actually use the code.
  * For this project, I haven&#8217;t use Maven, I just used the Eclipse plugins too quickly generate an application. In fact, it worked so quick I&#8217;m considering dumping Maven. Maven has some serious advantages, but <a title="Maven, Spring, Vaadin, App Engine" href="http://www.streamhead.com/maven-spring-vaadin-appengine/" target="_blank">the number of hoops I have to jump through keeps increasing exponentially</a>. Especially since Google doesn&#8217;t offer their own Maven repositories.

<a title="test project using gdata on appengine" href="http://dl.dropbox.com/u/2497061/Examples/test_gdata_appengine.zip" target="_blank"><img title="download" src="../wp-content/uploads/2008/11/download.png" alt="" width="30" height="24" />download an example project</a>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->