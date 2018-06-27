---
id: 2152
title: Vaadin Forms and Domain Objects
date: 2010-04-13T10:00:15+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2152
permalink: /vaadin-forms-domain-objects/
dsq_thread_id:
  - "85153330"
image: /wp-content/uploads/2010/04/forms.png
categories:
  - Java and JavaScript
---
One thing that has bothered me with Java development and JEE architectures are form backing objects. You might also know them as data transfer objects or other similar concepts. Basically they&#8217;re pretty much copies of beans you have elsewhere in your application (for instance, database entities). Usually they end up requiring an awful lot of code for managing them. Code that once might have had a reason to exist (remember layers, layers, layers) but only creates overhead in a more modern <a title="Domain drive design in JEE 6" href="http://www.streamhead.com/java-features-enable-domain-driven-design/" target="_blank">domain driven architecture</a>.

If you&#8217;re using Vaadin, <a title="Book of Vaadin - Form component" href="http://vaadin.com/book/-/page/components.form.html" target="_blank">the Form component</a> is you friend in the fight against useless transfer objects.

<!--more-->The Form component in combination with the BeanItem takes any Java class that confirms to the Java bean specs (pretty much anything really) and automatically generates a standard form for you.

Using a <a title="FormFieldFactory" href="http://vaadin.com/api/com/vaadin/ui/FormFieldFactory.html" target="_blank">FormFieldFactory</a> you can adapt the way different fields are shown in the form. It&#8217;s a clear separation of view and data. Easy enough once you&#8217;ve read and follow the examples in <a title="Vaadin promote the toolkit with a book" href="http://www.streamhead.com/vaadin-promote-great-gwt-toolkit/" target="_blank">the Book of Vaadin</a>. The most basic FormFieldFactory implementation will look a little like this:

<pre lang="Java">import com.fctr.ui.invoice.field.ArticleField;
import com.vaadin.data.Item;
import com.vaadin.ui.Component;
import com.vaadin.ui.Field;
import com.vaadin.ui.FormFieldFactory;
import com.vaadin.ui.TextField;

public class SomeFormFieldFactory implements FormFieldFactory {
        @Override
        public Field createField(Item item, Object propertyId, Component uiContext) {
                String pid = (String)propertyId;
                if(pid.equals("somePropertyName")) {
                        return new TextField();
                }
                return null;
        }
}</pre>

Notice that you don&#8217;t have to inject any kind of value into the text field. This is done for you, behind the screen. Great, huh?

It gets a little more complicated when the bean you want to expose via a form has nested beans. Or if you want to create a slightly more complex layout than the simple list. It took me some searching but the great news is, some one has already done most of the hard work for you.

<a title="Vaadin CustomField" href="http://vaadin.com/directory#addon/33" target="_blank">Introducing the CustomField</a>.

Before you dive into your first custom field, you&#8217;d best read up on <a title="Book of Vaadin - Binding components to data" href="http://vaadin.com/book/-/page/datamodel.html" target="_blank">the Vaadin binding model</a>. In Vaadin the data of every component is supplied by containers, properties en items. If you use those interfaces consistently throughout your application, you will notice some kind of magic happening: Fields will stay in sync with the data, bean properties will be updated automatically, components will only be redrawn when needed, etc.

Here&#8217;s an example of a custom field:

<pre lang="Java">import com.vaadin.data.Property;
import com.vaadin.data.util.BeanItem;
import com.vaadin.ui.CustomField;
import com.vaadin.ui.Form;
import com.vaadin.ui.HorizontalLayout;

public class ArticleField extends CustomField {
        private Form form;

        public ArticleField() {
                setCaption("Article");
                form = new Form(new HorizontalLayout());
                setCompositionRoot(form);
        }

        @Override
        public void setPropertyDataSource(Property newDataSource) {
                Article article = (Article)newDataSource.getValue();
                form.setItemDataSource(new BeanItem(article));
                super.setPropertyDataSource(newDataSource);
        }

        @Override
        public Class getType() {
                return Article.class;
        }
}</pre>

This example concerns a bean for which we create a form and inside the bean is another &#8220;Article&#8221; bean. I want to show this in a separate, embedded form on the principal form. Two things are happening in this example:

  * The constructor creates a custom layout. In this case an embedded form inside the form.
  * Setting the datasource on the custom field will inject the Article bean into the form that was created in the previous step.

Updating the value on the principal form will also update the values in the embedded form. Changing a field in the embedded form will update the principal bean. Once again nicely separating the view from your domain object.

Feel free to share your Vaadin tips in the comments, I&#8217;d love the hear them.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->