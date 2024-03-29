import lilyac
from lilyac import Token, Error


class Lexer:

    state: int = ...
    lexeme: str = ...

    def restart(self):
        self.state = 0
        self.lexeme = ''

    def step(self, symbol: str):
        column = Lexer.hash_symbol(symbol)
        self.state = lilyac.transitions[self.state][column]

    def generate_token(self, index: int, text: str):
        self.restart()
        while index < len(text):
            self.step(text[index])
            if self.is_delimiter():
                break
            if self.state != 0:
                self.lexeme += text[index]
            index += 1
        if index == len(text):
            return Token(lilyac.END_OF_FILE), index
        if self.is_final():
            self.lexeme += text[index]
        else:
            index -= 1
        if self.is_valid() and self.state == lilyac.RESERVED:
            if self.lexeme in lilyac.reserved_words:
                self.state = lilyac.RESERVED
            else:
                self.state = lilyac.IDENTIFIER
        token = Token(self.state, self.lexeme)
        return token, index + 1

    def is_delimiter(self):
        return self.state >= 100

    def is_final(self):
        ''' Check if the finishing state corresponds to a Token
            whose last character determines its end
        '''
        return (self.state == lilyac.LIBRARY
                or self.state == lilyac.COMMENTARY
                or self.state == lilyac.CHARACTER
                or self.state == lilyac.STRING
                or self.state == lilyac.COMMA
                or self.state == lilyac.SEMICOLON
                or self.state == lilyac.PARENTHESISOPEN
                or self.state == lilyac.PARENTHESISCLOSE
                or self.state == lilyac.BRACKETSOPEN
                or self.state == lilyac.BRACKETSCLOSE
                or self.state == lilyac.SQUAREBOPEN
                or self.state == lilyac.SQUAREBCLOSE
                or self.state == lilyac.ERRORUNKNOWNL)

    def is_valid(self):
        return self.state < 500

    @staticmethod
    def hash_symbol(symbol: str):
        ''' Hash symbols from the input alphabet to
            the corresponding column index of the transition matrix
        '''
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
        elif symbol.isspace():
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
        elif symbol == ';':
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
