import sys

n = int(sys.stdin.readline())
ar_a = [int(x) for x in sys.stdin.readline().split()]
dict_a = {}

m = int(sys.stdin.readline())
ar_b = [int(x) for x in sys.stdin.readline().split()]
dict_b = {}

for a in ar_a:
    dict_a[a] = dict_a.get(a, 0) + 1
    
for b in ar_b:
    dict_b[b] = dict_b.get(b, 0) + 1
    
diffs = []

for k,v in dict_b.items():
    if not k in dict_a or v > dict_a[k]:
        diffs.append(str(k))
        
print(' '.join(sorted(diffs)))