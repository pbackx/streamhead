---
id: 3394
title: 'Boonex Dolphin Development: Integrating with the Spy Module'
date: 2012-02-19T15:42:45+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=3394
permalink: /boonex-dolphin-spy-module-integration/
amazon_post_template:
  - ""
categories:
  - PHP
---
Boonex&#8217; Dolphin platform is widely used to support various communities. By itself it is fairly full-featured and can, for instance, be used to quickly build a private Facebook clone. It&#8217;s also pretty well programmed and can be extended in various ways. However, its development documentation is lacking. In this post I show how to integrate your module with the Spy module that shows user activity.

<!--more-->

Although not as widely known as, for instance, WordPress, [Boonex&#8217; Dolphin](http://www.boonex.com/dolphin "Boonex Dolphin") is used on many private community sites. It&#8217;s no secret that it is a hit for any kind of dating site, but it can be adapted to any community you want. In this regard, it is a pretty cheap alternative to [Ning.com](http://www.ning.com/ "Ning community sites").

Dolphin can be extended through modules, however the documentation is sorely lacking. [The tutorial is a good start](http://www.boonex.com/trac/dolphin/wiki/DolphinTutorialMyFirstModule "First Dolphin module"), but what follows next took me a lot of backtracing and debugging of existing code.

## The Spy Module

The Spy module is a popular Dolphin module that allows a user to track the activity of his friends and other users. Although it appears to be popular, it is completely undocumented. [This YouTube movie is the best I could come up with](http://www.youtube.com/watch?v=AeVC6dAXqu4 "Installing the Spy module").

Obviously, if you are to try what follows, you need to activate the Spy module (it comes prepackaged with Dolphin)

## Integration

Lets say you have an existing module, and want to see activity from your module on the Spy screens. Here are the different steps you need to take (see the end of this post for a fully example):

### 1. BxDolAlerts

Use BxDolAlerts for every action that you want to track. This has the added benefit that your module will nicely integrate with all other modules that use alerts, not just the Spy one.

You give an alert as follows:

<pre lang="PHP">bx_import('BxDolAlerts');
$alert = new BxDolAlerts('my_module_unit', 'action_name', $objectId, $memberId);
$alert->alert();</pre>

<div>
  The different variables in there are:
</div>

<div>
  <ul>
    <li>
      my_module_unit: this is the unit name to which you want to alert to belong. Pick whatever you like for your entire module, but make sure it&#8217;s unique (I wouldn&#8217;t use things like &#8220;photos&#8221; for instance)
    </li>
    <li>
      action_name: the name of the action the user performed.
    </li>
    <li>
      objectId: this is an id of the object associated with the action. This may be left blank or 0, but it&#8217;s always useful to fill it. For instance, say the user created a new blog post: use the id of that blog post.
    </li>
    <li>
      memberId: the id of the user performing the action.
    </li>
  </ul>
  
  <h3>
    2. Installation
  </h3>
  
  <p>
    At module installation time, the alerts you give are connected to the spy module. This means that whenever you add or change alerts, you need to re-install the module. This can be a hassle for your users, so pick names wisely.
  </p>
  
  <p>
    To enable recompilation of alerts, add &#8220;&#8216;recompile_alerts&#8217; => 1&#8221; to the install section of your config.php.
  </p>
  
  <p>
    The Spy module will also need to update his handlers. This is done in the installer.php file:
  </p>
  
  <pre lang="PHP">function install($aParams) {
    $aResult = parent::install($aParams);
    if($aResult['result'] && BxDolRequest::serviceExists('spy', 'update_handlers')) {
        BxDolService::call('spy', 'update_handlers', array($this->_aConfig['home_uri'], true));
   }
    return $aResult;
}
function uninstall($aParams) {
    if(BxDolRequest::serviceExists('spy', 'update_handlers')) {
        BxDolService::call('spy', 'update_handlers', array($this->_aConfig['home_uri'], false));
    }
    return parent::uninstall($aParams);
}</pre>
  
  <h3>
    3. Spy integration services
  </h3>
  
  <p>
    The final step is adding 2 services to your module. Here are 2 minimal implementations:
  </p>
  
  <pre lang="PHP">function serviceGetSpyData() {
    return array(
        'handlers' => array(
            array('alert_unit' => 'my_module_unit', 'alert_action' => 'action_name', 'module_uri' => 'my_uri', 'module_class' => 'Module', 'module_method' => 'get_spy_post')
        ),
        'alerts' => array(
            array('unit' => 'my_module_unit', 'action' => 'action_name')
        )
    );
}
function serviceGetSpyPost($action, $objectId, $memberId) {
    $spyPost = array();
    switch($action) {
        case 'action_name' :
            $spyPost = array(
                'lang_key' => "action_name was executed"
            );
            break;
    }
    return $spyPost;
}</pre>
  
  <p>
    The first one is used to register the alerts and handlers. Its parameters should be copied from your BxDolAlerts. The second one is called when the spy module wants to render its messages. As you can see, you get the same parameters back as you used when generating the alert. So you can use the objectId to load all details you&#8217;d like to show in the spy message.
  </p>
  
  <p>
    And that&#8217;s really all there is to it.
  </p>
</div>

## Full Example

If the explanation was not enough for you and you&#8217;d like to see a fully working example, I also offer a full module project that you can use as a basis to work on. It does not contain any kind of additional code. Everything in there is shown in the article. It&#8217;s just conveniently all put into one place.

<div class="buynow">
  Full example module with support, lifetime upgrades and 100% money back guarantee, only $5 for immediate download access<br /> [paiddownloads id=&#8221;1&#8243;]
</div>

Future updates might include internationalization (i18n), if there is interest. [Please also see my article on why I charge for some things](http://www.streamhead.com/about/why-buy-from-streamhead/ "Why buy from Streamhead").

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->