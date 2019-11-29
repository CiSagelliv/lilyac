import lilyac
from lilyac import Token

from typing import List


class Execution:

    self.quadruples: List = ...
    self.symbols_table: Dict = ...
    self.values: Dict = ...
    self.instruction: int = ...

    def __init__(self, quadruples, symbols_table):
        self.quadruples = quadruples
        self.symbols_table = symbols_table
        self.values = {}

        for symbol, symbol_type in self.symbols_table:
            self.values[symbol] = None

    def execute(self):
        ''' Evaluate every quadruple
        '''
        self.instruction = 0
        while self.instruction < len(self.quadruples):
            self.evaluate(self.quadruples[self.instruction])
        print('Finished Succesfully')

    def evaluate_quadruple(self, q):
        ''' Evaluate the result of a quadruple with a simple operation
            returning a token
        '''
        op = q[0]

        if op in nullary_operators:
            operator = unary_operators[op]
            operator()
        elif op in special_unary_operators:
            operator = unary_operators[op]
            op1 = get_value(q[3])
            result = operator(op1)
            if op1 = 'JI' and type(result) == int:
                self.instruction = result
        elif op in special_binary_operators:
            operator = binary_operators[op]
            op1 = get_value(q[1])
            op2 = get_value(q[3])
            result = operator(op1, op2)
            if type(result) == int:
                self.instruction = result
        elif op in unary_operators:
            operator = unary_operators[op]
            op1 = get_value(q[1])
            result = operator(op1)
            variable = q[3].lexeme
            self.values[variable] = result
        elif op in binary_operators:
            operator = binary_operators[op]
            op1 = get_value(q[1])
            op2 = get_value(q[2])
            result = operator(op1, op2)
            variable = q[3].lexeme
            self.values[variable] = result
        else:
            raise Exception('Error in operation: ', q)

    def get_value(self, token):
        if is_constant(token):
            if token.grammeme == lilyac.INTEGER:
                return int(token.lexeme)
            elif (token.grammeme == lilyac.FLOAT
                  or token.grammeme == lilyac.FLOATSCI):
                return float(token.lexeme)
            elif token.grammeme == lilyac.CHARACTER:
                return token.lexeme
            elif token.grammeme == lilyac.STRING:
                return token.lexeme
        else:
            return self.values[token.lexeme]


jumps = [
    'JF',
    'JT',
    'JI',
]


''' Operators whose parameter is
    stored as result in the quadruple
'''
special_unary_operators = {
    'write': print,
    'read': input,
    'JI': jump_inconditional,
}


special_binary_operators = {
    'JF': jump_false,
    'JT': jump_true,
}


nullary_operators = {
    'enter': enter,
}


unary_operators = {
    r'!': lambda x: not x,
}


binary_operators = {
    r'+': lambda x, y: x + y,
    r'-': lambda x, y: x - y,
    r'*': lambda x, y: x * y,
    r'/': lambda x, y: x / y,
    r'%': lambda x, y: x % y,
    r'||': lambda x, y: x or y,
    r'&&': lambda x, y: x and y,
    r'<': lambda x, y: x < y,
    r'<=': lambda x, y: x <= y,
    r'>': lambda x, y: x > y,
    r'>=': lambda x, y: x >= y,
    r'==': lambda x, y: x == y,
    r'!=': lambda x, y: x != y,
}


def jump_inconditional(instruction: int):
    return instruction


def jump_false(value: bool, instruction: int):
    return instruction if not value else None


def jump_true(value: bool):
    return instruction if value else None


def enter():
    print()
