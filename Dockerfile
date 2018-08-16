FROM ruby:2.4.4
RUN apt-get update && apt-get install -y default-jdk
WORKDIR /usr/src/app
COPY Gemfile Gemfile.lock /usr/src/app/
RUN bundle install
