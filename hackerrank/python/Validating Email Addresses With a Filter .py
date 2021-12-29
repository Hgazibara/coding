import re

data = []
pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$')
N = int(input())

while N > 0:
    data.append(input().strip())
    N -= 1
    
print(sorted(list(filter(lambda x: re.match(pattern, x), data))))