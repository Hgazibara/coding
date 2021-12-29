names = []

for n in range(int(input())):
    names.append(input())
    
names = sorted(names)

for q in range(int(input())):
    query = input()
    print((names.index(query) + 1)*sum([ord(c)-64 for c in query]))