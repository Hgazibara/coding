def sum_of_n(n):
    numbers = [0]
    sign = 1 if n == 0 else abs(n)/n
    
    for x in range(1, abs(n) + 1):
        numbers.append(numbers[-1] + x*sign)
    
    return numbers
