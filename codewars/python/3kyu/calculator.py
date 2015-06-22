import re

class Calculator(object):

    def evaluate(self, expression):
        p = re.compile(r'-|\+')

        tokens = p.split(expression)
        operations = p.findall(expression)

        subresults = [self.evaluate_sub(token) for token in tokens]
        result = subresults[0]

        for a, op in zip(subresults[1:], operations):
            result += (1 if op == '+' else -1) * a

        return round(result, 4)

    def evaluate_sub(self, token):
        p = re.compile(r'/|\*')

        tokens = [float(t) for t in p.split(token)]
        operations = p.findall(token)
        result = tokens[0]

        for a, op in zip(tokens[1:], operations):
            result = result / a if op == '/' else result * a

        return result
