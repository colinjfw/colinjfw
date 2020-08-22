---
layout: default
title:  "Where is Serverless Going?"
summary: Serverless as an idea has an incredible amount of hype and a huge amount of tools around it right now. But where is Serverless going? How will it evolve over the next 5 to 10 years?
---

# Where is Serverless Going?

Serverless as an idea has an incredible amount of hype and a huge amount of tools around it right now. But where is Serverless going? How will it evolve over the next 5 to 10 years?

My interest in this stems from a developers perspective — what will change over the next period of my career because of Serverless. How significantly will it change the way we develop applications or the way in which we package and ship them. In it’s current form, I find Serverless incredibly fun and interesting, but it doesn’t feel like it’s matured fully. We are still at the bottom of a long hill that it will work it’s way up on.

I’ve spent some time collecting patterns and changes that I believe will become prevalent over the next 5 to 10 years with Serverless architectures.

## 1. Event driven application architectures will become normal and easier

Event driven application architectures are effective for developing generic and composable applications. They fit well in distributed systems and with Serverless functions. These applications will have better tooling and more support overall.

Currently, to build a distributed event driven application using Serverless tech takes a lot of planning and some complex architectural decisions. Events are currently not standardized across platforms like AWS and Google cloud. It will take some Devops effort to build these applications. This will continue to get easier and patterns will emerge much more.

CQRS and event sourcing are application architectures that fit nicely in a Serverless world. They model data and applications as separate interdependent components that work together. They also model communication as a flow of information. These architectures will become more common and popular in a Serverless world as they fit better with some of the constructs.

## 2. Function composition components will emerge

With more applications rushing in the direction of Serverless and functions being developed, there is a missing middle section. I have a function that reacts to events to perform some sort of action, imagine a translation function that will translate values into another language. To use this function my data storage layer needs to emit an event so that I can modify the document to add my new translations. Wiring this all up will require new configurations and paradigms.

AWS has jumped on this with step functions. I currently find them very cryptic to use but the kind of service that focuses on composing many disparate Serverless functions I think will emerge. You may be able to build an entire application out of using a composition or workflow service to wire together pre-built functions.

These may even be in the form of new languages. The [ballerina](https://ballerina.io/) programming language is a language specifically designed as a sort of event bus programming language. It has constructs built in to more easily interact with API’s and other event sources. It is the glue code between functions built into a new language.

## 3. Kubernetes will probably stay but be heavily hidden

Kubernetes is too complex for most developers. With the emergence of opinionated event driven application architectures developers will be insulated from the complexity of all of the Kubernetes yaml files. This is a good thing. Kubernetes as a platform may drive most of the Serverless frameworks that will emerge but developers will work with more code and less config.

## 4. Lambda will lose out in favour of Fargate

Lambda and Fargate are two AWS Serverless compute solutions. One runs containers and one runs code inside specified runtimes. The lambda based solution is cost effective but limited, functions are required to run in under 3 minutes and are limited in terms of CPU and memory. These types of runtimes will begin to merge over time. A solution like Fargate which runs a generic application package will begin to become cheaper over time and more synonymous with Serverless.

A container, after all, is really just a packaging format for application code. It may contain more overhead than needed but it’s an incredibly useful format. The ability to run functions with any runtime or set of dependencies will eventually win out over the restricted versions that we see in Lambda today.

## 5. Shipping an application will look more like wiring up functions

Shipping a new application that performs common CRUD operations on a set of resources will look more like wiring up a set of functions. Developers will be able to deploy their favourite “Auth” function from a marketplace and wire this up using gateways or workflow engines. I think that overall once the concept of Serverless matures the benefit it gives to businesses is that developers can select from an incredibly diverse pool of modules to wire together to create their application. This will make development faster and easier.
