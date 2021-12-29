import math

for t in range(int(input())):
    N, num = [int(x) for x in input().split()]
    
    if num >= math.floor(N/2):
        print((N - num - 1)*2)
    else:
        print(num*2 + 1)