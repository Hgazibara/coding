import sys

N, K = [int(x) for x in sys.stdin.readline().split()]
toys = sorted([int(x) for x in sys.stdin.readline().split()])
bought = 0

for toy in toys:
    if K - toy > 0:
        bought += 1
        K -= toy
    else:
        break
        
print(bought)