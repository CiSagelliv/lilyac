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

    def __repr__(self):
        if self.grammeme == 501:
            return "Malformed identifier"
        elif self.grammeme == 502:
            return "Unknown library"
        elif self.grammeme == 503:
            return "It is not a float number"
        elif self.grammeme == 504:
            return "It is not a scientific notation"
        elif self.grammeme == 505:
            return "It is not a character"
        elif self.grammeme == 506:
            return "It is not an OR"
        elif self.grammeme == 507:
            return "It is not and AND"
        elif self.grammeme == 599:
            return "Unknown error"
        elif self.grammeme == 601:
            return "Program’s head: The program must start with either library declaration or class definition"
        elif self.grammeme == 602:
            return "Program’s head: Expected class definition or the import of a library"
        elif self.grammeme == 603:
            return "Expected variable declaration or a valid statement"
        elif self.grammeme == 604:
            return "Variables: Expected a variable identifier"
        elif self.grammeme == 605:
            return "Variables declaration: Expected a , or the “as” reserved word"
        elif self.grammeme == 606:
            return "Type specification: Invalid type"
        elif self.grammeme == 607:
            return "Expected a valid statement or the “end” reserved word"
        elif self.grammeme == 608:
            return "Statement: Invalid start of statement"
        elif self.grammeme == 609:
            return "Assignment: Invalid start of assignment statement"
        elif self.grammeme == 610:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 611:
            return "Expression: Invalid expression, expected a delimiter or a logical disjunction"
        elif self.grammeme == 612:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 613:
            return "Expression: Invalid expression, expected a delimiter or a logical operation"
        elif self.grammeme == 614:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 615:
            return "Expression: Invalid expression, expected a delimiter or a logical negation"
        elif self.grammeme == 616:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 617:
            return "Expression: Invalid expression, expected a delimiter, a logical operation or a relational operator"
        elif self.grammeme == 618:
            return "Expression: Invalid expression, expected a relational operator"
        elif self.grammeme == 619:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 620:
            return "Expression: Invalid expression, expected a delimiter, a logical operation, a relational operator or an arithmetic addition"
        elif self.grammeme == 621:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 622:
            return "Expression: Invalid expression, expected a delimiter, a logical operation, a relational operator or an arithmetic operation"
        elif self.grammeme == 623:
            return "Expression: Invalid start of expression"
        elif self.grammeme == 624:
            return "If statement: Expected the reserved word “if”"
        elif self.grammeme == 625:
            return "If statement: Expected the reserved word “else” or “endif”"
        elif self.grammeme == 626:
            return "While loop: Expected the reserved word “while”"
        elif self.grammeme == 627:
            return "For loop: Expected the reserved word “while”";
        elif self.grammeme == 628:
            return "Expressions: Invalid start of expression"
        elif self.grammeme == 629:
            return "Expressions: Invalid expressions, expected a , or a closing parenthesis"
        elif self.grammeme == 630:
            return "Read instruction: Expected the reserved word “read”"
        elif self.grammeme == 631:
            return "Write instruction: Expected the reserved word “write”"
        elif self.grammeme == 632:
            return "Enter statement: Expected the reserved word “enter”"
        else:
            return "Unknown error"

    def __str__(self):
        return self.__repr__()

class SemanticAction(Symbol):

    def __init__(self, grammeme: int):
        super().__init__(grammeme)
