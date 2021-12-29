str1 = input().strip()
str2 = input().strip()

freqs = {}
diffs = 0

for s in str1:
    freqs[s] = freqs.get(s, 0) + 1
    
for s in str2:
    if s in freqs:
        freqs[s] -= 1
        if freqs[s] == 0:
            del freqs[s]
    else:
        diffs += 1
        
print(diffs + sum(freqs.values()))