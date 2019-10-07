from typing import List, Tuple, Dict

import lilyac
from lilyac import Token, Error, SemanticAction, Type


class Intermediate:

    symbols_table: Dict[str, Type] = ...
    quadruples: List[List] = ...
    factor_pile: List = ...
    operator_pile: List = ...
    jump_pile: List = ...
    counter: int = ...
    last_token: Token = ...
    temporal_counter: int = ...

    def __init__(self):
        self.symbols_table = {}
        self.quadruples = []
        self.factor_pile = []
        self.operator_pile = []
        self.jump_pile = []
        self.counter = 0
        self.temporal_counter = 0

    def step(self, symbol):
        if isinstance(symbol, SemanticAction):
            return symbol(self)
        elif isinstance(symbol, Token):
            self.last_token = symbol

    def generate_quadruple(self,
                           operator: str = '', op1: Token = None,
                           op2: Token = None, result: str = ''):
        quadruple = [operator, op1, op2, result]
        result = self.check_quadruple(quadruple)
        self.counter += 1
        self.quadruples.append(quadruple)
        if isinstance(result, Error):
            return result

    def check_quadruple(self, quadruple: List):
        operator, op1, op2, result = quadruple
        type_r = Type.Error
        if operator in nonary_operators:
            operation = nonary_operators[operator]
            type_r = operation()
        elif operator in unary_operators:
            type_1 = self.get_type(op1)
            operation = unary_operators[operator]
            type_r = operation(type_1)
        elif operator in binary_operators:
            type_1 = self.get_type(op1)
            type_2 = self.get_type(op2)
            operation = binary_operators[operator]
            type_r = operation(type_1, type_2)
        if type_r != Type.Error:
            self.symbols_table[result] = type_r
            return
        else:
            return Error(lilyac.ERRORTYPEOP)

    def get_type(self, op: Token):
        if op.grammeme == lilyac.IDENTIFIER:
            if op.lexeme in self.symbols_table:
                return self.symbols_table[op.lexeme]
            else:
                return Error(lilyac.ERRORUNDECL, expected=op)
        elif op.grammeme == lilyac.INTEGER:
            return Type.integer
        elif op.grammeme == lilyac.FLOAT:
            return Type.float
        elif op.grammeme == lilyac.FLOATSCI:
            return Type.float
        elif op.grammeme == lilyac.CHARACTER:
            return Type.character
        elif op.grammeme == lilyac.STRING:
            return Type.string
        else:
            return Type.Error

    def new_temporal(self):
        self.temporal_counter += 1
        temporal = f'R{self.temporal_counter}'
        self.symbols_table[temporal] = ''
        return temporal


nonary_operators = {
    'JI': Type.JI,
}


unary_operators = {
    r'!': lambda x: not x,
    'JF': Type.JF,
    'JT': Type.JT
    # Add rest of operations
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
