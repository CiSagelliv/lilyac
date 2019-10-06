import lilyac
from enum import Enum, auto


class Symbol:

    grammeme: str = ...
    terminal: bool = ...

    def __init__(self, grammeme: int):
        self.grammeme = grammeme
        self.terminal = False

    def __repr__(self):
        grammeme = ''
        if self.grammeme == lilyac.END_OF_FILE:
            grammeme = 'End of file'
        elif self.grammeme == lilyac.PROGRAM:
            grammeme = 'Program'
        elif self.grammeme == lilyac.DECL_LIBRARIES:
            grammeme = 'Declaration of libraries'
        elif self.grammeme == lilyac.DECL_VARIABLES:
            grammeme = 'Declaration of variables'
        elif self.grammeme == lilyac.VARIABLES:
            grammeme = 'Variables'
        elif self.grammeme == lilyac.MORE_VARIABLES:
            grammeme = 'More variables'
        elif self.grammeme == lilyac.TYPE:
            grammeme = 'Type'
        elif self.grammeme == lilyac.STATEMENTS:
            grammeme = 'Statements'
        elif self.grammeme == lilyac.STATEMENT:
            grammeme = 'Statement'
        elif self.grammeme == lilyac.ASSIGNMENT:
            grammeme = 'Assignment'
        elif self.grammeme == lilyac.EXPRESSION_0:
            grammeme = 'Expression 0'
        elif self.grammeme == lilyac.DISJUNCTION:
            grammeme = 'Disjunction'
        elif self.grammeme == lilyac.EXPRESSION_1:
            grammeme = 'Expression 1'
        elif self.grammeme == lilyac.CONJUNCTION:
            grammeme = 'Conjunction'
        elif self.grammeme == lilyac.EXPRESSION_2:
            grammeme = 'Expression 2'
        elif self.grammeme == lilyac.NEGATION:
            grammeme = 'Negation'
        elif self.grammeme == lilyac.EXPRESSION_3:
            grammeme = 'Expression 3'
        elif self.grammeme == lilyac.COMPARISON:
            grammeme = 'Comparison'
        elif self.grammeme == lilyac.RELATIONAL_OPERATOR:
            grammeme = 'Relational operator'
        elif self.grammeme == lilyac.EXPRESSION_4:
            grammeme = 'Expression 4'
        elif self.grammeme == lilyac.ADDITION:
            grammeme = 'Addition'
        elif self.grammeme == lilyac.ADDEND:
            grammeme = 'Addend'
        elif self.grammeme == lilyac.MULTIPLICATION:
            grammeme = 'Multiplication'
        elif self.grammeme == lilyac.FACTOR:
            grammeme = 'Factor'
        elif self.grammeme == lilyac.IF:
            grammeme = 'If statement'
        elif self.grammeme == lilyac.ELSE:
            grammeme = 'Else clause'
        elif self.grammeme == lilyac.WHILE:
            grammeme = 'While statement'
        elif self.grammeme == lilyac.FOR:
            grammeme = 'For statement'
        elif self.grammeme == lilyac.EXPRESSIONS:
            grammeme = 'Expressions'
        elif self.grammeme == lilyac.MORE_EXPRESSIONS:
            grammeme = 'More expressions'
        elif self.grammeme == lilyac.READ:
            grammeme = 'Read statement'
        elif self.grammeme == lilyac.WRITE:
            grammeme = 'Write statement'
        elif self.grammeme == lilyac.ENTER:
            grammeme = 'Enter statement'

        return f'<{grammeme}>'

    def __str__(self):
        return self.__repr__()


