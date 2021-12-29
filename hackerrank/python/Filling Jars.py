N, M = [int(x) for x in input().split()]
result = 0

while M > 0:
    a, b, k = [int(x) for x in input().split()]
    result += (b - a + 1) * k
    M -= 1
  
print(result // N)