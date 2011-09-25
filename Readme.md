The Résomatic
=============

* `data.csv`: Tab-separated data from the web form (see `generate_html.py` for order)
* `deploy.sh`: Generate HTML, commit, upload
* `generate_html.py`: Python 3 script to generate `index.html` from `data.csv`
* `index.html`: Generated page
* `tag_lists.py`: Manually curated sidebar tags
* `template.html`: jinja2 template for the page

Deploying
=========

This repository uses [Github Pages](http://pages.github.com/) to host the
static HTML output of the script. To deploy, just run `deploy.sh`. It's an
extremely simple script. Switch to the `gh-pages` branch to use it.
