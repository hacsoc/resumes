from collections import namedtuple
import csv
import itertools
from pprint import pprint

import template


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

    template.write_header(html_f)

    for tag_list in template.tag_lists:
        for tag in tag_list:
            template.write_tag(html_f, tag)
        html_f.write('<br/><hr/>')

    template.write_separator(html_f)

    for person in people:
        template.write_person(html_f, person)

    template.write_page_divider(html_f)

    all_tags = sorted(set(itertools.chain(*tag_map.values())))
    for tag in all_tags:
        template.write_tag_header(html_f, tag)
        for person in people:
            if tag in tag_map[person.name]:
                template.write_person_link(html_f, person)
    
    template.write_footer(html_f)
