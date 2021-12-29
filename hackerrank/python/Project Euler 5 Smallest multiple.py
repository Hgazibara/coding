import math
import operator

def sieve(limit):
    flags = [False, False] + [True for x in range(2, limit+1)]
    primes = []
    
    for number, flag in enumerate(flags):
        if flag:
            for multiple in range(number*2, limit+1, number):
                flags[multiple] = False
            primes.append(number)
            
    return primes

for t in range(input()):
    N = input()
    primes = sieve(N)
    result = reduce(operator.mul, primes, 1)
    
    for base in [2, 3, 5, 7]:
        if base <= N:
            result *= base**(int(math.log(N, base))-1)
    
    print(result)