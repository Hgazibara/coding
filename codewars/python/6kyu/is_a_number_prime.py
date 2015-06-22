def is_prime(num):
    if num < 2:
        return False

    for x in range(2, num + 1):
        if x*x > num:
            return True
        if num % x == 0:
            return False
            
    return True
