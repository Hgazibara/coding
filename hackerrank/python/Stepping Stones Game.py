import math


def calc_n(N):
    return (1 + math.sqrt(1 + 8*N))/2
    
    
def check_n(n):
    return n == int(n)


for t in range(int(input())):
    N = int(input())
    n = calc_n(N)
    if check_n(n):
        print('Go On Bob {:.0f}'.format(n-1))
    else:
        print('Better Luck Next Time')