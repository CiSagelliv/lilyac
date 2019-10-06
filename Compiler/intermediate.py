from typing import List, Tuple, Dict
from Compiler import Token, SemanticAction


class Intermediate:

    symbols_table: Dict[str, str] = ...
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

    def step(self, symbol):
        if isinstance(symbol, SemanticAction):
            symbol(self)
        elif isinstance(symbol, Token):
            self.last_token = symbol

    def generate_quadruple(self, operator='', op1='', op2='', result=''):
        quadruple = (self.counter, operator, op1, op2, result)
        self.quadruples.append(quadruple)
