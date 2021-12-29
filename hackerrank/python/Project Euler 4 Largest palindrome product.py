def create_palindrome(number):
    return int(str(number)+str(number)[::-1])


def find_palindrome(limit):
    
    for number in range(999, 99, -1):
        palindrome = create_palindrome(number)
        if palindrome > limit:
            continue
        for divisor in range(999, 99, -1):
            result = palindrome // divisor
            if result < 100 or result > 999 or palindrome % divisor != 0:
                continue
            else:
                return palindrome


for t in range(int(input())):
    print(find_palindrome(int(input())))