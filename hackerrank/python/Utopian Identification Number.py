import sys
import re

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]

for line in all_lines[1:]:
    print('VALID' if re.match('^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$', line) else 'INVALID')