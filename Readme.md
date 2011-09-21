The Résomatic
=============

* `data.csv`: Tab-separated data from the web form (see `generate_html.py` for order)
* `generate_html.py`: Python 3 script to generate `index.html` from `data.csv`
* `template.py`: HTML format strings and tag lists for the left sidebar

Deploying
=========

This repository uses [Github Pages](http://pages.github.com/) to host the
static HTML output of the script. The deployment process is basically:

    git checkout master
    cp index.html /tmp/index.html
    git checkout gh-pages
    mv /tmp/index.html index.html
    git push origin gh-pages
