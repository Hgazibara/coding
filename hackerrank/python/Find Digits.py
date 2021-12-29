import sys

T = int(sys.stdin.readline())

while T > 0:
    
    counter = 0
    N = sys.stdin.readline().replace('\n', '')
    digits, N = list(N), int(N)
    
    for digit in digits:
        digit = int(digit)
        if digit != 0 and N % int(digit) == 0:
            counter += 1
            
    print(counter)
    T -= 1