# Intro

This is the source for my website at [www.streamhead.com](https://www.streamhead.com/).

# Development

[reference](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

## Install Ruby and Jekyll

It is suggested to run this in WSL. Previously it was possible to run this directly on Windows,
but this seems to be broken now.

Follow the [official instruction](todo):

```bash
sudo apt-get install ruby-full build-essential zlib1g-dev

echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

gem install jekyll bundler
```

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
