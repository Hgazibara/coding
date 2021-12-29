one_digit = {
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',
    '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
    '8': 'Eight', '9': 'Nine'
}

two_digit = {
    '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen',
    '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen',
    '18': 'Eighteen', '19': 'Nineteen', '20': 'Twenty', '30': 'Thirty',
    '40': 'Forty', '50': 'Fifty', '60': 'Sixty', '70': 'Seventy',
    '80': 'Eighty', '90': 'Ninety'
}

units = ['Thousand', 'Million', 'Billion', 'Trillion']

def resolve_one_digit(number):
    return one_digit[number]


def resolve_two_digit(number):
    if 11 <= int(number) <= 19:
        return two_digit[number]
    elif number == '00':
        return ''
    elif number.startswith('0'):
        return resolve_one_digit(number[1:])
    else:
        first_part = two_digit['{0}0'.format(number[0])]
        second_part = resolve_one_digit(number[1])

        if second_part == 'Zero':
            return first_part
        else:
            return '{} {}'.format(first_part, second_part)
    

def translate(number):
    
    if len(number) == 1:
        return resolve_one_digit(number)
    elif len(number) == 2:
        return resolve_two_digit(number)
    elif len(number) == 3:
        first_part, second_part = translate(number[0]), translate(number[1:])
        if first_part != 'Zero':
            return '{} Hundred {}'.format(first_part, second_part)
        elif second_part:
            return second_part
        else:
            return ''
    else:
        num_length = len(number)
        unit = (num_length-1) // 3
        part = (num_length-1) % 3 + 1
        first_part, second_part = translate(number[:part]).strip(), translate(number[part:]).strip()
        if first_part and first_part != 'Zero':
            return '{} {} {}'.format(first_part, units[unit-1], second_part)
        elif second_part:
            return second_part
        else:
            return ''
    
    
for t in range(int(input())):
    print(translate(input()).strip())