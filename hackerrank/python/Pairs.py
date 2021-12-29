import sys

lines = [line.replace('\n','') for line in sys.stdin]
(N,K) = [int(x) for x in lines[0].split()]

numbers1 = set([int(x) for x in lines[1].split()])
numbers2 = set([int(x)-K for x in lines[1].split()])

print(len(numbers1&numbers2))