for t in range(int(input())):
    s = input().strip()
    n = len(s)
    
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[-i-1]) - ord(s[-i])):
            print('Not Funny')
            break
    else:
        print('Funny')