#!/bin/sh
python2.7 generate_html.py &&
git add index.html &&
git commit &&
git push origin gh-pages
