import operator as op

x = float(input())
y = float(input())

ops = [op.add, op.sub, op.mul, op.truediv, op.floordiv]

for o in ops:
    print('{0:.2f}'.format(o(x, y)))