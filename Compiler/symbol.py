from Compiler import derivations


class Symbol:

    grammeme: str = ...
    terminal: bool = ...

    def __init__(self, grammeme: int):
        self.grammeme = grammeme
        self.terminal = False


class Token(Symbol):

    lexeme: str = ...

    def __init__(self, grammeme: int, lexeme: str = ''):
        super().__init__(grammeme)
        self.lexeme = lexeme
        self.terminal = True


class Error(Symbol):

    def __init__(self, grammeme: int):
        super().__init__(grammeme)


class SemanticAction(Symbol):

    def __init__(self, grammeme: int):
        super().__init__(grammeme)

