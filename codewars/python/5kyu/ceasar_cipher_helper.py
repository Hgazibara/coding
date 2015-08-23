class CaesarCipher(object):
    START = 65
    END = 90

    def __init__(self, shift):
        self.shift = shift
        self._init_tables()

    def _init_tables(self):
        characters = self.END - self.START + 1

        self.in_table = {}
        self.out_table = {}

        for x in xrange(characters):
            a = chr(self.START + x)
            b = chr(self.START + (x + self.shift) % characters)

            self.in_table[a] = b
            self.out_table[b] = a

    def encode(self, message):
        return ''.join(self.in_table.get(char, char) for char in message.upper())

    def decode(self, message):
        return ''.join(self.out_table.get(char, char) for char in message.upper())
