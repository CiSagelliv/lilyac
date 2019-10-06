from typing import List
import Compiler
from Compiler import Error, predictions, derivations


class Parser:

    symbols: List = ...

    def __init__(self):
        self.symbols = [
            Token(Compiler.END_OF_FILE, '$'),
            Symbol(Compiler.PROGRAM),
        ]

    def step(self, token):
        while True:
            top = symbols.pop()
            if top == token:
                return top
            elif top.terminal:
                # Add number code for syntax errors
                # Expected a token
                return Error(0)
            else:
                column = Parser.hash_token(top)
                row = top.grammeme
                production = predictions[row][column]
                if production < 600:
                    symbols += derivations[production]
                else:
                    # Add number code for syntax error
                    # Invalid derivation
                    return Error(1)

    @staticmethod
    def hash_token(token):
        if token.grammeme == Compiler.RESERVED:
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
        if token.grammeme == Compiler.IDENTIFIER:
            return 27
        if token.grammeme == Compiler.LIBRARY:
            return 28
        if token.grammeme == Compiler.COMMENTARY:
            return 29
        if token.grammeme == Compiler.INTEGER:
            return 30
        if token.grammeme == Compiler.FLOAT:
            return 31
        if token.grammeme == Compiler.FLOATSCI:
            return 32
        if token.grammeme == Compiler.CHARACTER:
            return 33
        if token.grammeme == Compiler.STRING:
            return 34
        if token.grammeme == Compiler.TIMES_SIGN:
            return 35
        if token.grammeme == Compiler.OVER_SIGN:
            return 36
        if token.grammeme == Compiler.PLUS_SIGN:
            return 37
        if token.grammeme == Compiler.MINUS_SIGN:
            return 38
        if token.grammeme == Compiler.MODULO:
            return 39
        if token.grammeme == Compiler.OR:
            return 40
        if token.grammeme == Compiler.AND:
            return 41
        if token.grammeme == Compiler.NOT:
            return 42
        if token.grammeme == Compiler.LESSTHAN:
            return 43
        if token.grammeme == Compiler.LESSEQUALS:
            return 44
        if token.grammeme == Compiler.GREATERTHAN:
            return 45
        if token.grammeme == Compiler.GREATEREQUALS:
            return 46
        if token.grammeme == Compiler.EQUALS:
            return 47
        if token.grammeme == Compiler.NEQUALS:
            return 48
        if token.grammeme == Compiler.EQUAL_SIGN:
            return 49
        if token.grammeme == Compiler.POINT:
            return 50
        if token.grammeme == Compiler.COMMA:
            return 51
        if token.grammeme == Compiler.COLON:
            return 52
        if token.grammeme == Compiler.SEMICOLON:
            return 53
        if token.grammeme == Compiler.PARENTHESISOPEN:
            return 54
        if token.grammeme == Compiler.PARENTHESISCLOSE:
            return 55
        if token.grammeme == Compiler.BRACKETSOPEN:
            return 56
        if token.grammeme == Compiler.BRACKETSCLOSE:
            return 57
        if token.grammeme == Compiler.SQUAREBOPEN:
            return 58
        if token.grammeme == Compiler.SQUAREBCLOSE:
            return 59
        if token.grammeme == Compiler.END_OF_FILE:
            return 60
        else:
            return 699
