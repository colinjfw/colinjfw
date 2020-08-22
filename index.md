---
layout: default
---

<div class="text-center" style="margin-top: 1em;">
  <img src="assets/images/me.jpg" alt="Profile pic" style="border: thick solid #eee; width: 200px; height: 200px; border-radius: 100px; margin: auto;">
</div>

## Colin Walker

Full stack generalist. I currently work at AWS building out the platform I have used and loved for
many years. All opinions expressed in this blog are my own.

My [GitHub](https://github.com/colinjfw) is full of all my fun projects and is
a good representation of the types of programming that I enjoy working on.
I love to play with distributed systems, developer CI/CD tools, building
databases and sometimes hacking my own fitbit.

I have been a sailing instructor for over 6 years and enjoy sailing whenever I
can. I try and keep my passion for teaching throughout my work and enjoy
working on productive and fun teams. I occasionally tutor at Lighthouse Labs.

### Open source projects I'm working on

- [Deliverybot](https://deliverybot.dev): Simple GitHub deployment automation.
- [Battlesnake](https://battlesnake.com): Battlesnake is a fun engaging
  progrmamming game.

## Writing

{% for post in site.posts %}
<div class="post-list-item">
<h4 class="post-list-title"><a href="{{post.url}}">{{post.title}}</a></h4>
<p class="post-list-sub">{{post.date | date: "%Y-%m-%d"}}</p>

{{post.summary}}
</div>
{% endfor %}
