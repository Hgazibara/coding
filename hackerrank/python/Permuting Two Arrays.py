import sys

T = int(sys.stdin.readline())

while T > 0:
    N, K = [int(x) for x in sys.stdin.readline().split()]
    arr1 = [int(x) for x in sys.stdin.readline().split()]
    arr2 = [int(x) for x in sys.stdin.readline().split()]
    
    arr1 = sorted(arr1, reverse=True)
    arr2 = sorted(arr2)
    
    possible = True
    
    for x,y in zip(arr1, arr2):
        if x + y < K:
            possible = False
            break
            
    print('YES' if possible else 'NO')
    
    T -= 1