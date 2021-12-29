string = input().strip()
substring = input().strip()
win = len(substring)

bottom = len(string) - win
counter = 0

while bottom >= 0:
    if substring in string[bottom:bottom + win]:
        counter += 1
    bottom -= 1
        
print(counter)