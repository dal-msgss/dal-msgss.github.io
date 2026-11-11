---
title: Executive
---
{% assign terms = site.executive | sort: "year" | reverse %}
{% assign current = terms.first %}

# Executive

Every mathematics or statistics graduate student at Dalhousie is a member of the society. The society administration is run by a council of graduate students, elected at the Annual General Meeting (in early October). See the [constitution and bylaws]({{ '/docs/' | relative_url }}) for details.

## Roles

### President

Leads the society and chairs council and executive meetings. Acts as the society's main spokesperson, advocates for graduate students with the department and on the Lett Bursary Committee, and sets the society's long-term direction.

### Vice-President External

Oversees the society's events and communications. Chairs the Student Events Committee, manages emails, newsletters and promotion, and works with the President as a liaison to outside organizations.

### Vice-President Internal

Manages the society's finances, budget and DSU audit, and chairs the Finance Committee. Takes meeting minutes, maintains the bylaws, acts as the official student advocate on academic and disciplinary appeals, and is the society's liaison with the department administration.

### Program Representatives

Each graduate program (PhD Mathematics, PhD Statistics, MSc Mathematics and MSc Statistics) has one representative, who represents the students in that program on council, serves as a liaison between council and students, and helps plan the graduate seminar.

## Current executive ({{ current.year }})

{{ current.content | markdownify }}

## Past executives

<ul class="talk-list">
{%- for t in terms offset: 1 %}
  <li><a href="{{ t.url | relative_url }}">{{ t.year }}</a></li>
{%- endfor %}
</ul>
