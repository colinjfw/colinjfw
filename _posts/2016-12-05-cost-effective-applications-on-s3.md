---
layout: default
title:  "How to Run Cost Effective Frontend Applications on S3"
summary: This post is about maintaining single page applications in the cloud.
---

# How to Run Cost Effective Frontend Applications on S3

A large part of my professional life involves cleaning up and maintaining infrastructure and doing devops for Team MuseFind. This post is about that part, maintaining single page applications in the cloud.

I want to describe the evolution of Musefind’s frontend tech stack on AWS. Specifically moving from Docker and ECS to using S3 exclusively for managing our frontend applications. Overall, in moving to S3 we achieved better developer productivity and an easier to manage platform without sacrificing any of the features we enjoyed while using Nginx. Some of these tools are relatively unknown in the community and I wanted to show our journey here.

## Nginx and Containers

Our deployment stack originally started out as an Nginx based setup on the new container service from AWS. We liked this originally; we built docker images and could distribute those docker images throughout our dev, staging and production environments. It also allowed us a great deal of freedom, I am very familiar with Nginx configurations and pretty much anything you need from a frontend application server can be handled with Nginx.

Each application also had its own load balancer. We also has fault tolerance and blue green deployments, we could run at least two instances of an application and upgrade incrementally, only routing traffic when health checks were passing. This piece is handled automatically by ECS.

Overall, our team was happy with the setup. It was relatively quick to push to production and we were able to trigger updates to the application only when the health checks were passing.

### High Cost

For a startup, load balancers aren’t the best way to burn through your hard earned cash. Even though I loved our setup and felt comfortable with it, I was beginning to question how heavyweight it was. We shouldn’t have to pay for an individual load balancer for every frontend application. This was also a blocker to productivity. That pet project that we wanted to show to the rest of our team was relegated to localhost because we couldn’t justify the cost for a load balancer for a small internal application.

Additionally, it was a fully custom setup. We had some downtime simply due to the fact that there were a lot of moving pieces and we were managing a large amount of them. Configuration mixups and even typo’s were common. For a small team, my goal is to remove as much devops work as possible, and this setup involved a significant amount of care.

With four machines and four load balancers dedicated to solely our single page applications, we were simply spending too much to host static assets.

## S3 and Cloudfront

In our search for a better, more devops friendly setup, I began looking at hosting our site on S3. I had read some documentation as well as some blog posts about the advantages of hosting on S3. Initially, I didn’t think that it was the right place for a single page application.

Our requirements for a hosting solution were as follows:

* Browser caching for all assets.

* Serving a single index file for all requests.

* Full SSL support, with redirect from http to https.

* Zero downtime deploys. It shouldn’t take longer that a few minutes to deploy.

Browser caching was a big request from a service that I view as an object store. Also, serving a single index file for every request seems out of the scope of what S3 has to offer without digging into complicated XML configurations which just looked painful. I wasn’t optimistic going into the project.

### Enter Cloudfront

Cloudfront is Amazon’s CDN. It distributes your static assets around the world to get faster response times. Cloudfront also has a host of, somewhat hidden, features that make it a first class choice for deploying your frontend application.

A key feature is the integration with the AWS certificate service, which allows you to get SSL on your site for free with no configuration. That’s right, free. If you don’t manage your DNS with route53 I don’t believe this is possible, however this may be a reason to switch (view Mark’s response below for a summary of the capabilities of AWS Certificate Manager).

Cloudfront also has some error handling features that allow us to control the error pages and error codes that will be returned to a client. This became an essential feature for us. This is how we solved serving the index page by default. We simply set error handlers to convert a 403 to a 200 and to return an index page. At first I thought this was a hack and was nervous about putting it into production, however after running this setup for over 6months I’m convinced that if this is a hack, it’s one that works very well.

Now, if you’re counting cloudfront has knocked down a few of our requirements, however a couple remain, namely, zero downtime deployments and fine grained control over browser caching.

### Enter S3 Website, A Ruby Gem

S3 does support adding cache control headers to your resources, but who is going to update all of their assets manually? For a small website this is a likely scenario but we want to push easily two or three times a day without adding too much overhead to the process.

While browsing github one day I found a real gem by the name of [s3_website](https://github.com/laurilehmijoki/s3_website). It promised to handle a few things for us, uploading assets to S3, and dealing with some cloudfront specificities, however, it’s main selling point for us was it’s ability to gzip everything and set cache control headers on an entire group of resources easily.

This gem has proved essentially to our daily workflow. The simple configuration options combined with the speed and reliability has proved a big win in terms of productivity for our frontend developers. Currently all pushes to our four frontend sites use this gem for the critical upgrades.

With all of this in place, I was able to instruct cloudfront to use the cache headers from the S3 resource, allowing us to have fine grained control over cache headers. Specifically, everything under the assets path is cached forever.

![](https://cdn-images-1.medium.com/max/2000/1*0i0uDCNs3-OcJinCEuyEtQ.jpeg)

### **A Complete Setup**

With all of this in place, we have ticked all the boxes by hosting our website on S3. Today, if you visit any of Musefind’s sites you can see this setup in action. We have very fast page load times with full browser caching for all of our assets. We push code daily which involves simply updating some assets in S3 as well as issuing cloudfront invalidations. We also have full SSL support without touching a single cert file.

## Getting Started With S3 Website

To get started on this yourself, I recommend getting the s3_website gem and following the documentation. In total, the configuration for creating a fully functioning website with cloudfront and S3 looks like this:

    # s3_website.yml

    s3_id: <%= ENV['AWS_ACCESS_KEY'] %>
    s3_secret: <%= ENV['AWS_SECRET_KEY'] %>
    s3_bucket: musefind.com

    site: build

    index_document: index.html
    error_document: index.html

    cache_control:
      "static/*": public, max-age=60000000
      "*": no-cache, no-store

    gzip: true

    cloudfront_distribution_id: <YOUR_DIST_ID>
    cloudfront_distribution_config:
      aliases:
        quantity: 1
        items:
          CNAME: musefind.com

    cloudfront_invalidate_root: true
    cloudfront_wildcard_invalidation: true

We keep something like this in the root of your repositories, with different file’s for staging and production environments. We also upload frequently small test projects without incurring any significant costs. This has been a big boost in productivity.

## Conclusion

We now run a very cheap setup for our frontend applications with a heavy emphasis on developer productivity and speed to deploy. It takes us only a few minutes to get changes live to any of our four main websites. This has proven a big advantage in both bugfixes and keeping our frontend developers happy.

Although it may be tricky to figure out, I encourage switching to S3 if you can. It takes some time to build up the resources and knowledge to run cloudfront and S3 together, but for the lean startup I think it’s a much superior approach to the conventional one of managing Nginx or Apache servers.

Please let me know if you have any comments or questions!
