N = int(input())

def remove_repeated_chars(string):
    
    used = set()
    letters = []
    
    for char in string:
        if char not in used:
            letters.append(char)
            used.add(char)
            
    return ''.join(letters)

def generate_columns(key):
    
    columns = [[s] for s in key]
    columns_num = len(key)
    used = set(list(key))
    
    pos = 0
    
    for c in [chr(i) for i in range(65, 91)]:
        if c not in used:
            used.add(c)
            columns[pos].append(c)
            pos = (pos + 1) % columns_num
            
    return columns

def sort_columns(columns):
    return sorted(columns, key=lambda t: t[0])
    
def generate_alphabet(key):
    
    key = remove_repeated_chars(key)
    columns = sort_columns(generate_columns(key))
    alphabet = {}
    c = 65
    
    for column in columns:
        for char in column:
            alphabet[char] = chr(c)
            c += 1
    
    return alphabet
    
def decrypt(alphabet, ciphertext):
    
    letters = []
    
    for char in ciphertext:
        if char in alphabet:
            letters.append(alphabet[char])
        else:
            letters.append(char)
            
    return ''.join(letters)
    
while N > 0:
    key = input().rstrip()
    ciphertext = input().rstrip()
    print(decrypt(generate_alphabet(key), ciphertext))
    N -= 1