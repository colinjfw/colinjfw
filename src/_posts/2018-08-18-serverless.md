---
layout: post
title: "Serverless vs Containerization"
description: |
  Serverless is a brand new paradigm with some very interesting promises. If
  you're like me though, you just got used to containers.
---

Serverless is a brand new paradigm. As a web developer initially, the first
thing that I became used to was `rails new` as a starting point for a project.
This spun up a set of files, databases and base configuration for working on a
project. Containerization, VM's and other new developments in the world of
devops have challenged how we release software but none have significantly
challenged how we build it like serverless.

Serverless, as a paradigm, is confusing. We know it's running on someone's
server somewhere. Serverless, as some have described the term, is just someone
elses server. Others associate the term with primarily the concept of functions.
Functions as a service are programs that both AWS and Google Cloud are providing
as managed platforms to run code. There's truth to both of these definitions.

As I see serverless, it's more synonymous with infinite scaling. The fact that I
can write a function, push it up the code, and that code will now scale
infinitely and elastically based on demand to actually use that code. It
abstracts away packaging and infrastructure from the software development cycle.

I think this removes the confusing concept of 'functions' from serverless.
Functions are a byproduct of the ability to have infinite scaling and a simple
deployment pipeline. Developers can now reasonably package a function and deploy
it. The only reason we would avoid doing this with a more legacy pipeline is
because the overhead just to push a mere function would be too high.

However, you should be able to use serverless for much more than just functions.
I want to be able to run a legacy Rails app or Django application on a
serverless platform, what I get is infinite scaling.

## Why Should I Care for this Definition?

Recently I've been reading views of serverless and functions online and reading
quotes such as this:

> The one exception, of course, being how everybody seems to have come together
> around containers. So now everybody’s excited about containers, but the
> battle’s shifted up. So you’ve won the battle, but lost the war. --
> [Simon Wardley](https://read.acloud.guru/simon-wardley-is-a-big-fan-of-containers-despite-what-you-might-think-18c9f5352147)

The argument here is that serverless and containerization are fundamentally
different technologies and that one will win out over another. Serverless
however, is more of a paradigm. It's a development practice, a way of writing
code and deploying it not tied to one specific implementation. Containerization
on the other hand is merely a way of packaging code.

What we should be thinking about is combining the serverless paradigm of
infinite scaling, simple development and deployment with containerization. This
is how I think about serverless. There are a set of different projects that
are doing this:

* [https://kubeless.io/](Kubeless)
* [https://fission.io/](Fission)
* [https://cloud.google.com/knative/](Knative)

Most of these are based on Kubernetes but they don't have to be. These projects
to me represent the desired state of where development should be going. I want
the best of both worlds, I want to write my Django application, containerize it
and have it scale infinitely. I also want to write a simple API, maybe only 10
lines of Javascript, and deploy it through the same platform.


### My Take

I've written a simple project to test the waters with serverless, if you are
interested, give it a look over [here](https://kubefuncs.com).
