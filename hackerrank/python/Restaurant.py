from fractions import gcd

for t in range(int(input())):
    l, b = [int(x) for x in input().split()]
    g = gcd(l, b)
    print((l//g)*(b//g))