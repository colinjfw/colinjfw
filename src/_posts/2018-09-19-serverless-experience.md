---
layout: post
title: "Where is Serverless Going"
description: |
  Serverless has an incredible amount of hype around it right now, where is the
  paradigm and platform going?
---

# Where is Serverless Going

Serverless as an idea has an incredible amount of hype and a huge amount of
tools around it right now. But where is serverless going? How will it evolve
over the next 5 to 10 years?

In a previous post, I discussed the value of serverless as more of an
application paradigm. Serverless is a way in which we write and deploy code, not
a platform or a specific provider. It's not lambda, it could be achieved with
writing code for kubernetes and deployed using containers. 

## Patterns

I've thought about a few different patterns of evolution that I believe
serverless will experience. These are general and not tied to a specific
platform overall.

### 1. Event driven application architectures will become normal and easier

Event driven application architectures are effective for developing generic

### 2. Function composition components will emerge

With more applications rushing in the direction of serverless and functions
being developed, there is a missing middle section. I have a function that
reacts to events to perform some sort of action, imagine a translation function
that will translate values into another language. To use this function, my data
storage layer needs to emit an event so that I can modify the document to add my
new translations. Wiring this all up will require new configurations and
paradigms.

These may even be in the form of new languages. Right now this is done using
static configuration languages like yaml, but the
[https://ballerina.io/](ballerina) programming language is a very interesting 
example of what is to come.

### 3. Kubernetes will probably stay but be heavily hidden

Kubernetes is too complex for most developers. With the emergence of opinionated
event driven application architectures, developers will be insulated from the
complexity of all of the kubernetes yaml files. This is a good thing. Kubernetes
as a platform will likely drive most of the serverless frameworks that will
emerge but developers will work with more code and less config.

### 4. Lambda will lose out in favour of fargate

Lambda and fargate are two aws serverless compute solutions. One runs
containers and one runs code inside specified runtimes. The lambda based
solution is cost effective but limited, functions are required to run in under 3
minutes and are limited in terms of CPU and memory. These types of runtimes will
begin to merge over time. A solution like fargate which runs a generic
application package will begin to become cheaper over time as platforms begin to
run more generic compute platforms.

### 5. Shipping an application will look more like wiring up functions

Shipping a new application that performs common CRUD operations on a set of
resources will look more like wiring up a set of functions. Developers will be
able to deploy their favourite "Auth" function from a marketplace and wire this
up using gateways or workflow engines.

