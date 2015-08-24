def primeFactors(n):
    factors = findFactors(n)
    return stringifyFactors(factors)


def findFactors(n):
    factors = {}

    for p in xrange(2, n + 1):
        if not isPrime(p):
            continue

        if n <= 1:
            break

        while n > 1 and n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n /= p

    return factors


def isPrime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for p in xrange(3, int(n**0.5) + 1, 2):
        if n % p == 0:
            return False

    return True


def stringifyFactors(factors):
    output = []

    for p in sorted(factors):
        if factors[p] > 1:
            output.append('({0}**{1})'.format(p, factors[p]))
        else:
            output.append('({0})'.format(p))

    return ''.join(output)
