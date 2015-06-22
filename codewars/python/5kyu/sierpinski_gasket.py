def sierpinski(n):
    if n == 0: return 'L'
    if n == 1: return 'L\nL L'
    if n == 2: return 'L\nL L\nL   L\nL L L L'

    t = sierpinski(n - 1)
    return t + '\n' + duplicate(t)


def duplicate(t):
    parts = t.split('\n')
    longest_part = max(len(part) for part in parts)

    output = []
    f = '{{0:{0}s}} {{0}}'.format(longest_part)

    for part in parts:
        output.append(f.format(part))

    return '\n'.join(output)
