L, R = int(input()), int(input())

max_xor = 0

for a in range(L, R+1):
    for b in range(L, R+1):
        max_xor = max(max_xor, a^b)
        
print(max_xor)