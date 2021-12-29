def sieve(limit):
    flags = [False, False] + [True for x in range(2, limit+1)]
    primes = []
    
    for number, flag in enumerate(flags):
        if flag:
            for multiple in range(number*2, limit+1, number):
                flags[multiple] = False
            primes.append(number)
            
    return primes

primes = sieve(104729)
T = int(input())

for t in range(T):
    print(primes[int(input())-1])