import sys
import re

N = sys.stdin.readline()
tag_pattern = re.compile(r'(<([a-zA-Z0-9]+).*?>)')
sq_attr_pattern = re.compile(r'([a-zA-Z]+)=\'[^\']*\'')
dq_attr_pattern = re.compile(r'([a-zA-Z]+)="[^"]*"')
tags = {}

for line in sys.stdin:
    for found in re.findall(tag_pattern, line):
        tag = found[1]
        tags[tag] = tags.get(tag, set())
        tags[tag] |= set(re.findall(sq_attr_pattern, found[0]))
        tags[tag] |= set(re.findall(dq_attr_pattern, found[0]))

for key in sorted(tags.keys()):
    print("{0}:{1}".format(key, ','.join(sorted(tags[key]))))