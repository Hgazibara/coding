def decodeBits(bits):
    bits = bits.strip('0')
    freq = determine_frequency(bits)

    sampled_bits = bits[::freq]
    without_ones = sampled_bits.replace('111', '-').replace('1', '.')
    without_zeros = without_ones.replace('0000000', '  ').replace('000', ' ').replace('0', '')

    return without_zeros


def determine_frequency(bits):
    return 1


def decodeMorse(morseCode):
    words = morseCode.split('  ')
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split()) for word in words)
