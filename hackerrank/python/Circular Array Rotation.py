N, K, Q = map(int, input().strip().split())
arr = [int(x) for x in input().strip().split()]
positions = []

for pos in range(N):
    positions.append((pos + K) % N)
    
while Q > 0:
    q = int(input())
    print(arr[positions.index(q)])
    Q -= 1