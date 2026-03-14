---
title: Archive of the Brick Sorter Updates newsletter
date: 2026-03-14T00:00:00+00:00
author: Peter Backx
layout: page
---
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