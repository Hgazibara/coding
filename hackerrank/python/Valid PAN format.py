import sys
import re

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]
N = int(all_lines[0])
pans = all_lines[1:]

for pan in pans:
	print('NO' if re.match('[A-Z]{5}\d{4}[A-Z]', pan) == None else 'YES')