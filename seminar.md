---
title: Seminar
full_title: Dalhousie Mathematics & Statistics Graduate Seminar
permalink: /seminar/
---
{% assign talks = site.talks | sort: "date" | reverse %}

# Dalhousie Mathematics & Statistics Graduate Seminar

Our weekly grad seminar is a chance for graduate students to share their research or other findings in an informal, friendly setting. If you want to give a talk or coordinate a workshop, reach out at [msgss@dal.ca](mailto:msgss@dal.ca).

**Location:** Chase Building, Room 227<br>
**Time:** Thursdays, 4:00-5:00 PM<br>
**Contact:** [msgss@dal.ca](mailto:msgss@dal.ca)

{% assign current = "" %}
{% for talk in talks %}
  {%- assign start = talk.date | date: "%Y" | plus: 0 -%}
  {%- assign month = talk.date | date: "%-m" | plus: 0 -%}
  {%- if month < 7 %}{% assign start = start | minus: 1 %}{% endif -%}
  {%- assign end = start | plus: 1 | modulo: 100 -%}
  {%- if end < 10 %}{% assign end = end | prepend: "0" %}{% endif -%}
  {%- capture label %}{{ start }}/{{ end }}{% endcapture -%}
  {%- if label != current %}{% unless current == "" %}
</ul>{% endunless %}{% assign current = label %}
<h2>{{ label }}</h2>
<ul class="talk-list">{% endif %}
  <li><a href="{{ talk.url | relative_url }}">{{ talk.title }}</a><br><span class="meta">{{ talk.date | date: "%A, %B %-d" }} &middot; {{ talk.speaker }}</span></li>
{%- endfor %}
{% unless current == "" %}</ul>{% endunless %}
