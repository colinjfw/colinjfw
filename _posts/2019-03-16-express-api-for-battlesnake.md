---
layout: default
title:  "Learning to build an Express API for Battlesnake"
summary: Building an API is an important skill for any software developer. In this tutorial we want to build a basic HTTP server that controls a snake like you see in the game board below. All of the snakes in the game have been programmed by individuals like you and run autonomously using play.battlesnake.io.
---

# Learning to build an Express API for Battlesnake

Building an API is an important skill for any software developer. In this tutorial we want to build a basic HTTP server that controls a snake like you see in the game board below. All of the snakes in the game have been programmed by individuals like you and run autonomously using [play.battlesnake.io](https://play.battlesnake.io).

Battlesnake is a version of the Snake game you found on old cellphones, and MS-DOS computers before that. It’s very much the same game, except multiple snakes are on the same board at once and each snake is controlled by a live web server. Snake servers implement commands receiving board information for every turn and responding with “up”, “down”, “left”, or “right” to control their snake. You can begin Battlesnake using simple algorithms, and build up to more and more complex solutions over time.

![](https://cdn-images-1.medium.com/max/2000/1*EPJNR1Lb-DtAgrlwdzQFZw.gif)

This tutorial will help you get started building your own Battlesnake and help you learn some of the tools and fundamentals of API design.

## Before we begin…

You should have some beginner JavaScript knowledge and have a general idea of what Node.js is.

You will need the following installed:

* Node.js® — a JavaScript runtime built on Chrome’s V8 JavaScript engine

* npm — a popular package manager, used for JavaScript projects

* Git — a popular version control system

* Your favourite text editor

* A terminal shell

* A text editor for writing code

## Let’s get started!

First, let’s open our terminal and get a new npm project started:

    mkdir battlesnake-api
    cd battlesnake-api
    touch index.js

We just created a directory for our snake server and an empty file inside it (index.js) which will hold our snake logic. Next, initialize npm so that we can install any necessary packages. It will prompt you for some information about your project, but the defaults will work for now.

    npm init

For this tutorial we’ll be using Express, one of the most widely-used server-side HTTP JavaScript libraries. Because of it’s amazing documentation and ease-of-use, it’s a great starting point! Run the below command to install Express into our project.

    npm add express --save

Now that we’ve added Express, let’s begin using it in our index.js file:

<iframe src="https://medium.com/media/5d37c33d01f0d36c0571a2f35f1825ff" frameborder=0></iframe>

The above is a basic Express server. We can run this server by executing `node index.js`. This should print out the message “Listening on port 3000” in your terminal window if it was successful.

Now, to test our server, start a new terminal instance and execute the following command:

    curl [http://localhost:3000](http://localhost:3000)

This command should print out “Cannot GET /” in the terminal window. This means that the server is running and working correctly! Curl is a utility used often for interacting with HTTP servers and can be used for debugging issues with them. We will use it throughout this tutorial for testing the endpoints in our server’s API.

## Deploying

Before we go any further, deploying our snake API to the internet is a key part of getting started. It’s much better to figure out how to deploy early, so we can test our snake easily as we go. You can deploy Battlesnake servers to any cloud platform, but for the sake of simplicity and ease-of-use we will use [Heroku](https://www.heroku.com/). Heroku is a platform that will run your code inside their infrastructure and give you a URL to access it. Setting up an account is easy and free to get started!

To deploy to Heroku, install their [CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) tool and run the following commands:

    heroku create
    git push heroku master
    heroku open

## Adding Battlesnake API Endpoints

Now that we’ve deployed our code, let’s add the necessary endpoints to our API . Snakes need to implement four endpoints to play the game: /start, /move, /end, and /ping:

<iframe src="https://medium.com/media/a512ca87b1cafe94713bc9b38e97e528" frameborder=0></iframe>

Each endpoint represents a command used to control our snake using code (like in the image above). Of the four commands, the most important is the /move command. In the above app we’ve built a snake that only moves right on a game board (you can see “right” on line 10). The next step is to start programming logic to control which direction the snake should go. Can we make it turn up when it gets near a wall? I think we can, but let’s save that for another post!

## Signing up

Now that we’ve built and deployed a basic node snake server, head over to [play.battlesnake.io](https://play.battlesnake.io) and register your snake to play against other developers!

## Looking for more?

Here are some simple links to get you started:

* Documentation with “zero to snake” instructions:[ docs.battlesnake.io](https://docs.battlesnake.io)

* Node starter snake:[ github.com/battlesnakeio/starter-snake-node](https://github.com/battlesnakeio/starter-snake-node)

* You can find the rest of the starter snakes for various languages here: [https://github.com/battlesnakeio/community/blob/master/starter-snakes.md](https://github.com/battlesnakeio/community/blob/master/starter-snakes.md)
