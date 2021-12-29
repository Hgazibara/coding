string = input().strip()
substring = input().strip()
substring_len = len(substring)

bottom = len(string) - len(substring)
top = len(string)
counter = 0

while bottom >= 0:
    if substring in string[bottom:top]:
        counter += 1
        bottom -= substring_len - 1
        top -= substring_len - 1
    else:
        bottom -= 1
        top -= 1
        
print(counter)