T = int(input())

for t in range(T):
    N = int(input())
    f1, f2 = 1, 2
    result = 0
            
    while f2 <= N:
        if f2%2 == 0:
            result += f2
        f1, f2 = f2, f1 + f2
        
    print(result)