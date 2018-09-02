---
layout: post
title: "Building an RDS Operator with the Operator Framework"
description: |
  This goes through building out a Kubernetes operator using the operator
  framework.
---

The [operator framework](https://github.com/operator-framework) from coreos is
a golang library for building operators on Kubernetes. An operator is a control
loop that watches custom resources on Kubernetes and takes some action to create
further resources.

The operator framework does code generation, setup and handles most of the
boilerplate for setting up an operator. Starting a new project involves a simple
`operator-sdk new`. From this we get a set of boilerplate code, a test framework
and Kubernetes manifests. The only major change I made here was to change from
using a set of manifests to making a helm chart.

The project I made with this was a simple rds operator. It watches on a custom
resource definition `Database` and creates an rds database with the same
database configuration.

The [rds-operator](https://github.com/ColDog/rds-operator) project is the result
of this trial.
