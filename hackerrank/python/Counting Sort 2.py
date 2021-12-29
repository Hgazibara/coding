import sys

n = int(sys.stdin.readline())
ar = [int(x) for x in sys.stdin.readline().split()]

counter = {}

for a in ar:
    counter[a] = counter.get(a, 0) + 1

values = []    

for num in range(0, 100):
    values.extend([str(num)] * counter.get(num, 0))
    
print(' '.join(values))