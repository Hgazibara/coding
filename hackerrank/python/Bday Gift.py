N = int(input())
e = 0

while N > 0:
    e += int(input())
    N -= 1
    
print('{:.1f}'.format(e * 0.5))