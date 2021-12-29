import sys

N = int(sys.stdin.readline())
ar = sorted([int(x) for x in sys.stdin.readline().split()])

min_diff = 1e6
pairs = []

for i in range(0, len(ar) - 1):
    if (ar[i+1] - ar[i]) == min_diff:
        pairs.append((ar[i], ar[i+1]))
    elif (ar[i+1] - ar[i]) < min_diff:
        pairs = [(ar[i], ar[i+1])]
        min_diff = ar[i+1] - ar[i]
        
print(' '.join([' '.join([str(t[0]), str(t[1])]) for t in pairs]))