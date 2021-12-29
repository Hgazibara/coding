import numpy


N = int(input())
a = [[float(v) for v in input().split()] for _ in range(N)]

print(round(numpy.linalg.det(a), 2))
