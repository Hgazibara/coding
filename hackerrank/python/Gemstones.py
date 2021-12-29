N = int(input()) - 1
elements = set(input())

while N > 0:
    elements &= set(input())
    N -= 1
    
print(len(elements))