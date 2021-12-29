def fib(n):
    
    numbers = [0, 1, 1]
    
    if n < 4:
        return numbers[0:n]
    
    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-2])
        
    return numbers

print(list(map(lambda x: x**3, fib(int(input())))))