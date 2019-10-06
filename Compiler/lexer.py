from typing import List
import Compiler
from Compiler import Token, Error, transitions, reserved_words, END_OF_FILE


class Lexer:

    state: int = ...
    lexeme: str = ...

    def restart(self):
        self.state = 0
        self.lexeme = ''

    def step(self, symbol: str):
        column = Lexer.hash_symbol(symbol)
        self.state = transitions[self.state][column]

    def generate_token(self, index: int, text: str):
        self.restart()
        while True:
            self.step(text[index])
            if self.is_delimiter():
                break
            if self.state != 0:
                self.lexeme += text[index]
            index += 1
        if index == len(text):
            return Token(END_OF_FILE)
        if self.is_final():
            self.lexeme += text[index]
        else:
            index -= 1
        if self.is_valid() and self.state == Compiler.RESERVED:
            if self.lexeme in reserved_words:
                self.state = Compiler.RESERVED
            else:
                self.state = Compiler.IDENTIFIER
        token = Token(self.state, self.lexeme)
        return token, index

    def is_delimiter(self):
        return self.state >= 100

    def is_final(self):
        return (self.state == Compiler.LIBRARY
                or self.state == Compiler.COMMENTARY
                or self.state == Compiler.CHARACTER
                or self.state == Compiler.STRING
                or self.state == Compiler.COMMA
                or self.state == Compiler.SEMICOLON
                or self.state == Compiler.PARENTHESISOPEN
                or self.state == Compiler.PARENTHESISCLOSE
                or self.state == Compiler.BRACKETSOPEN
                or self.state == Compiler.BRACKETSCLOSE
                or self.state == Compiler.SQUAREBOPEN
                or self.state == Compiler.SQUAREBCLOSE
                or self.state == Compiler.ERRORUNKNOWNL)

    def is_valid(self):
        return self.state < 500

    @staticmethod
    def hash_symbol(symbol: str):
        if symbol == 'E':
            return 0
        elif symbol == 'e':
            return 1
        elif symbol == 'l':
            return 2
        elif symbol == 'y':
            return 3
        elif symbol.islower():
            return 4
        elif symbol.isupper():
            return 5
        elif symbol.isdigit():
            return 6
        elif symbol == '_':
            return 7
        elif symbol == '*':
            return 8
        elif symbol == '/':
            return 9
        elif symbol == '+':
            return 10
        elif symbol == '-':
            return 11
        elif symbol == '%':
            return 12
        elif symbol == '.':
            return 13
        elif symbol == '\'':
            return 14
        elif symbol == '\"':
            return 15
        elif symbol == ' ' or symbol == '\n' or symbol == '\t':
            return 16
        elif symbol == '|':
            return 17
        elif symbol == '&':
            return 18
        elif symbol == '!':
            return 19
        elif symbol == '<':
            return 20
        elif symbol == '>':
            return 21
        elif symbol == '=':
            return 22
        elif symbol == ':':
            return 23
        elif symbol == ',':
            return 24
        elif symbol == '':
            return 25
        elif symbol == '(':
            return 26
        elif symbol == ')':
            return 27
        elif symbol == '{':
            return 28
        elif symbol == '}':
            return 29
        elif symbol == '[':
            return 30
        elif symbol == ']':
            return 31
        else:
            return 32
