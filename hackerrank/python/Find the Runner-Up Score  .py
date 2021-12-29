import sys

n = sys.stdin.readline()
print(sorted([int(x) for x in set(sys.stdin.readline().split())], reverse=True)[1])