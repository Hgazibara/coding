for t in range(int(input())):
    n = ~int(input())
    if n < 0:
        n += 2**32
    print(n)