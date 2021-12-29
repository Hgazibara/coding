import math
import collections

def create_sieve(N):
    sieve = [0] * (N - 1)
    
    for k in range(2, int(math.floor(math.sqrt(N))) + 1):
        if sieve[k - 2] != 0:
            continue
        
        for f in range(k*k, N + 1, k):
            sieve[f - 2] = k
        
    return sieve

def factorize(n, sieve):
    if sieve[n - 2] == 0:
        return [n]
    return [sieve[n - 2]] + factorize(n//sieve[n - 2], sieve)
        

inputs = []
    
for t in range(int(input())):
    inputs.append(int(input()))
    
sieve = create_sieve(max(inputs))

print(sum(sum(factorize(N, sieve)) for N in inputs))
