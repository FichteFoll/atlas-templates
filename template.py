#!/usr/bin/env python2

import dmsl

import yaml
with open("ryze.yaml") as f:
    data = yaml.load(f)
# data = {"min_width": "1000px"}

html = dmsl.parse('template.dmsl', **data)

with open("ryze.html", 'w') as f:
    f.write(html)

print("template run successfully")
