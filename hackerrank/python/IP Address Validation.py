import sys
import re

N = int(sys.stdin.readline())

for input in sys.stdin:
    first_try = input.split('.')
    flag = True
    
    if len(first_try) == 4:
        for num in first_try:
            try:
                if int(num) > 255:
                    flag = False
                    break
            except:
                flag = False
                break
    else:
        flag = False
                
    if flag:
        print('IPv4')
        continue
        
    second_try = input.split(':')
    flag = True
    
    if len(second_try) == 8:
        for num in second_try:
            try:
                if int(num, 16) > 65535:
                    flag = False
                    break
            except:
                flag = False
                break
    else:
        flag = False
                
    if flag:
        print('IPv6')
        continue
        
    print('Neither')