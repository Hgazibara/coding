import sys

T = int(sys.stdin.readline())

def find_freqs(string):
    freqs = {}
    
    for s in string:
        freqs[s] = freqs.get(s, 0) + 1
    
    return freqs

def find_diff(string):
    strlen = len(string)
    left = string[0:strlen//2]
    right = string[strlen//2:]
    
    leftf = find_freqs(left)
    rightf = find_freqs(right)
    
    counter = 0
    
    for k, v in rightf.items():
        f = leftf.get(k, 0)
        if v > f:
            counter += v - f
    
    return counter

for line in sys.stdin:
    line = line.replace('\n', '')
    if len(line) % 2 != 0:
        print(-1)
    else:
        print(find_diff(line))
    