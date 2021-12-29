for t in range(int(input())):
    input_str = input().strip()
    input_str_len = len(input_str)
    num_of_ops = 0
    
    for pos in range(input_str_len//2):
        num_of_ops += abs(ord(input_str[pos]) - ord(input_str[input_str_len - pos - 1]))
        
    print(num_of_ops)
        