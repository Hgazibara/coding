def divisors(integer):
    divs = set()
    for x in range(2, integer + 1):
        if x*x >= integer:
            return sorted(divs) if divs else '{0} is prime'.format(integer)
        if integer % x == 0:
            divs.update([x, integer/x])
    return sorted(divs)
