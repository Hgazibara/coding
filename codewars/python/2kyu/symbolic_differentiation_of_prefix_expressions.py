import abc


class Operand(object):
    pass


class Operator(object):
    pass


class Expression(abc.ABC):
    
    @abc.abstractclassmethod
    def from_string(cls, expression):
        pass
    
    def derive(self):
        pass
        
    def simplify(self):
        pass


class UnaryExpression(Expression):
    
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def derive(self):
        pass
        
    def simplify(self):
        pass


class BinaryExpression(Expression):
    
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
    
    def derive(self):
        pass
        
    def simplify(self):
        pass


def diff(s):
    pass
