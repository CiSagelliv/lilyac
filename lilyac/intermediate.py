from typing import List, Tuple, Dict

import lilyac
from lilyac import Token, Error, SemanticAction, Type


class Intermediate:
    ''' Aggregated intermediate representation module and semantic analysis

        In order to avoid traversing the syntax diagrams in multiple occasions
        the semantic analysis is done upon the quadruples themselves
    '''

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
            # Let the semantic action act upon the intermediate
            return symbol(self)
        elif isinstance(symbol, Token):
            # Keep the last token for future semantic actions
            self.last_token = symbol

    def generate_quadruple(self,
                           operator: str = '', op1: Token = None,
                           op2: Token = None, result: Token = None):
        ''' Quadruples' elements are stored internally as tokens
            in order to have more information for semantic analysis
        '''
        quadruple = [operator, op1, op2, result]
        # Semantic analysis
        result = self.check_quadruple(quadruple)
        self.counter += 1
        self.quadruples.append(quadruple)
        if isinstance(result, Error):
            return result

    def check_quadruple(self, quadruple: List):
        ''' Semantic analysis

            Determine if the operation described by the quadruple is valid
            according to the semantics of the language

            Note:
                See Type class and it's methods
        '''
        operator, op1, op2, result = quadruple
        type_r = Type.Error
        if operator == '=':
            # Both types must coincide
            type_1 = self.get_type(op1)
            type_2 = self.get_type(result)
            if isinstance(type_1, Error):
                return type_1
            if isinstance(type_2, Error):
                return type_2
            if type_1.value == type_2.value:
                return
        elif operator in lilyac.nullary_operators:
            operation = lilyac.nullary_operators[operator]
            type_r = operation()
        elif operator in lilyac.special_operators:
            type_1 = self.get_type(result)
            if isinstance(type_1, Error):
                return type_1
            operation = lilyac.special_operators[operator]
            type_r = operation(type_1)
        elif operator in lilyac.unary_operators:
            type_1 = self.get_type(op1)
            if isinstance(type_1, Error):
                return type_1
            operation = lilyac.unary_operators[operator]
            type_r = operation(type_1)
        elif operator in lilyac.binary_operators:
            type_1 = self.get_type(op1)
            type_2 = self.get_type(op2)
            if isinstance(type_1, Error):
                return type_1
            if isinstance(type_2, Error):
                return type_2
            operation = lilyac.binary_operators[operator]
            type_r = operation(type_1, type_2)
        if type_r.value == Type.Error.value:
            return Error(lilyac.ERRORTYPEOP, expected=operator, found=type_r)
        elif result:
            # Save the type of the result for further analysis
            self.symbols_table[result.lexeme] = type_r

    def get_type(self, op: Token):
        ''' Recover type from symbols table if available
            Otherwise, determine type by token's grammeme
        '''
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
        ''' Create a new identifier for a new temporal register
            Returns a Token of an identifier
            Saves this identifier in the symbols table

            The lexeme of this temporal variable starts with '.R'
            since no token's lexeme may start with a dot
        '''
        self.temporal_counter += 1
        lexeme = f'.R{self.temporal_counter}'
        temporal = Token(lilyac.IDENTIFIER, lexeme)
        self.symbols_table[lexeme] = None
        return temporal
