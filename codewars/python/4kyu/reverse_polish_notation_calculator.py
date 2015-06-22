import operator

def calc(expr):
    if not expr: return 0

    stack = []
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div
    }

    for part in expr.split():
        if part in operators.keys():
            a, b = stack.pop(), stack.pop()
            stack.append(operators[part](b, a))
        else:
            stack.append(float(part))

    return stack.pop()
