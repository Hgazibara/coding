from itertools import combinations

S, k = input().split()

for r in range(1, int(k) + 1):
    print('\n'.join(''.join(c) for c in combinations(sorted(S), r)))
