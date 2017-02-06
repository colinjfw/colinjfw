---
layout: post
title:  "Raft Algorithm"
description: |
  Raft is a distributed consensus algorithm meant to keep a replicated log of commands sent to a client. These are my attempts at building my own working version.
---

Raft is a distributed consensus algorithm. It provides a mechanism for keeping
a cluster of machines in sync. I had heard about the algorithm while deploying services like Consul at work. I thought it would be a good challenge to learn how to build my own raft implementation.

I ended up with two implementations:

- https://github.com/coldog/new-raft
- https://github.com/coldog/raft

Both of these are missing configuration management and log compaction. I want to try and get these working at some point but have enjoyed playing with and learning from a bar minimum implementation.

### Using GO

For both of these projects I used GO. I have become more excited about the capabilities provided by GO and some of the features of the language. This has become my go to language to build services at this point.
