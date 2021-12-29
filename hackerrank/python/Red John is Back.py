T = int(input())
cache = {}

def compute(width):
    if width < 4:
        cache[width] = 1
        return 1
    else:
        l, r = width - 1, width - 4
        cache[l] = cache.get(l, None) or compute(l)
        cache[r] = cache.get(r, None) or compute(r)
        
        return cache[l] + cache[r]

def count_primes(n):
    
    A = [False] * 2 + [True] * (n - 2)
    
    for number, is_prime in enumerate(A):
        if is_prime:
            for x in range(number * number, n, number):
                A[x] = False
    
    return sum([1 for x in A if x == True])
        
while T > 0:
    print(count_primes(compute(int(input())) + 1))
    T -= 1