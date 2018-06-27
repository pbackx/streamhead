---
id: 3164
title: How to Run Your WordPress.org Blog Locally for Experimentation and Fun
date: 2011-04-27T16:00:55+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3164
permalink: /wordpress-locally/
dsq_thread_id:
  - "289687855"
amazon_post_template:
  - ""
image: /wp-content/uploads/2011/04/wordpress-logo-stacked-rgb.png
categories:
  - Java and JavaScript
tags:
  - virtualbox
---
If you have a WordPress.org blog and want to try a new plugin or a new look, you have two options: You could just install it on your running production site and risk crashing it. Or you could first experiment with it on a different test installation. Ideally this test system would resemble the real site as closely as possible. I think you can guess which one is the right way and which is the one most people go for. This article show how to copy your existing blog to a local computer and run it there, so you don&#8217;t have to fear trying out something new.

<!--more-->This tutorial requires some technical knowledge. How to set up a LAMP/WAMP stack, FTP files and use phpmyadmin. Nothing very complicated, but if you don&#8217;t feel comfortable doing it, I&#8217;d gladly help you out and create a fully working VirtualBox image of your blog for $50 (I&#8217;ll also support you in setting up VirtualBox).

([why buy from Streamhead?](http://www.streamhead.com/about/why-buy-from-streamhead/ "Why buy from Streamhead?"))

## Step 0. Prerequisites

This tutorial won&#8217;t work for WordPress.com hosted blogs, only for self-hosted WordPress.org blogs. You will need to have an FTP account that can access your WordPress installation files. Every host offers this, so check your hosting details and keep the FTP url, login and password ready.

You will also need to export your database. The easiest way is via phpMyAdmin. I haven&#8217;t seen a host that doesn&#8217;t offer this super-useful application. A link to it is usually located in the control panel of your hosting account.

## Step 1. Operating environment

Depending on your preferences, there are a wide range of operating systems and environments you can work with.

  * If you&#8217;re used to Windows and you like to keep it simple. You can install everything on Windows.
  * If you want to create something portable, I suggest running some kind of virtualization software. <a title="VirtualBox Keeps Your Development Environment Tidy" href="http://www.streamhead.com/virtualbox/" target="_blank">I&#8217;m a fan of VirtualBox</a>.

Basically, pretty much any operating system will do, but I like to create a virtual <a title="Ubuntu" href="http://www.ubuntu.com/" target="_blank">Ubuntu system</a> in VirtualBox. It&#8217;s a great way to keep the server software that you&#8217;ll install in step 2 away from your &#8220;normal&#8221; operating environment. Shut down the virtual machine and you don&#8217;t need to worry about system processes that keep using memory and CPU that you forgot to shut down.

## Step 2. LAMP

While there are other ways to run WordPress, the easiest way is to install the Apache web server, MySQL database and PHP language. It&#8217;s the same environment that your blog host uses, so this is the best way to reproduce identical conditions.

  * If you&#8217;re on Windows, you can go for <a title="WAMP, an acronym that actually makes developers' lives easier" href="http://www.streamhead.com/wamp-acronym-developers-lives-easier/" target="_blank">one of the many WAMP distributions</a>.
  * For Ubuntu there is an <a title="Ubuntu Server Guide" href="https://help.ubuntu.com/10.10/serverguide/C/index.html" target="_blank">in depth guide to setting up a server</a>. Keep in mind that you don&#8217;t need to go through the whole guide. You only need to install Apache2, MySQL and PHP5. I also suggest to add phpMyAdmin while you&#8217;re installing. It isn&#8217;t strictly necessary but will make copying the database easier.
  * If you&#8217;re on Mac, <a title="MAMP, Mac, Apache, MySQL, PHP" href="http://www.mamp.info/en/index.html" target="_blank">there&#8217;s MAMP</a>.

## Step 3. Copy WWW directory

Now it&#8217;s time to do the actual work. First you need to copy all the blog files locally:

  * Figure out where the local Apache server stores its files. On Ubuntu this will be in /var/www. Many WAMP distributions offer shortcuts to this directory.
  * Next open an FTP client. I like <a title="21 programs to have on your Windows PC" href="http://www.streamhead.com/21-programs-pc/" target="_blank">FileZilla</a>, but feel free to pick the one you like.
  * Connect to your blog&#8217;s FTP site and navigate to the WWW directory. Usually it&#8217;s called &#8220;www&#8221;, sometimes &#8220;public_html&#8221; or something similar. There should be 3 directories in there that start with wp (wp-admin, wp-content and wp-includes) plus a bunch of .php files that also start with wp and then a number of miscellaneous files.
  * Download this entire directory into your local www directory. This might take some time, especially if you have been blogging for a while, have many plugins/themes and/or have uploaded a lot of files.

You can already perform steps 4 to 7 while the download continues.

## Step 4. The Database Connection

In the WWW directory, open the file &#8220;wp-config.php&#8221;. You will see a number of lines that start with &#8220;define&#8221;. There&#8217;s one that defines the name of your database, it&#8217;s &#8220;DB\_NAME&#8221;. Write down the name after that. By default it&#8217;s going to be &#8220;wrdp&#8221;, but this can vary. Also write down the values for DB\_USER and DB_PASSWORD. You may have entered those at some point but might have forgotten them. Or they could be autogenerated when WordPress was installed.

## Step 5. Export the database

Fire up phpMyAdmin on your remote host.

  * In the right part of the screen, you&#8217;ll see a number of tabs.
  * One of those is &#8220;Export&#8221;. Click that one.
  * You&#8217;ll see a screen divided into two sections: &#8220;Export&#8221; and &#8220;Options&#8221;.
  * In the &#8220;Export&#8221; section select the database name that you wrote down in step 4.
  * You don&#8217;t need to change anything in the &#8220;Options&#8221; section.
  * If you have a large database, select &#8220;gzipped&#8221; compression at the bottom of the screen. This can reduced the file size by a lot (mine was only 30% of the original, uncompressed file)
  * If you like, you can pick a nice name for the download.
  * Click &#8220;go&#8221; and remember where you save the file.

## Step 6. Import the Database

Now we are going to import this file into your local database.

  * Fire up phpMyAdmin locally. Again, your AMP distributions will come with a shortcut to it. On Ubuntu you&#8217;ll find it at <a title="Local phpMyAdmin" href="http://localhost/phpmyadmin/" target="_blank">http://localhost/phpmyadmin/</a> by default.
  * This time pick the &#8220;Import&#8221; tab. It&#8217;s right next to the &#8220;Export&#8221; one.
  * Browse and select the file you just saved.
  * Press &#8220;go&#8221;.

## Step 7. Set Up the Database User

Now we need to configure the WordPress database user. Remember you wrote down the name and password in step 4.

  * In the left section of phpMyAdmin, where it shows the databases, you should now see your imported WordPress database.
  * Click on it and it will show the tables in that database.
  * Now click on the &#8220;Privileges&#8221; tab.
  * Enter the username and password.
  * As host enter * or localhost.
  * Check all privileges (this will give global privileges, you could also give the user only access to the WordPress database. Since this is a local test system I&#8217;m not too worried about strict security, but keep this in mind)
  * Click &#8220;go&#8221; to create the user.

## Step 8. First Test

Surf to <a title="Local WordPress install" href="http://localhost" target="_blank">http://localhost</a>

You should see the blog appear, but you might notice it downloads all images from your original blog site. All links will also still point to the Internet, not to the local site. You won&#8217;t be able to log into the administration.

## Step 9. Converting to Localhost

You didn&#8217;t leave phpMyAdmin, did you?

  * In the left column, click on your blog database (if it isn&#8217;t already showing)
  * Browse the &#8220;wp_options&#8221; table (it&#8217;s the first tiny actions icon)
  * Find the two options with option_name &#8220;siteurl&#8221; and &#8220;home&#8221;. There are many ways to do this, phpMyAdmin has a search function or you could change the SQL query if you know what you&#8217;re doing.
  * Change both options (with the little pen icon) so that their &#8220;option_value&#8221; reads &#8220;http://localhost&#8221;

## Step 10. You&#8217;re Done

That&#8217;s it. You now have a fully functioning local copy of your WordPress.org blog.

## Common Issues

### When importing the database you receive an error that the file is too large.

In many cases, it might be beneficial to first <a title="Optimize WordPress for shared hosting" href="http://www.streamhead.com/wordpress-shared-hosting/" target="_blank">clean up your database</a>. Also make sure you enable gzip compression. If none of those help, you will need to <a title="PHP File Upload Configuration" href="http://www.radinks.com/upload/config.php" target="_blank">change the default PHP file upload limit</a>.

### Categories or article links don&#8217;t work

Depending on your permalink structure, you need to have the &#8220;mod_rewrite&#8221; Apache module enabled. I&#8217;m not sure why, but this isn&#8217;t always on by default. There are numerous articles about it if you Google. For instance <a title="Enable mod_rewrite on Apache 2 for Ubuntu" href="http://www.ghacks.net/2009/12/05/enable-mod_rewrite-in-a-ubuntu-server/" target="_blank">here&#8217;s a howto for Ubuntu</a>.

### Can&#8217;t add/configure plugins and themes and other permission issues.

Again, depending on how your installation is configured, the Apache/PHP process may not have permissions to change or add files in your WWW directory. If you don&#8217;t care about security, I suggest a &#8220;chmod -R 777 *&#8221; in your WWW directory. If you do care, find the group that the Apache process runs in and give that group write access to the entire WWW directory.

### Something else

I haven&#8217;t run into this issue, but I can imagine there are plugins that won&#8217;t like to be moved to a different server. If you see strange issues, try to disable your plugins and enable them one by one. If you find the culprit, maybe you need to change its options in the wp_options database table.

## Conclusion

Having a full copy of your blog on your own computer is a great resource to experiment with new themes or plugins. Although it might look daunting, once you&#8217;ve done this procedure, you won&#8217;t know why you didn&#8217;t try this earlier.

If you&#8217;re not very technical, or don&#8217;t feel like going through all the steps, I offer a $50 service for creating a VirtualBox Ubuntu image. Feel free to <a title="Contact me for more information" href="http://www.streamhead.com/contact/" target="_blank">contact me for more information</a>, or you can go straight to PayPal (VirtualBox setup is included).

([why buy from Streamhead?](../about/why-buy-from-streamhead/ "Why buy from Streamhead?"))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->