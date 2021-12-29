import sys

V = int(sys.stdin.readline())
n = int(sys.stdin.readline())
ar = [int(x) for x in sys.stdin.readline().split()]

print(ar.index(V))