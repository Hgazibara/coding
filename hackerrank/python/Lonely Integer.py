import sys

N = int(sys.stdin.readline())
input = sorted([int(x) for x in sys.stdin.readline().split()])
repeats = {}

for number in input:
    repeats[number] = repeats.get(number, 0) + 1
    
print(sorted(repeats.items(), key=lambda t: t[1])[0][0])