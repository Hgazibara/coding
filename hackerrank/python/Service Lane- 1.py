import sys

N, T = [int(x) for x in sys.stdin.readline().split()]
widths = [int(x) for x in sys.stdin.readline().split()]

def find_max(start, end, widths):
    vehicle = 3
    
    for w in range(start, end + 1):
        if widths[w] < vehicle:
            vehicle = widths[w]
            
    return vehicle

for case in sys.stdin:
    start, end = [int(x) for x in case.split()]
    print(min(widths[start:end+1]))