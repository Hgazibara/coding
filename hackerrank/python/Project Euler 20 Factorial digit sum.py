import math

for t in range(int(input())):
    print(sum([int(digit) for digit in str(math.factorial(int(input())))]))