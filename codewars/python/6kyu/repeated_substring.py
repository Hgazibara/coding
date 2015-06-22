def f(s):
    n = len(s)
    for x in xrange(1, n/2 + 1):
        r = n/x
        if s == s[:x]*r:
            return (s[:x], r)
    return (s, 1)
