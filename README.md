# Intro

This is the source for my website at [www.streamhead.com](https://www.streamhead.com/).

# Development

[reference](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

## Install Ruby and Jekyll

For Windows, I have found that [scoop](https://scoop.sh/) is a handy tool:

    scoop install ruby
    scoop install msys2
    msys2
    exit
    ridk install

Now you can install Jekyll and Bundler

    gem install jekyll bundler

## Upgrade Github pages

From time to time, there will be enough security warnings that you will want to upgrade the Github pages gem:

    bundle update github-pages

## Running the site locally:

    bundle install
    bundle exec jekyll serve

Open [http://127.0.0.1:4000](http://127.0.0.1:4000)