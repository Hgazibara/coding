import numpy

coeff = [float(c) for c in  input().split()]
x = float(input())

print(numpy.polyval(coeff, x))
