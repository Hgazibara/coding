import sys

line = sys.stdin.readline().replace('\n', '')

freqs = {}
odd = 0

for char in line:
    freqs[char] = freqs.get(char, 0) + 1
    
for freq in freqs.values():
    if freq % 2 == 1:
        odd += 1
        
print('NO' if odd > 1 else 'YES')