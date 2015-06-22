mapping = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
    10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
    1000: 'M'
}


def solution(n):
    if n == 0: return ''
    m, s = find_closest_smaller(n)
    return s + solution(n - m)


def find_closest_smaller(n):
    _, k = min([(n - x, x) for x in mapping.iterkeys() if n >= x])
    return k, mapping[k]
