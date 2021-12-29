import heapq

N, K = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]

positions = dict((value, index) for index, value in enumerate(values))

for index, value in enumerate(values):
    if (value != N - index) and K:
        other_index = positions[N - index]
        positions[value], positions[N - index] = other_index, positions[value]
        values[index], values[other_index] = N - index, value
        K -= 1
        
print(' '.join(map(str, values)))
    