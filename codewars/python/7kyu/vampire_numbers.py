from collections import Counter

def vampire_test(x, y):
    cp = Counter(str(x*y))

    cp.subtract(Counter(str(x)))
    cp.subtract(Counter(str(y)))

    return all(v == 0 for v in cp.values())
