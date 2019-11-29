import lilyac
from lilyac import Token

from typing import List, Dict


class Execution:

    quadruples: List = ...
    symbols_table: Dict = ...
    values: Dict = ...
    instruction: int = ...
    output: List = ...

    def __init__(self, quadruples, symbols_table):
        self.quadruples = quadruples
        self.symbols_table = symbols_table
        self.values = {}
        self.output = []

        for symbol in self.symbols_table:
            self.values[symbol] = None

    def execute(self):
        ''' Evaluate every quadruple
        '''
        self.instruction = 0
        while self.instruction < len(self.quadruples):
            self.evaluate(self.quadruples[self.instruction])
        print('Finished Succesfully')

    def evaluate(self, q):
        ''' Evaluate the result of a quadruple with a simple operation
            returning a token
        '''
        op = q[0]
        if op in nullary_operators:
            operator = nullary_operators[op]
            operator()
            self.instruction += 1

        elif op in special_unary_operators:
            operator = special_unary_operators[op]
            op1 = self.get_value(q[3])
            result = operator(op1)
            if op == 'JI' and type(result) == int:
                self.instruction = result
            else:
                self.instruction += 1
                if op == 'write':
                    self.output.append(op1)

        elif op in special_binary_operators:
            operator = special_binary_operators[op]
            op1 = self.get_value(q[1])
            op2 = self.get_value(q[3])
            result = operator(op1, op2)
            if type(result) == int:
                self.instruction = result
            self.instruction += 1
        elif op in unary_operators:
            operator = unary_operators[op]
            op1 = self.get_value(q[1])
            result = operator(op1)
            variable = q[3].lexeme
            self.values[variable] = result
            self.instruction += 1
        elif op in binary_operators:
            operator = binary_operators[op]
            op1 = self.get_value(q[1])
            op2 = self.get_value(q[2])
            result = operator(op1, op2)
            variable = q[3].lexeme
            self.values[variable] = result
            self.instruction += 1
        elif op == '=':
            variable = q[1].lexeme
            self.values[variable] = self.get_value(q[3])
            self.instruction += 1
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


def is_constant(factor):
    return factor.grammeme in constants


def jump_inconditional(instruction: int):
    return instruction


def jump_false(value: bool, instruction: int):
    return instruction if not value else None


def jump_true(value: bool, instruction: int):
    return instruction if value else None


def enter():
    print()


jumps = [
    'JF',
    'JT',
    'JI',
]


constants = [
    lilyac.INTEGER,
    lilyac.FLOAT,
    lilyac.FLOATSCI,
    lilyac.CHARACTER,
    lilyac.STRING,
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
