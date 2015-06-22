def number_property(n):
    return [is_prime(n), is_even(n), is_multiple(n)]
 
def is_prime(n):
    if n < 2:
        return False
        
    for x in xrange(2, n + 1):
        if x*x > n:
            return True
        if n % x == 0:
            return False
    
def is_even(n):
    return n % 2 == 0
    
def is_multiple(n):
    return n % -10 == 0
