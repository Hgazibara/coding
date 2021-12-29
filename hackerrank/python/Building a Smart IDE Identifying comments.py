import sys
import string

pos = 0
code = ''.join(sys.stdin.readlines())
chars_num = len(code)

def handle_comment(pos, code, target, endc):
    comment = [code[pos]]
    pos += 1
    
    while code[pos] != target:
        comment.append(code[pos])
        pos += 1
    
    comment.append(code[pos])
    print(''.join(comment), end=endc)
    
    return pos

def handle_single(pos, code):
    return handle_comment(pos, code, '\n', '')

def handle_multi(pos, code):
    return handle_comment(pos, code, '/', '\n')

while pos < chars_num:
    if code[pos] == '/':
        if code[pos + 1] == '/':
            pos = handle_single(pos, code)
        elif code[pos + 1] == '*':
            pos = handle_multi(pos, code)
        pos += 1
    else:
        pos += 1