class Token(Symbol):

    lexeme: str = ...

    def __init__(self, grammeme: int, lexeme: str = ''):
        super().__init__(grammeme)
        self.lexeme = lexeme
        self.terminal = True

    def __eq__(self, other):
        return self.grammeme == other.grammeme

    def __repr__(self):
        grammeme = ''
        if self.grammeme == lilyac.RESERVED:
            if self.lexeme == 'class':
                grammeme = 'Reserved word: class'
            elif self.lexeme == 'begin':
                grammeme = 'Reserved word: begin'
            elif self.lexeme == 'end':
                grammeme = 'Reserved word: end'
            elif self.lexeme == 'def':
                grammeme = 'Reserved word: def'
            elif self.lexeme == 'as':
                grammeme = 'Reserved word: as'
            elif self.lexeme == 'integer':
                grammeme = 'Reserved word: integer'
            elif self.lexeme == 'float':
                grammeme = 'Reserved word: float'
            elif self.lexeme == 'char':
                grammeme = 'Reserved word: char'
            elif self.lexeme == 'string':
                grammeme = 'Reserved word: string'
            elif self.lexeme == 'boolean':
                grammeme = 'Reserved word: boolean'
            elif self.lexeme == 'if':
                grammeme = 'Reserved word: if'
            elif self.lexeme == 'else':
                grammeme = 'Reserved word: else'
            elif self.lexeme == 'elseif':
                grammeme = 'Reserved word: elseif'
            elif self.lexeme == 'endif':
                grammeme = 'Reserved word: endif'
            elif self.lexeme == 'for':
                grammeme = 'Reserved word: for'
            elif self.lexeme == 'do':
                grammeme = 'Reserved word: do'
            elif self.lexeme == 'endfor':
                grammeme = 'Reserved word: endfor'
            elif self.lexeme == 'while':
                grammeme = 'Reserved word: while'
            elif self.lexeme == 'endwhile':
                grammeme = 'Reserved word: endwhile'
            elif self.lexeme == 'function':
                grammeme = 'Reserved word: function'
            elif self.lexeme == 'endfunction':
                grammeme = 'Reserved word: endfunction'
            elif self.lexeme == 'import':
                grammeme = 'Reserved word: import'
            elif self.lexeme == 'null':
                grammeme = 'Reserved word: null'
            elif self.lexeme == 'read':
                grammeme = 'Reserved word: read'
            elif self.lexeme == 'write':
                grammeme = 'Reserved word: write'
            elif self.lexeme == 'enter':
                grammeme = 'Reserved word: enter'
            elif self.lexeme == 'principal':
                grammeme = 'Reserved word: principal'
        if self.grammeme == lilyac.IDENTIFIER:
            grammeme = 'Identifier'
        if self.grammeme == lilyac.LIBRARY:
            grammeme = 'Library identifier'
        if self.grammeme == lilyac.COMMENTARY:
            grammeme = 'Commentary'
        if self.grammeme == lilyac.INTEGER:
            grammeme = 'Integer value'
        if self.grammeme == lilyac.FLOAT:
            grammeme = 'Floating point value'
        if self.grammeme == lilyac.FLOATSCI:
            grammeme = 'Floating point value, scientific notation'
        if self.grammeme == lilyac.CHARACTER:
            grammeme = 'Character'
        if self.grammeme == lilyac.STRING:
            grammeme = 'String'
        if self.grammeme == lilyac.TIMES_SIGN:
            grammeme = 'Multiplication arithmetic operator'
        if self.grammeme == lilyac.OVER_SIGN:
            grammeme = 'Division arithmetic operator'
        if self.grammeme == lilyac.PLUS_SIGN:
            grammeme = 'Addition arithmetic operator'
        if self.grammeme == lilyac.MINUS_SIGN:
            grammeme = 'Substraction arithmetic operator'
        if self.grammeme == lilyac.MODULO:
            grammeme = 'Modulo sign'
        if self.grammeme == lilyac.OR:
            grammeme = 'OR logical operator'
        if self.grammeme == lilyac.AND:
            grammeme = 'AND logical operator'
        if self.grammeme == lilyac.NOT:
            grammeme = 'NOT logical operator'
        if self.grammeme == lilyac.LESSTHAN:
            grammeme = 'Less than relational operator'
        if self.grammeme == lilyac.LESSEQUALS:
            grammeme = 'Less than or equal relational operator'
        if self.grammeme == lilyac.GREATERTHAN:
            grammeme = 'Greater than relational operator'
        if self.grammeme == lilyac.GREATEREQUALS:
            grammeme = 'Greater than or equal relational operator'
        if self.grammeme == lilyac.EQUALS:
            grammeme = 'Equals relational operator'
        if self.grammeme == lilyac.NEQUALS:
            grammeme = 'Not equals relational operator'
        if self.grammeme == lilyac.EQUAL_SIGN:
            grammeme = 'Equals sign'
        if self.grammeme == lilyac.POINT:
            grammeme = 'Point'
        if self.grammeme == lilyac.COMMA:
            grammeme = 'Comma'
        if self.grammeme == lilyac.COLON:
            grammeme = 'Colon'
        if self.grammeme == lilyac.SEMICOLON:
            grammeme = 'Semicolon'
        if self.grammeme == lilyac.PARENTHESISOPEN:
            grammeme = 'Left parenthesis'
        if self.grammeme == lilyac.PARENTHESISCLOSE:
            grammeme = 'Right parenthesis'
        if self.grammeme == lilyac.BRACKETSOPEN:
            grammeme = 'Left bracket'
        if self.grammeme == lilyac.BRACKETSCLOSE:
            grammeme = 'Right bracket'
        if self.grammeme == lilyac.SQUAREBOPEN:
            grammeme = 'Left square bracket'
        if self.grammeme == lilyac.SQUAREBCLOSE:
            grammeme = 'Right square bracket'
        if self.grammeme == lilyac.END_OF_FILE:
            grammeme = 'End of file'
        if self.lexeme:
            return f'<{grammeme}, {self.lexeme}>'
        else:
            return f'<{grammeme}>'

    def __str__(self):
        return self.__repr__()


