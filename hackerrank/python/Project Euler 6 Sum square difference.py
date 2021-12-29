T = int(input())

while T > 0:
    N = int(input())
    print(int((N*(N+1)/2)**2 - N*(N+1)*(2*N+1)/6))
    T -= 1