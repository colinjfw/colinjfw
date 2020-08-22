---
layout: default
title: "Causal Consistency: A brief introduction"
summary: As developers most of us have heard of the basic consistency types like eventual consistency and strong consistency. There are, however, a multitude of different consistency models contained in different research papers. One of my favourites that I have been reading into over the last while is causal consistency.
---

# Causal Consistency: A brief introduction

As developers most of us have heard of the basic consistency types like eventual consistency and strong consistency. There are, however, a multitude of different consistency models contained in different research papers. One of my favourites that I have been reading into over the last while is causal consistency.

Causal consistency allows for within the realm of a session or client the reads to be consistent. If I update item A and read the value back I am guaranteed to see the same value. This is if you remember not guaranteed in an eventually consistent model which makes the programming model much more difficult. Causal consistency has the benefit of allowing the programming model to remain pretty much the same as in a strongly consistent model but getting similar availability benefits as an eventually consistent model.

The paper “Bolt-on Causal Consistency” discusses adding a middleware layer to all client transactions that happen against a set of distributed eventually consistent data stores which “bolts-on” a causally consistent view of the data.
> In the bolt-on causal consistency architecture (Figure 2), a shim upgrades an eventually consistent data store (hereafter, *ECDS*) to provide convergent causal consistency. The shim is tasked only with causal safety guarantees, and replication, availability, durabil- ity, and convergence are guaranteed by the *ECDS*. Clients make requests to the shim layer, which handles all communication with an underlying *ECDS *and other clients.

I immediately think of all of the programming applications that I have for this sort of model. Some of the use cases are remarkably simple. A user reads a post on their Facebook news feed and adds a new comment. A background job adds a new row and then generates a report. In both of these cases serializable transaction level isolation is not required and the use case could be satisfied by making the operations explicitly causal thereby allowing the database engine to return the correct results to a user.

Causal consistency is not something I have come across in any production system that I have used (I think?). But it’s something I immediately see the value in. Hopefully I can experiment with a system soon.
