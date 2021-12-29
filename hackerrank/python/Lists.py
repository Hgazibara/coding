if __name__ == '__main__':
    commands = {
        'insert': lambda i, e: l.insert(i, e),
        'print': lambda: print(l),
        'remove': lambda e: l.remove(e),
        'append': lambda e: l.append(e),
        'sort': lambda: l.sort(),
        'pop': lambda: l.pop(),
        'reverse': lambda: l.reverse()
    }
    
    l = []
    N = int(input())
    
    for n in range(N):
        line = input()
        parts = line.split(maxsplit=1)
    
        command = commands[parts[0]]
        
        if len(parts) > 1:
            command(*[int(x) for x in parts[1].split()])
        else:
            command()
