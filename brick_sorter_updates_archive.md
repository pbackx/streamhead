---
title: Brick Sorter newsletter archive
date: 2026-03-14T00:00:00+00:00
author: Peter Backx
layout: page
sidebar_link: true
---
Ever since I originally released the plans to my [Lego sorting bot](http://localhost:4000/3d%20printing/ai/2021/11/01/deep-learning-lego-sorting.html) almost entirely build out of Lego,
I have regularly updated the software and the machine itself. And I have started work on a complete
overhaul of the machine.

I have documented all of this in a monthly newsletter (in practice, I send out about 6 newsletters per year). You can read previous editions here, or you can subscribe using the form below.

<div class="ml-embedded" data-form="wXZSvx"></div>


<ul class="posts-list">
  {% for post in site.brick_sorter_updates %}
    <li>
      <h3>
        <a href="{{ post.url | relative_url }}">
          {{ post.title }}
          <small>{{ post.date | date_to_string }}</small>
        </a>
      </h3>
    </li>
  {% endfor %}
</ul>