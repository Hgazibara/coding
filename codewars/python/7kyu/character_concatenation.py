def char_concat(word):
    n = len(word)
    return ''.join([part(word, n, x) for x in xrange(n/2)])


def part(word, n, x):
    return '{0}{1}{2}'.format(word[x], word[n - x - 1], x + 1)
