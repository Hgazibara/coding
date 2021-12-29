import sys
import re

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]
counter = 0

for line in all_lines[1:]:
    if re.search('hackerrank', line, re.IGNORECASE): counter += 1
        
print(counter)