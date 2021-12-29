import re

T = int(input())

for t in range(T):
    try:
        re.compile(input())
        print('True')
    except:
        print('False')
