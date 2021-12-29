import collections

N = int(input())
X = sorted([int(x) for x in input().split()])

d = collections.Counter(X)

print('{0:.1f}'.format(sum(X) / len(X)))
print('{0:.1f}'.format(X[len(X)//2] if len(X) % 2 == 1 else (X[len(X)//2-1] + X[len(X)//2]) / 2))
print(d.most_common(1)[0][0])
