def perimeter(n):
    return 4 * (fibo(n + 2) - 1)

def fibo(n):
    prev, curr = 1, 1
    for x in xrange(1, n):
        prev, curr = curr, prev + curr
    return curr
