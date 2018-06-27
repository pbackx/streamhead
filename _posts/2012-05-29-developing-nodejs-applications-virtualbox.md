---
id: 3449
title: Developing Node.JS Applications on Virtualbox Tutorial
date: 2012-05-29T15:54:51+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3449
permalink: /developing-nodejs-applications-virtualbox/
pdrp_attributionLocation:
  - end
image: /wp-content/uploads/2012/05/nodejs_on_virtualbox.png
categories:
  - Java and JavaScript
---
While the Node.JS community is quickly evolving all the libraries and making your life as a developer easier every day. One thing you read little about, is the development environment. Every one uses their own cobbled together thing. To get you started with Node.JS, this post is a step by step guide to creating a full working and reproducible environment that supports deployment to Heroku.<!--more-->

[I&#8217;ve previously sung praise for VirtualBox](http://www.streamhead.com/tag/virtualbox/). It&#8217;s a tool that any developer should have. It will allow you to create an environment that&#8217;s easily portable and can be quickly reproduced by any new developer on the team.

## Step 1. Installing the Operating System

If you&#8217;ve previously created a Linux virtual machine with VirtualBox, you can probably skip this step. But for those new and for my own reference, here are my steps:

  1. Download the latest ISO image of your prefered Linux. I usually just go for Ubuntu because it has the largest community and thus the most chance any issues you may encounter have already been solved.
  2. Create a new virtual machine, everything is default, except
  * mount the Ubuntu ISO image on the CD-ROM controller.
  * create a new automounted shared folder (handy for sending files between both operating systems)
  * 1024 MB of memory is plenty. 512 works too, but it&#8217;s a little more comfortable with some more.
  * the 8GB hard drive space is plenty for all of Node, an Apache server and one or two database engines. If you are going to install anything more, you&#8217;re either going to have to be careful with space (like removing Libre Office), or just make the virtual hard drive 16GB.

  3. Start the new VM
  4. If the CD image is mounted, it should automatically start the Ubuntu installation. This is going to take some time, so grab a coffee.
  5. After your first boot in your newly installed VM, first open the update manager and update everything. At least if you intend on keeping your VM up-to-date, if not, it&#8217;s probably best to disable to automated update checks.
  6. For Heroku, Github, etc access, you should also generate a public/private key pair:
  * ssh-keygen -t rsa

  7. Feel free to install any editor you like. Depending on my mood, I use VIM or [Geany](http://www.geany.org/ "Geany: text editor and ide").

## Step 2. Integrating Guest and Host

<figure id="attachment_3464" style="width: 300px" class="wp-caption alignright"><img class="size-medium wp-image-3464" title="Virtual Reality Center" src="http://www.streamhead.com/wp-content/uploads/2012/05/virtual_reality_center-300x140.jpg" alt="" width="300" height="140" srcset="http://www.streamhead.com/wp-content/uploads/2012/05/virtual_reality_center-300x140.jpg 300w, http://www.streamhead.com/wp-content/uploads/2012/05/virtual_reality_center.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" /><figcaption class="wp-caption-text">With VirtualBox you create a virtual computer, completely isolated from your actual PC</figcaption></figure>
  
Integration between the Ubuntu guest VM and your host will allow you a few nice perks, like being able to use your full screen, exchange files and even seamlessly integrate both systems (if you like this, it&#8217;s not for every one)

  1. Install the VirtualVox Guest Additions from the VirtualBox menu that shows up when your VM is running. Or you can press Host-D (the Host key is associated with the right ctrl button on Windows)
  2. With those additions installed, the shared folder will be mounted. Now you just need to add your user to the correct usergroup so he has access. Open a terminal and type (on the Ubuntu VM):
  * sudo usermod -a -G vboxsf <username>
  * now logout and log back on
  * test your share access with &#8220;ls /media/sf_<sharename>&#8221;

## Step 3. Setting Up and Configuring Node.JS and Heroku

Now we&#8217;re getting close to getting some actual work done. If you don&#8217;t already have a Heroku account and want to follow along, now is the time to sign up.

  1. You can compile Node.JS for yourself. It is a pretty painless operation, but [via the Ubuntu (well, Debian) package manager it&#8217;s even easier](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager):
  * sudo apt-get install python-software-properties
  * sudo apt-add-repository ppa:chris-lea/node.js
  * sudo apt-get update
  * sudo apt-get install nodejs npm
  * sudo apt-get install nodejs-dev (Needed for some of the database drivers)

  2. Test out your install by creating a helloworld.js that contains:
  * console.log(&#8216;hello world&#8217;)

  3. Run: node helloworld.js
  4. [Install the Heroku toolbelt](https://toolbelt.herokuapp.com/linux)
  5. Check the correct installation by login in and adding your key:
  * heroku login
  * heroku keys:add ~/.ssh/id_rsa.pub

  6. And configure your default git e-mail and name:
  * git config &#8211;global user.name &#8220;<username>&#8221;
  * git config &#8211;global user.email &#8220;<useremail>&#8221;

## Step 4. Creating a Minimal CRUD App

<figure id="attachment_3466" style="width: 200px" class="wp-caption alignleft"><img class="size-medium wp-image-3466" title="Create" src="http://www.streamhead.com/wp-content/uploads/2012/05/create-200x300.jpg" alt="" width="200" height="300" srcset="http://www.streamhead.com/wp-content/uploads/2012/05/create-200x300.jpg 200w, http://www.streamhead.com/wp-content/uploads/2012/05/create.jpg 683w" sizes="(max-width: 200px) 100vw, 200px" /><figcaption class="wp-caption-text">CRUD = Create Read Update Delete</figcaption></figure>
  
You&#8217;re now ready to start developing and deploying your Node.JS application. I like to use [RailwayJS](http://railwayjs.com/ "RailwayJS") to get a head start, but there are many many other options.

  * sudo npm install railway -g
  * sudo npm install coffee-script -g (avoids having to download this for every railway applications)
  * railway init blog && cd blog
  * npm install -l
  * railway generate crud post title content
  * railway server 8888
  * open http://127.0.0.1:8888/posts

This will set you up with a minimal CRUD application that uses an in-memory store for all storage.

## Step 5. Configuring & Deploying to Heroku

Before deploying, there are a few steps and tweaks you will want to make.

Adding a Redis session store:

  * <div>
      sudo apt-get install redis-server
    </div>

  * add&#8221;connect-heroku-redis&#8221; : &#8220;>= 0.1.2&#8221; in your package.json
  * in the config/environment.js file:
  * HerokuRedisStore = require(&#8216;connect-heroku-redis&#8217;)(express);
  * app.use(express.session({secret: &#8216;secret&#8217;, store: new HerokuRedisStore }));

  * You may want to replace the secret!

Make sure you are using the latest Node version on Heroku, by adding the following to your package.json:

  * <div>
      &#8220;engines&#8221; : { &#8220;node&#8221; : &#8220;0.6.x&#8221; }
    </div>

You probably want to have git ignore the node_modules folder:

  * <div>
      echo node_modules > .gitignore
    </div>

Set up Heroku as the production environment:

  * <div>
      heroku config:add NODE_ENV=production
    </div>

  * But disable file logging in the Railwayjs production.js file: remove the line &#8220;app.settings.quiet=true&#8221;

I&#8217;m keeping the database configuration for another post, because there&#8217;s just so much choice. But both MongoDB and PostgreSQL can be tested out for free on Heroku and are fairly easy to configure.

The actual deployment looks like this:

  * git init
  * git add .
  * git commit -m &#8220;first version&#8221;
  * heroku create &#8211;stack cedar
  * heroku addons:add redistogo:nano
  * git push heroku master
  * heroku ps:scale web=1
  * heroku open

This should bring up a browser with your deployed application.

During actual development the deployment flow is as simple as:

  * git add <changed file>
  * git commit -m &#8220;commit message&#8221;
  * git push heroku master

## Conclusion

A reliable development environment is the best guarantee that you&#8217;ll not only experiment with Node.JS, but also actually get some work done. Developing in Node will bring back the programmer&#8217;s joy you felt before enormous frameworks and gigantic API&#8217;s.

<div class="buynow">
  If you want a little more assistance, I currently have a special offer running: <a title="dirt cheap node.js web app" href="http://www.streamhead.com/dirt-cheap-node-js-web-apps/">A prototype Node.JS CRUD app for virtually nothing. If you want to get started even faster, check it out</a>.
</div>

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->