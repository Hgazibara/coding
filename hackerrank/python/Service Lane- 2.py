import sys

N, T = [int(x) for x in sys.stdin.readline().split()]
widths = [int(x) for x in sys.stdin.readline().split()]

for case in sys.stdin:
    start, end = [int(x) for x in case.split()]
    print(min(widths[start:end+1]))