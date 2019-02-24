---
layout: post
title:  "GraphQL Api"
description: |
  I am the author of the GraphQL-Api library on Github. I continue to develop this to make it easier to get started with GraphQL on rails.
---

> View the original Medium post [here](https://hackernoon.com/graphql-api-with-rails-faab252aaffa#.ufxhlt2l9)/

Graphql is an awesome new technology which is making it easier for client

side developers to iterate quickly and batch together network requests.

I really like the promise provided by GraphQl however it is not as easy as rest to get up and running on immediately. This blog post takes a look at how to build a working GraphQL backend in just a few steps using rails.

I am using my own project graphql-api as a framework for building out the GraphQL backend.

We will look at building a basic blogging application. A blog will have an author and some tags.

First create the rails backend.

```bash
rails new blog-api --api
```

Add the necessary libraries to the Gemfile

```ruby
gem 'graphql'
gem 'graphql-api'
```

Create our models

```ruby
rails g model Author name:string
rails g model Blog title:string content:text author:references
rails db:migrate
```

Add our has many relations to author class

```ruby
class Author
  has_many :blogs
end
```

Great! Now we have a basic setup for our blogging backend. Let's add some controllers to serve basic Graphql queries.

Add the following file to app/controllers/graphql_controller.rb.

```ruby
class GraphqlController < ApplicationController
  SCHEMA = GraphQL::Api::Schema.new.schema
  def create
    render json: SCHEMA.execute(
      params[:query],
      variables: params[:variables] || {},
    )
  end
end
```

Add the following route to config/routes.rb

```ruby
resources :graphql, only: :create
```

Now let's test out the new api with curl. Start up the server and run the
following command to see if we have any blog posts

```bash
curl -XPOST -d 'query=query { blogs { id } }' \
     localhost:3000/graphql
{"data":{"blogs":[]}}
```

Let's create an author

```bash
curl -XPOST \
  -d 'query=mutation {
         createAuthor(input: {name: "foobar"}) {
            author { id }
     }}' localhost:3000/graphql
{"data":{"createAuthor":{"author":{"id":1}}}}
```

Now let's create a blog with that author's id

```bash
curl -XPOST \
  -d 'query=mutation {
         createBlog(input: {title: "foobar", author_id: 1}) {
             blog { id }
      }}' localhost:3000/graphql
{"data":{"createBlog":{"blog":{"id":1}}}}
```

Let’s try that first query again, but this time let’s try and return the blog authors as well as the blog name.

```bash
curl -XPOST -d 'query=query {
  blogs {
    id
    title
    content
    author {
      name
    }
  }
}' localhost:3000/graphql
```

You can also run updateBlog mutations as well as updateAuthor mutations. Try deleting an author or blog and see what responses you get back.
