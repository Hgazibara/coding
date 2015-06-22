memory = {}

def exp_sum(n):
    if n < 0: return 0
    if n == 0 or n == 1: return 1

    if n in memory:
        return memory[n]

    factors = []

    for k in xrange(1, n + 1):
        p1 = exp_sum(n - k*(3*k - 1)/2)
        p2 = exp_sum(n - k*(3*k + 1)/2)
        factors.append((-1)**(k + 1) * (p1 + p2))

    memory[n] = sum(factors)
    return memory[n]