class Error(Symbol):

    def __init__(self, grammeme: int, **kwargs):
        super().__init__(grammeme)
        self.terminal = True
        if 'expected' in kwargs:
            self.expected = kwargs['expected']
        if 'found' in kwargs:
            self.found = kwargs['found']

    def __repr__(self):
        if self.grammeme == lilyac.ERRORIDENTIFIER:
            return 'Lexical Error: Malformed identifier'
        elif self.grammeme == lilyac.ERRORLIBRARY:
            return 'Lexical Error: Unknown library'
        elif self.grammeme == lilyac.ERRORFLOAT:
            return 'Lexical Error: It is not a float number'
        elif self.grammeme == lilyac.ERRORFLOATSCI:
            return 'Lexical Error: It is not a scientific notation'
        elif self.grammeme == lilyac.ERRORCHAR:
            return 'Lexical Error: It is not a character'
        elif self.grammeme == lilyac.ERROROR:
            return 'Lexical Error: It is not an OR'
        elif self.grammeme == lilyac.ERRORAND:
            return 'Lexical Error: It is not and AND'
        elif self.grammeme == lilyac.ERRORUNKNOWNL:
            return 'Lexical Error: Unknown error'
        elif self.grammeme == lilyac.ERRORPH_0:
            return 'Syntax Error: Program’s head: The program must start with either library declaration or class'
        elif self.grammeme == lilyac.ERRORPH_1:
            return 'Syntax Error: Program’s head: Expected class definition or the import of a library'
        elif self.grammeme == lilyac.ERROREVD:
            return 'Syntax Error: Expected variable declaration or a valid statement'
        elif self.grammeme == lilyac.ERROREVID:
            return 'Syntax Error: Variables: Expected a variable identifier'
        elif self.grammeme == lilyac.ERRORVARD:
            return 'Syntax Error: Variables declaration: Expected a , or the “as” reserved word'
        elif self.grammeme == lilyac.ERRORINVTY:
            return 'Syntax Error: Type specification: Invalid type'
        elif self.grammeme == lilyac.ERROREVST:
            return 'Syntax Error: Expected a valid statement or the “end” reserved word'
        elif self.grammeme == lilyac.ERRORISOST_O:
            return 'Syntax Error: Statement: Invalid start of statement'
        elif self.grammeme == lilyac.ERRORISOST_1:
            return 'Syntax Error: Assignment: Invalid start of assignment statement'
        elif self.grammeme == lilyac.ERRORISOEX_0:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORINVE_0:
            return 'Syntax Error: Expression: Invalid expression, expected a delimiter or a disjunction'
        elif self.grammeme == lilyac.ERRORISOEX_1:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORINVE_1:
            return 'Syntax Error: Expression: Invalid expression, expected a delimiter or a logical operation'
        elif self.grammeme == lilyac.ERRORISOEX_2:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORINVE_2:
            return 'Syntax Error: Expression: Invalid expression, expected a delimiter or a logical negation'
        elif self.grammeme == lilyac.ERRORISOEX_3:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORINVE_3:
            return 'Syntax Error: Expression: Invalid expression, expected a delimiter, a logical operation or a relational operator'
        elif self.grammeme == lilyac.ERRORINVE_4:
            return 'Syntax Error: Expression: Invalid expression, expected a relational operator'
        elif self.grammeme == lilyac.ERRORISOEX_4:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORINVE_5:
            return 'Syntax Error: Expression: Invalid expression, expected a delimiter, a logical operation, a relational operator or an arithmetic addition'
        elif self.grammeme == lilyac.ERRORISOEX_5:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORINVE_6:
            return 'Syntax Error: Expression: Invalid expression, expected a delimiter, a logical operation, a relational operator or an arithmetic operation'
        elif self.grammeme == lilyac.ERRORISOEX_6:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == lilyac.ERRORIFST_1:
            return 'Syntax Error: If statement: Expected the reserved word "if"'
        elif self.grammeme == lilyac.ERRORIFST_2:
            return 'Syntax Error: If statement: Expected the reserved word "else" or "endif"'
        elif self.grammeme == lilyac.ERRORWHLOOP:
            return 'Syntax Error: While loop: Expected the reserved word “while”'
        elif self.grammeme == lilyac.ERRORFOR:
            return 'Syntax Error: For loop: Expected the reserved word “while”'
        elif self.grammeme == lilyac.ERROREXIN_0:
            return 'Syntax Error: Expressions: Invalid start of expression'
        elif self.grammeme == lilyac.ERROREXIN_1:
            return 'Syntax Error: Expressions: Invalid expressions, expected a , or a closing parenthesis'
        elif self.grammeme == lilyac.ERRORREAD:
            return 'Syntax Error: Read instruction: Expected the reserved word “read”'
        elif self.grammeme == lilyac.ERRORWRITE:
            return 'Syntax Error: Write instruction: Expected the reserved word “write”'
        elif self.grammeme == lilyac.ERRORENTER:
            return 'Syntax Error: Enter statement: Expected the reserved word “enter”'
        elif self.grammeme == lilyac.ERROREXPECT:
            return f'Syntax Error: Expected a {self.expected}, but found: {self.found}'
        elif self.grammeme == lilyac.ERRORDERIVE:
            return f'Syntax Error: Invalid derivation: : Expected a {self.expected}, but found: {self.found}'
        elif ...:
            ...
        else:
            return 'Unknown error'

    def __str__(self):
        return self.__repr__()


