from typing import List, Tuple, Dict
import operator

from Compiler import Token, Error, SemanticAction, Type


class Intermediate:

    symbols_table: Dict[str, Type] = ...
    quadruples: List[Tuple] = ...
    factor_pile: List = ...
    operator_pile: List = ...
    jump_pile: List = ...
    counter: int = ...
    last_token: Token = ...

    def __init__(self):
        self.symbols_table = {}
        self.quadruples = []
        self.factor_pile = []
        self.operator_pile = []
        self.jump_pile = []
        self.counter = 0

    def step(self, symbol):
        if isinstance(symbol, SemanticAction):
            symbol(self)
        elif isinstance(symbol, Token):
            self.last_token = symbol

    def generate_quadruple(self, operator='', op1='', op2='', result=''):
        quadruple = (operator, op1, op2, result)
        result = check_quadruple(quadruple)
        if isinstance(result, Error):
            pass
        else:
            self.quadruples.append(quadruple)

    def check_quadruple(self, quadruple: Tuple):
        operator, op1, op2, result = quadruple
        if operator in unary_operators:
            type_1 = symbols_table[op1]
            operation = unary_operators[operator]
            type_r = operation(type_1)
        elif operator in binary_operators:
            type_1 = symbols_table[op1]
            type_2 = symbols_table[op2]
            operation = binary_operators[operator]
            type_r = operation(type_1, type_2)
        if type_r != Type.Error:
            symbols_table[result] = type_r
            return
        else:
            return Error(Compiler.ERRORTYPEOP)


unary_operators = {
    r'!': operator.not_,
    'SF': Type.JF,
    # Add rest of operations
}

binary_operators = {
    r'+': operator.add,
    r'-': operator.sub,
    r'*': operator.mul,
    r'/': operator.truediv,
    r'%': operator.mod,
    r'||': operator.or_,
    r'&&': operator.and_,
    r'<': operator.lt,
    r'<=': operator.lte,
    r'>': operator.gt,
    r'>=': operator.gte,
    r'==': operator.eq,
    r'!=': operator.ne,
}
