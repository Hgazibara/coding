def solution(roman):
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    numbers = [values[digit] for digit in roman]

    for index, number in enumerate(numbers[1:], 1):
        sign = -1 if number > numbers[index - 1] else 1
        numbers[index - 1] *= sign

    return sum(numbers)
