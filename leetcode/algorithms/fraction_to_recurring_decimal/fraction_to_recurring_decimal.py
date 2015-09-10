class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0 or denominator == 0:
            return "0"

        indexes = {}
        numbers = []

        if (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0):
            sign = 1
        else:
            sign = -1

        numerator = abs(numerator)
        denominator = abs(denominator)

        start_repetition = -1
        i = 0

        while numerator:
            quotient = numerator / denominator
            numbers.append(quotient)

            remainder = numerator % denominator

            if remainder == 0:
                break

            if remainder in indexes:
                start_repetition = indexes[remainder]
                break

            indexes[remainder] = i
            numerator = remainder * 10
            i += 1

        if len(numbers) == 1:
            intermediate = str(numbers[0])

        elif start_repetition == -1:
            intermediate = '{0}.{1}'.format(numbers[0], ''.join(map(str, numbers[1:])))

        else:
            before = ''.join(map(str, numbers[1:start_repetition]))
            after = ''.join(map(str, numbers[start_repetition:]))
            intermediate = '{0}.{1}({2})'.format(numbers[0], before, after)

        return '{0}{1}'.format('' if sign > 0 else '-', intermediate)