class SemanticAction(Symbol):

    def __init__(self, grammeme: int):
        super().__init__(grammeme)

    def __repr__(self):
        return str(self.grammeme)

    def __str__(self):
        return self.__repr__()

    def __call__(self, im):
        if self.grammeme == lilyac._ID:
            pass
        elif self.grammeme == lilyac._TYPE:
            pass
        elif self.grammeme == lilyac._FACTOR_ID:
            pass
        elif self.grammeme == lilyac._FACTOR_INT:
            pass
        elif self.grammeme == lilyac._FACTOR_REAL:
            pass
        elif self.grammeme == lilyac._FACTOR_CHAR:
            pass
        elif self.grammeme == lilyac._FACTOR_STR:
            pass
        elif self.grammeme == lilyac._OPERATOR:
            pass
        elif self.grammeme == lilyac._OR:
            pass
        elif self.grammeme == lilyac._AND:
            pass
        elif self.grammeme == lilyac._NOT:
            pass
        elif self.grammeme == lilyac._RELATIONAL:
            pass
        elif self.grammeme == lilyac._ADDITION:
            pass
        elif self.grammeme == lilyac._MULTIPLICATION:
            pass
        elif self.grammeme == lilyac._ASSIGNMENT:
            pass
        elif self.grammeme == lilyac._BOTTOM:
            pass
        elif self.grammeme == lilyac._BOTTOM_D:
            pass
        elif self.grammeme == lilyac._GO_TO_TRUE:
            pass
        elif self.grammeme == lilyac._GO_TO_FALSE:
            pass
        elif self.grammeme == lilyac._GO_TO:
            pass
        elif self.grammeme == lilyac._FILL_JUMP:
            pass
        elif self.grammeme == lilyac._READ:
            pass
        elif self.grammeme == lilyac._WRITE:
            pass
        elif self.grammeme == lilyac._ENTER:
            pass


class Type(Enum):
    ''' Data types
    '''
    Boolean = auto()
    Integer = auto()
    Real = auto()
    Character = auto()
    String = auto()
    Error = auto()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __sub__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __mul__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __truediv__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __mod__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __and__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __or__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __lt__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __le__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __eq__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __ne__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __gt__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    def __ge__(self, other):
        if ...:
            pass
        else:
            return Type.Error

    @staticmethod
    def JF(factor):
        pass

    # Add rest of operations, ej JF, JT, J, Write, Read, ...
