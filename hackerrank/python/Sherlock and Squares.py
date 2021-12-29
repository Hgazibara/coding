import math

T = int(input())

while T > 0:
    A, B = [int(x) for x in input().split()]
    counter = 0
    number = 1
    diff = 3
    while number <= B:
        if number >= A:
            counter += 1
        number += diff
        diff += 2
    print(counter)
    T -= 1