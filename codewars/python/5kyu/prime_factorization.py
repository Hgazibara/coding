class PrimeFactorizer:
    def __init__(self, number):
        self.number = number
        self.factors = {}

    @property
    def factor(self):
        x = self.number

        for p in xrange(2, x + 1):
            if not self.is_prime(p):
                continue

            if x <= 1:
                break

            while x > 1 and x % p == 0:
                self.factors[p] = self.factors.get(p, 0) + 1
                x /= p

        return self.factors

    def is_prime(self, x):
        if x < 2:
            return False

        for p in xrange(2, int(x**0.5) + 1):
            if x % p == 0:
                return False

        return True
