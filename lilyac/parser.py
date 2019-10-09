from typing import List
import lilyac
from lilyac import Token, Symbol, Error, SemanticAction


class Parser:

    symbols: List = ...

    def __init__(self):
        self.symbols = [
            Token(lilyac.END_OF_FILE, '$'),
            Symbol(lilyac.PROGRAM),
        ]

    def step(self, token):
        while True:
            top = self.symbols.pop()
            if isinstance(top, SemanticAction):
                return top
            elif top == token:
                return top
            elif top.terminal:
                # Non-coinciding terminal symbols
                return Error(lilyac.ERROREXPECT,
                             expected=str(top), found=str(token))
            else:
                column = Parser.hash_token(token)
                row = top.grammeme
                production = lilyac.predictions[row][column]
                if production < 600:
                    derivation = lilyac.derivations.get(production, [])
                    # Add all symbols from the derivation in opposite order
                    self.symbols += derivation[::-1]
                else:
                    # Invalid derivation
                    return Error(lilyac.ERRORDERIVE, expected=top, found=token)

    def is_semantic_action(self) -> bool:
        top = self.symbols[-1]
        return isinstance(top, SemanticAction)

    @staticmethod
    def hash_token(token):
        ''' Hash tokens from the input language to
            the corresponding column index of the prediction matrix
        '''
        if token.grammeme == lilyac.RESERVED:
            if (token.lexeme == 'class'):
                return 0
            elif token.lexeme == 'begin':
                return 1
            elif token.lexeme == 'end':
                return 2
            elif token.lexeme == 'def':
                return 3
            elif token.lexeme == 'as':
                return 4
            elif token.lexeme == 'integer':
                return 5
            elif token.lexeme == 'float':
                return 6
            elif token.lexeme == 'char':
                return 7
            elif token.lexeme == 'string':
                return 8
            elif token.lexeme == 'boolean':
                return 9
            elif token.lexeme == 'if':
                return 10
            elif token.lexeme == 'else':
                return 11
            elif token.lexeme == 'elseif':
                return 12
            elif token.lexeme == 'endif':
                return 13
            elif token.lexeme == 'for':
                return 14
            elif token.lexeme == 'do':
                return 15
            elif token.lexeme == 'endfor':
                return 16
            elif token.lexeme == 'while':
                return 17
            elif token.lexeme == 'endwhile':
                return 18
            elif token.lexeme == 'function':
                return 19
            elif token.lexeme == 'endfunction':
                return 20
            elif token.lexeme == 'import':
                return 21
            elif token.lexeme == 'null':
                return 22
            elif token.lexeme == 'read':
                return 23
            elif token.lexeme == 'write':
                return 24
            elif token.lexeme == 'enter':
                return 25
            elif token.lexeme == 'principal':
                return 26
            else:
                return 699
        if token.grammeme == lilyac.IDENTIFIER:
            return 27
        if token.grammeme == lilyac.LIBRARY:
            return 28
        if token.grammeme == lilyac.COMMENTARY:
            return 29
        if token.grammeme == lilyac.INTEGER:
            return 30
        if token.grammeme == lilyac.FLOAT:
            return 31
        if token.grammeme == lilyac.FLOATSCI:
            return 32
        if token.grammeme == lilyac.CHARACTER:
            return 33
        if token.grammeme == lilyac.STRING:
            return 34
        if token.grammeme == lilyac.TIMES_SIGN:
            return 35
        if token.grammeme == lilyac.OVER_SIGN:
            return 36
        if token.grammeme == lilyac.PLUS_SIGN:
            return 37
        if token.grammeme == lilyac.MINUS_SIGN:
            return 38
        if token.grammeme == lilyac.MODULO:
            return 39
        if token.grammeme == lilyac.OR:
            return 40
        if token.grammeme == lilyac.AND:
            return 41
        if token.grammeme == lilyac.NOT:
            return 42
        if token.grammeme == lilyac.LESSTHAN:
            return 43
        if token.grammeme == lilyac.LESSEQUALS:
            return 44
        if token.grammeme == lilyac.GREATERTHAN:
            return 45
        if token.grammeme == lilyac.GREATEREQUALS:
            return 46
        if token.grammeme == lilyac.EQUALS:
            return 47
        if token.grammeme == lilyac.NEQUALS:
            return 48
        if token.grammeme == lilyac.EQUAL_SIGN:
            return 49
        if token.grammeme == lilyac.POINT:
            return 50
        if token.grammeme == lilyac.COMMA:
            return 51
        if token.grammeme == lilyac.COLON:
            return 52
        if token.grammeme == lilyac.SEMICOLON:
            return 53
        if token.grammeme == lilyac.PARENTHESISOPEN:
            return 54
        if token.grammeme == lilyac.PARENTHESISCLOSE:
            return 55
        if token.grammeme == lilyac.BRACKETSOPEN:
            return 56
        if token.grammeme == lilyac.BRACKETSCLOSE:
            return 57
        if token.grammeme == lilyac.SQUAREBOPEN:
            return 58
        if token.grammeme == lilyac.SQUAREBCLOSE:
            return 59
        if token.grammeme == lilyac.END_OF_FILE:
            return 60
        else:
            return 699
