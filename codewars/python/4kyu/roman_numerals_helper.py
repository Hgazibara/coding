class RomanNumerals(object):

    mapping_to = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    mapping_from = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    @classmethod
    def to_roman(cls, number):
        if number == 0: return ''
        m, s = cls.find_closest_smaller(number)
        return s + cls.to_roman(number - m)

    @classmethod
    def find_closest_smaller(cls, n):
        _, k = min([(n - x, x) for x in cls.mapping_to.iterkeys() if n >= x])
        return k, cls.mapping_to[k]

    @classmethod
    def from_roman(cls, roman_number):
        numbers = [cls.mapping_from[digit] for digit in roman_number]

        for index, number in enumerate(numbers[1:], 1):
            sign = -1 if number > numbers[index - 1] else 1
            numbers[index - 1] *= sign

        return sum(numbers)
