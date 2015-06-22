def decodeMorse(morse_code):
    words = morse_code.split('   ')
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split()) for word in words)
