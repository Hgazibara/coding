from operator import mul

def factorial(n):
    return None if n < 0 else reduce(mul, xrange(1, n+1), 1)
