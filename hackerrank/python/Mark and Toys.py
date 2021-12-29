import sys

# read input
input = sys.stdin.readlines()
(N,K) = [int(x) for x in input[0].split()]
toys = [int(x) for x in input[1].split()]

# sort price of toys because the best idea is to keep
# choosing lower-priced toys first
toys = sorted(toys)

counter = 0
max_cost = 0

for toy in toys:
    if max_cost + toy <= K:
        counter += 1
        max_cost += toy
    else:
        break
        
print(counter)