---
id: 3086
title: 'Integrating Vaadin with Google&#8217;s App Engine Blobstore, an Example'
date: 2011-03-16T16:00:12+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3086
permalink: /vaadin-blobstore/
dsq_thread_id:
  - "255483617"
categories:
  - Java and JavaScript
---
Google&#8217;s AppEngine is a great piece of software. But because of its particular nature, it isn&#8217;t always easy to integrate with existing frameworks such as Vaadin. In this article I take a look at how to **integrate the App Engine Blobstore with Vaadin**. You aren&#8217;t able to use Vaadin&#8217;s standard Upload component so there are some workarounds necessary. This is just one, feel free to share yours in the comments.

<!--more-->I have created a standalone example project that demonstrates the explanation in this article. The example shows how to upload an image to the App Engine Blobstore and associate it with the current user (which is stored in the Datastore). You can use it with Maven, or load the provided Eclipse project files:

[<img class="alignnone size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="" width="30" height="24" />Vaadin / Google AppEngine integration example project](http://www.streamhead.com/wp-content/uploads/2011/03/vaadin-gae-blobstore-example.zip)

Once the file is extracted, change into the folder and simply run:

<pre>&gt; mvn gae:run</pre>

If Maven is correctly installed this will launch the Google AppEngine development server and when launched, you can point your browser to [http://localhost:8888/](http://localhost:8888/ "blobstore & Vaadin example on localhost"). Enter a username which is persisted in the DataStore and in the next step you can upload an image that will get associated with that user.

To use the Google AppEngine Blobstore with Vaadin, you&#8217;ll need the following 5 components:

## 1. Vaadin user management

This example doesn&#8217;t really go into how to deal with users. But to demonstrate the concepts, there&#8217;s a basic user object. It contains a name and an id. The example uses Objectify for easy persistence to the datastore.

The user object also has 2 more field:

  * a blobkey that points to the uploaded image (if any)
  * an uploadkey that is only used during the upload. This is explained later on.

The user object is stored in the Vaadin application&#8217;s user field.

<pre lang="Java">public class User implements Serializable {
  @Id Long id;
  String name;
  String uploadKey;
  String blobKey;

  // skipping getters, setters, constructors, equals and hashcode
	
  public String generateUploadKey() {
    this.uploadKey = String.valueOf(Math.round(Math.random() * 100000f));
    // you probably want something more robust here
    return uploadKey;
  }
}</pre>

## 2. Blobstore upload form

The example reuses the upload form that is used in the Blobstore documentation.

There is one difference: we add a hidden field that contains a randomly generated upload key. This key is also stored with the user object in the datastore. This key will be used by the servlet below.

<pre lang="Java">final String uploadKey = user.generateUploadKey();
final String uploadUrl = BlobstoreServiceFactory.getBlobstoreService().createUploadUrl("/uploadImage");
final Label label = new Label("", Label.CONTENT_XHTML);
</pre>

## 3. Upload servlet

The Blobstore itself is responsible to handle the upload. So we can&#8217;t use the traditional way of uploading multipart formdata. There is no direct access to the bytes. Instead the Blobstore will save the uploaded file and call a servlet. This servlet can access the uploaded blob via a number of parameters in the request.

Because Vaadin hides this request it is difficult to add the handling of the upload to your Vaadin application. I&#8217;m sure it&#8217;s not impossible, but I decided to create a separate servlet.

The servlet does not have access to the Vaadin application and its associated user object. That is why the servlet gets the upload key from the form. It searches the associated user and can then add put the blobkey into the user object.

<pre lang="Java">protected void doPost(HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {
  final Map blobs = blobstoreService.getUploadedBlobs(req);
  final BlobKey blobKey = blobs.get("myImage");
  final String uploadKey = req.getParameter("uploadKey");

  final Objectify ofy = ObjectifyService.begin();
  final User user = ofy.query(User.class).filter("uploadKey", uploadKey).get();
  user.setBlobKey(blobKey.getKeyString());
  ofy.put(user);
        
  resp.sendRedirect("/?refresh");
}</pre>

## 4. Vaadin refresh parameter handler

After the upload servlet has done its work, it redirects the user to the Vaadin application. To make sure the application updates it&#8217;s content, an additional parameter is added to the request URL.

This parameter is intercepted by a parameter handler that&#8217;s responsible for refreshing the Vaadin layout.

<pre lang="Java">@Override
public void handleParameters(Map&lt;String, String[]> parameters) {
  if(parameters.containsKey("refresh")) {
    // refresh the layout ...
  }
}</pre>

## 5. A Vaadin resource for the blobstore

This is a fairly straightforward implementation of the Vaadin ApplicationResource. It makes it easy to integrate blobs into your application.

<pre lang="Java">public class BlobstoreResource implements ApplicationResource {
  // variables skipped
  public BlobstoreResource(String keyStr, Application application) {
    this.application = application;
    this.blobKey = new BlobKey(keyStr);
    this.blobInfo = new BlobInfoFactory().loadBlobInfo(blobKey);
    if (blobInfo == null)
      ; // handle missing blob here
    application.addResource(this);
  }

  @Override
  public String getMIMEType() {
    return blobInfo.getContentType();
  }

  @Override
  public DownloadStream getStream() {
    InputStream inputStream;
    try {
      inputStream = new BlobstoreInputStream(blobKey);
    } catch (IOException e) {
      return null;
    }

    final DownloadStream ds = new DownloadStream(inputStream,
        getMIMEType(), getFilename());
    ds.setBufferSize(getBufferSize());
    ds.setCacheTime(cacheTime);
    return ds;
  }

  // other methods skipped ...
}</pre>

## Conclusion

The example demonstrated the basics for integrating the Google AppEngine Blobstore with a Vaadin application. It was a fully functional example, but beware, before you go to production, you&#8217;re going to want to add a whole lot of error handling.

[<img class="alignnone size-full wp-image-498" title="download" src="http://www.streamhead.com/wp-content/uploads/2008/11/download.png" alt="" width="30" height="24" />Vaadin / Google AppEngine integration example project](http://www.streamhead.com/wp-content/uploads/2011/03/vaadin-gae-blobstore-example.zip)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->