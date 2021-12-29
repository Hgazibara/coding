from itertools import combinations_with_replacement

S, k = input().split()

print('\n'.join(''.join(c) for c in combinations_with_replacement(sorted(S), int(k))))
