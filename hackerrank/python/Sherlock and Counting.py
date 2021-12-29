import math

for t in range(int(input())):
    N, K = [int(x) for x in input().split()]
    D = N*(N-4*K)
    
    if D <= 0:
        print(N-1)
    else:
        sqrtD = math.sqrt(D)
        print(math.floor((N - sqrtD)/2) + (N - math.ceil((N + sqrtD)/2)))