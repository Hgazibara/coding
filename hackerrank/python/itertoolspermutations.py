from itertools import permutations

S, k = input().split()

print('\n'.join(''.join(p) for p in permutations(sorted(S), int(k))))
