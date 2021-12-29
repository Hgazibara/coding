M = int(input())
m = set(map(int, input().split()))

N = int(input())
n = set(map(int, input().split()))

print('\n'.join(map(str, sorted(m.union(n).difference(m.intersection(n))))))