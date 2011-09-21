cp index.html /tmp &&
git checkout gh-pages &&
rm index.html &&
mv /tmp/index.html index.html &&
git add index.html &&
git commit -m $@ &&
git push origin gh-pages &&
git checkout master
