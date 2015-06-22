def brain_luck(code, text):
    interpreter = Interpreter(code, text)
    return interpreter.interpret()


class Interpreter(object):

    def __init__(self, code, text):
        self.tokenizer = Tokenizer(code)
        self.text = iter(text)

        self.memory = Memory()
        self.output = []

        self.__commands = {
            '>': lambda t: self.memory.inc_pointer(),
            '<': lambda t: self.memory.dec_pointer(),
            '+': lambda t: self.memory.inc_value(),
            '-': lambda t: self.memory.dec_value(),
            ',': lambda t: self.read_input(),
            '.': lambda t: self.store_output(),
            '[': self.in_branch,
            ']': self.out_branch
        }

    def read_input(self):
        self.memory.input(next(self.text))

    def store_output(self):
        self.output.append(self.memory.output())

    def in_branch(self, token):
        if self.memory.is_empty():
            self.tokenizer.set_pointer(token.next)

    def out_branch(self, token):
        if not self.memory.is_empty():
            self.tokenizer.set_pointer(token.next)

    def interpret(self):
        for token in self.tokenizer:
            self.run_command(token)

        return ''.join(self.output)

    def run_command(self, token):
        self.__commands[token.name](token)


class Tokenizer(object):

    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.pointer = 0

        self._tokenize()

    def _tokenize(self):
        prev_positions = []

        # Create tokens, but also build static connections between [ & ]
        for index, token in enumerate(self.code):
            if token == '[':
                prev_positions.append(index)

            if token == ']':
                position = prev_positions.pop()
                self.tokens.append(Token(token, position))
                self.tokens[position].next = index
            else:
                self.tokens.append(Token(token, index + 1))

    def set_pointer(self, index):
        self.pointer = index

    def __iter__(self):
        tokens_number = len(self.tokens)

        while self.pointer < tokens_number:
            yield self.tokens[self.pointer]
            self.pointer += 1


class Token(object):

    def __init__(self, name, next_token):
        self.name = name
        self.next = next_token


class Memory(object):

    def __init__(self):
        self.pointer = 0
        self.cells = [0]

    def inc_pointer(self):
        self.pointer += 1
        if len(self.cells) == self.pointer:
            self.cells.append(0)

    def dec_pointer(self):
        self.pointer -= 1

    def inc_value(self):
        value = self.cells[self.pointer]
        self.cells[self.pointer] = (value + 1) % 256

    def dec_value(self):
        value = self.cells[self.pointer]
        self.cells[self.pointer] = 255 if value == 0 else value - 1

    def output(self):
        return chr(self.cells[self.pointer])

    def input(self, c):
        self.cells[self.pointer] = ord(c)

    def is_empty(self):
        return self.cells[self.pointer] == 0
