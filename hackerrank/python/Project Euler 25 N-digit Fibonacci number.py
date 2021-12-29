def find_terms(max_length):
    f1, f2 = 1, 1
    term = 2
    current_length = 1
    terms = {}
    
    while len(str(f2)) <= max_length:
        f1, f2 = f2, f1+f2
        
        if len(str(f2)) > current_length:
            terms[current_length+1] = term+1
            current_length += 1
            
        term += 1
        
    return terms


terms = find_terms(5000)

for t in range(int(input())):
    print(terms[int(input())])