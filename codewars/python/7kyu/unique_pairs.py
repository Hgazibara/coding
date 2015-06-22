from math import factorial as f

def projectPartners(n):
    return f(n) / f(2) / f(n - 2)
