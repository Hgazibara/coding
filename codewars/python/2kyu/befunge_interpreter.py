import operator
import random

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '%': operator.mod
}

def interpret(code):
    stack = []
    pointer = Pointer()

    ascii_mode = False
    output = []

    grid = init_grid(code)
    lines = 0

    while True:
        command = grid[pointer.x][pointer.y]
        lines += 1

        if command == None:
            pointer.make_move()
            continue

        if ascii_mode:
            if command == '"':
                ascii_mode = False
            else:
                stack.append(ord(command))

        else:
            if command == '"':
                ascii_mode = True

            elif command.isdigit():
                stack.append(int(command))

            elif command in '+-*/%':
                a, b = stack.pop(), stack.pop()
                try:
                    stack.append(operations[command](b, a))
                except ZeroDivisionError as e:
                    stack.append(a)

            elif command == '!':
                stack.append(int(not stack.pop()))

            elif command == '`':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b > a))

            elif command in '<>^v':
                pointer.direction = command

            elif command == '?':
                pointer.direction = '<>^v'[random.randint(0, 3)]

            elif command == '_':
                a = stack.pop()
                pointer.direction = '>' if a == 0 else '<'

            elif command == '|':
                a = stack.pop()
                pointer.direction = 'v' if a == 0 else '^'

            elif command == ':':
                x = 0 if not stack else stack[-1]
                stack.append(x)

            elif command == '\\':
                a = stack.pop()
                b = stack.pop() if stack else 0
                stack.extend([b, a])

            elif command == '$':
                stack.pop()

            elif command == '.':
                output.append(str(stack.pop()))

            elif command == ',':
                output.append(chr(stack.pop()))

            elif command == '#':
                pointer.make_move()

            elif command == 'p':
                y, x, v = stack.pop(), stack.pop(), stack.pop()
                code[x][y] = chr(v)

            elif command == 'g':
                y, x = stack.pop(), stack.pop()
                stack.append(ord(code[x][y]))

            elif command == '@':
                print lines
                return ''.join(output)

        pointer.make_move()


def init_grid(code):
    code = [line for line in code.split('\n')]
    grid = [[None] * 80 for _ in xrange(25)]

    for i, row in enumerate(code):
        for j, cell in enumerate(row):
            grid[i][j] = cell

    return grid


class Pointer(object):

    directions = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    MAX_X = 25
    MAX_Y = 80

    def __init__(self):
        self.direction = '>'
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def make_move(self):
        x, y = self.directions[self.direction]
        self.__x = (self.__x + x) % self.MAX_X if (self.__x + x) >= 0 else self.MAX_X + x
        self.__y = (self.__y + y) % self.MAX_Y if (self.__y + y) >= 0 else self.MAX_Y + y
