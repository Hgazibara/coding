import sys
import re

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]

for line in all_lines[1:]:
    if re.match('^hi [^d]', line, re.IGNORECASE): print(line)