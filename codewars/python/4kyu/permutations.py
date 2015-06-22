import itertools

def permutations(string):
    return set(''.join(p) for p in itertools.permutations(string))
