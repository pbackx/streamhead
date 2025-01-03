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

Next you need to manually install wdm [with a specific flag](https://stackoverflow.com/questions/17026441/ruby-how-to-install-a-specific-version-of-a-ruby-gem):

    gem install wdm -v 0.1.1 -- --with-cflags=-Wno-implicit-function-declaration

## Upgrade Github pages

From time to time, there will be enough security warnings that you will want to upgrade the Github pages gem:

    bundle update github-pages

## Running the site locally:

    bundle install
    bundle exec jekyll serve

Open [http://127.0.0.1:4000](http://127.0.0.1:4000)

Todo:
Explain drafts
Add info re IFTTT trigger for scheduled post
