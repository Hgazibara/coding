import re

N = int(input())
pattern = re.compile(r'^[7-9][0-9]{9}$')

while N > 0:
  print('YES' if re.match(pattern, input().strip()) else 'NO')
  N -= 1