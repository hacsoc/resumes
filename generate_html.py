from collections import namedtuple
import csv
import itertools
import re

import jinja2

from tag_lists import tag_lists


def sanitize_tag(t):
    return re.sub('[^a-zA-Z_]', '', t)


def render(name, *args, **kwargs):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    t = env.get_template(name)
    with open('index.html', 'w') as f:
        f.write(t.render(*args, **kwargs))


# Define column names for easy CSV translation
Wizard = namedtuple('Wizard', ['timestamp', 'name', 'major', 'tags', 'url',
                               'email'])


# Open one file for reading CSV and one for writing HTML
with open('data.csv') as csv_f, open('index.html', 'w') as html_f:

    # Read data into list, omitting first row which is the header
    reader = csv.reader(csv_f, delimiter='\t')
    people = sorted([Wizard(*row) for row in reader][1:],
                     key=lambda p: p.name.split()[-1])

    # namedtuple is immutable, so transform the comma-separated tag string
    # into a set and store it in a dictionary
    tag_map = {p.name: [t.strip().lower() for t in p.tags.split(',')]
               for p in people}

    # for each tag, show links to all the people under it
    all_tags = sorted(set(itertools.chain(*tag_map.values())))

    sanitized_tags = {t: sanitize_tag(t) for t in all_tags}
    sanitized_names = {p.name: sanitize_tag(p.name) for p in people}
    tag_people = {tag: [p for p in people if tag in tag_map[p.name]] for tag in all_tags}

    render('template.html', **locals())
