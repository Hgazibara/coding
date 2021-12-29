T = int(input())

while T > 0:
    N = int(input())
    size, cycle = 1, 1
    while cycle <= N:
        if cycle % 2 == 1:
            size *= 2
        else:
            size += 1
        cycle += 1
    print(size)
    T -= 1