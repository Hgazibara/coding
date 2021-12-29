import itertools

A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]

print(' '.join(map(str, itertools.product(A, B))))
