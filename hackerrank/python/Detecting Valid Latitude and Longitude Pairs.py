import sys
import re
import math

N = sys.stdin.readline()
pattern = re.compile(r'\([+-]?([0-9](\.[0-9]+)?|[1-8][0-9](\.[0-9]+)?|90(\.[0]+)?), [+-]?([0-9](\.[0-9]+)?|[1-9][0-9](\.[0-9]+)?|[1][0-7][0-9](\.[0-9]+)?|180(\.[0]+)?)\)')

for line in sys.stdin:
    if re.match(pattern, line):
        print('Valid')
    else:
        print('Invalid')