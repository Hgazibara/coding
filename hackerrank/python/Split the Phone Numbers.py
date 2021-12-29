import sys
import re

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]

for line in all_lines[1:]:
    m = re.match('^([0-9]{1,3})( |-)([0-9]{1,3})( |-)([0-9]{4,10})$', line)
    print('CountryCode={},LocalAreaCode={},Number={}'.format(m.group(1), m.group(3), m.group(5)))