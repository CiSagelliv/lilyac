import Compiler
from enum import Enum, auto


class Symbol:

    grammeme: str = ...
    terminal: bool = ...

    def __init__(self, grammeme: int):
        self.grammeme = grammeme
        self.terminal = False

    def __repr__(self):
        grammeme = ''
        if self.grammeme == END_OF_FILE:
            grammeme = 'End of file'
        elif self.grammeme == PROGRAM:
            grammeme = 'Program'
        elif self.grammeme == DECL_LIBRARIES:
            grammeme = 'Declaration of libraries'
        elif self.grammeme == DECL_VARIABLES:
            grammeme = 'Declaration of variables'
        elif self.grammeme == VARIABLES:
            grammeme = 'Variables'
        elif self.grammeme == MORE_VARIABLES:
            grammeme = 'More variables'
        elif self.grammeme == TYPE:
            grammeme = 'Type'
        elif self.grammeme == STATEMENTS:
            grammeme = 'Statements'
        elif self.grammeme == STATEMENT:
            grammeme = 'Statement'
        elif self.grammeme == ASSIGNMENT:
            grammeme = 'Assignment'
        elif self.grammeme == EXPRESSION_0:
            grammeme = 'Expression 0'
        elif self.grammeme == DISJUNCTION:
            grammeme = 'Disjunction'
        elif self.grammeme == EXPRESSION_1:
            grammeme = 'Expression 1'
        elif self.grammeme == CONJUNCTION:
            grammeme = 'Conjunction'
        elif self.grammeme == EXPRESSION_2:
            grammeme = 'Expression 2'
        elif self.grammeme == NEGATION:
            grammeme = 'Negation'
        elif self.grammeme == EXPRESSION_3:
            grammeme = 'Expression 3'
        elif self.grammeme == COMPARISON:
            grammeme = 'Comparison'
        elif self.grammeme == RELATIONAL_OPERATOR:
            grammeme = 'Relational operator'
        elif self.grammeme == EXPRESSION_4:
            grammeme = 'Expression 4'
        elif self.grammeme == ADDITION:
            grammeme = 'Addition'
        elif self.grammeme == ADDEND:
            grammeme = 'Addend'
        elif self.grammeme == MULTIPLICATION:
            grammeme = 'Multiplication'
        elif self.grammeme == FACTOR:
            grammeme = 'Factor'
        elif self.grammeme == IF:
            grammeme = 'If statement'
        elif self.grammeme == ELSE:
            grammeme = 'Else clause'
        elif self.grammeme == WHILE:
            grammeme = 'While statement'
        elif self.grammeme == FOR:
            grammeme = 'For statement'
        elif self.grammeme == EXPRESSIONS:
            grammeme = 'Expressions'
        elif self.grammeme == MORE_EXPRESSIONS:
            grammeme = 'More expressions'
        elif self.grammeme == READ:
            grammeme = 'Read statement'
        elif self.grammeme == WRITE:
            grammeme = 'Write statement'
        elif self.grammeme == ENTER:
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

    def __repr__(self):
        grammeme = ''
        if token.grammeme == Compiler.RESERVED:
            if (token.lexeme == 'class'):
                grammeme = 'Reserved word: class'
            elif token.lexeme == 'begin':
                grammeme = 'Reserved word: begin'
            elif token.lexeme == 'end':
                grammeme = 'Reserved word: end'
            elif token.lexeme == 'def':
                grammeme = 'Reserved word: def'
            elif token.lexeme == 'as':
                grammeme = 'Reserved word: as'
            elif token.lexeme == 'integer':
                grammeme = 'Reserved word: integer'
            elif token.lexeme == 'float':
                grammeme = 'Reserved word: float'
            elif token.lexeme == 'char':
                grammeme = 'Reserved word: char'
            elif token.lexeme == 'string':
                grammeme = 'Reserved word: string'
            elif token.lexeme == 'boolean':
                grammeme = 'Reserved word: boolean'
            elif token.lexeme == 'if':
                grammeme = 'Reserved word: if'
            elif token.lexeme == 'else':
                grammeme = 'Reserved word: else'
            elif token.lexeme == 'elseif':
                grammeme = 'Reserved word: elseif'
            elif token.lexeme == 'endif':
                grammeme = 'Reserved word: endif'
            elif token.lexeme == 'for':
                grammeme = 'Reserved word: for'
            elif token.lexeme == 'do':
                grammeme = 'Reserved word: do'
            elif token.lexeme == 'endfor':
                grammeme = 'Reserved word: endfor'
            elif token.lexeme == 'while':
                grammeme = 'Reserved word: while'
            elif token.lexeme == 'endwhile':
                grammeme = 'Reserved word: endwhile'
            elif token.lexeme == 'function':
                grammeme = 'Reserved word: function'
            elif token.lexeme == 'endfunction':
                grammeme = 'Reserved word: endfunction'
            elif token.lexeme == 'import':
                grammeme = 'Reserved word: import'
            elif token.lexeme == 'null':
                grammeme = 'Reserved word: null'
            elif token.lexeme == 'read':
                grammeme = 'Reserved word: read'
            elif token.lexeme == 'write':
                grammeme = 'Reserved word: write'
            elif token.lexeme == 'enter':
                grammeme = 'Reserved word: enter'
            elif token.lexeme == 'principal':
                grammeme = 'Reserved word: principal'
        if token.grammeme == Compiler.IDENTIFIER:
            grammeme = 'Identifier'
        if token.grammeme == Compiler.LIBRARY:
            grammeme = 'Library identifier'
        if token.grammeme == Compiler.COMMENTARY:
            grammeme = 'Commentary'
        if token.grammeme == Compiler.INTEGER:
            grammeme = 'Integer value'
        if token.grammeme == Compiler.FLOAT:
            grammeme = 'Floating point value'
        if token.grammeme == Compiler.FLOATSCI:
            grammeme = 'Floating point value, scientific notation'
        if token.grammeme == Compiler.CHARACTER:
            grammeme = 'Character'
        if token.grammeme == Compiler.STRING:
            grammeme = 'String'
        if token.grammeme == Compiler.TIMES_SIGN:
            grammeme = 'Multiplication arithmetic operator'
        if token.grammeme == Compiler.OVER_SIGN:
            grammeme = 'Division arithmetic operator'
        if token.grammeme == Compiler.PLUS_SIGN:
            grammeme = 'Addition arithmetic operator'
        if token.grammeme == Compiler.MINUS_SIGN:
            grammeme = 'Substraction arithmetic operator'
        if token.grammeme == Compiler.MODULO:
            grammeme = 'Modulo sign'
        if token.grammeme == Compiler.OR:
            grammeme = 'OR logical operator'
        if token.grammeme == Compiler.AND:
            grammeme = 'AND logical operator'
        if token.grammeme == Compiler.NOT:
            grammeme = 'NOT logical operator'
        if token.grammeme == Compiler.LESSTHAN:
            grammeme = 'Less than relational operator'
        if token.grammeme == Compiler.LESSEQUALS:
            grammeme = 'Less than or equal relational operator'
        if token.grammeme == Compiler.GREATERTHAN:
            grammeme = 'Greater than relational operator'
        if token.grammeme == Compiler.GREATEREQUALS:
            grammeme = 'Greater than or equal relational operator'
        if token.grammeme == Compiler.EQUALS:
            grammeme = 'Equals relational operator'
        if token.grammeme == Compiler.NEQUALS:
            grammeme = 'Not equals relational operator'
        if token.grammeme == Compiler.EQUAL_SIGN:
            grammeme = 'Equals sign'
        if token.grammeme == Compiler.POINT:
            grammeme = 'Point'
        if token.grammeme == Compiler.COMMA:
            grammeme = 'Comma'
        if token.grammeme == Compiler.COLON:
            grammeme = 'Colon'
        if token.grammeme == Compiler.SEMICOLON:
            grammeme = 'Semicolon'
        if token.grammeme == Compiler.PARENTHESISOPEN:
            grammeme = 'Left parenthesis'
        if token.grammeme == Compiler.PARENTHESISCLOSE:
            grammeme = 'Right parenthesis'
        if token.grammeme == Compiler.BRACKETSOPEN:
            grammeme = 'Left bracket'
        if token.grammeme == Compiler.BRACKETSCLOSE:
            grammeme = 'Right bracket'
        if token.grammeme == Compiler.SQUAREBOPEN:
            grammeme = 'Left square bracket'
        if token.grammeme == Compiler.SQUAREBCLOSE:
            grammeme = 'Right square bracket'
        if token.grammeme == Compiler.END_OF_FILE:
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
        if self.grammeme == Compiler.ERRORIDENTIFIER:
            return 'Lexical Error: Malformed identifier'
        elif self.grammeme == Compiler.ERRORLIBRARY:
            return 'Lexical Error: Unknown library'
        elif self.grammeme == Compiler.ERRORFLOAT:
            return 'Lexical Error: It is not a float number'
        elif self.grammeme == Compiler.ERRORFLOATSCI:
            return 'Lexical Error: It is not a scientific notation'
        elif self.grammeme == Compiler.ERRORCHAR:
            return 'Lexical Error: It is not a character'
        elif self.grammeme == Compiler.ERROROR:
            return 'Lexical Error: It is not an OR'
        elif self.grammeme == Compiler.ERRORAND:
            return 'Lexical Error: It is not and AND'
        elif self.grammeme == Compiler.ERRORUNKNOWN:
            return 'Lexical Error: Unknown error'
        elif self.grammeme == Compiler.ERRORPH_0:
            return 'Syntax Error: Program’s head: '
            + 'The program must start with either library declaration or class'
        elif self.grammeme == Compiler.ERRORPH_1:
            return 'Syntax Error: Program’s head: '
            + 'Expected class definition or the import of a library'
        elif self.grammeme == Compiler.ERROREVD:
            return 'Syntax Error: '
            + 'Expected variable declaration or a valid statement'
        elif self.grammeme == Compiler.ERROREVID:
            return 'Syntax Error: Variables: Expected a variable identifier'
        elif self.grammeme == Compiler.ERRORVARD:
            return 'Syntax Error: Variables declaration: '
            + 'Expected a , or the “as” reserved word'
        elif self.grammeme == Compiler.ERRORINVTY:
            return 'Syntax Error: Type specification: Invalid type'
        elif self.grammeme == Compiler.ERROREVST:
            return 'Syntax Error: '
            + 'Expected a valid statement or the “end” reserved word'
        elif self.grammeme == Compiler.ERRORISOST_O:
            return 'Syntax Error: Statement: Invalid start of statement'
        elif self.grammeme == Compiler.ERRORISOST_1:
            return 'Syntax Error: Assignment: '
            + 'Invalid start of assignment statement'
        elif self.grammeme == Compiler.ERRORISOEX_0:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORINVE_0:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a delimiter or a disjunction'
        elif self.grammeme == Compiler.ERRORISOEX_1:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORINVE_1:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a delimiter or a logical operation'
        elif self.grammeme == Compiler.ERRORISOEX_2:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORINVE_2:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a delimiter or a logical negation'
        elif self.grammeme == Compiler.ERRORISOEX_3:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORINVE_3:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a delimiter, '
            + 'a logical operation or a relational operator'
        elif self.grammeme == Compiler.ERRORINVE_4:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a relational operator'
        elif self.grammeme == Compiler.ERRORISOEX_4:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORINVE_5:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a delimiter, a logical operation, '
            + 'a relational operator or an arithmetic addition'
        elif self.grammeme == Compiler.ERRORISOEX_5:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORINVE_6:
            return 'Syntax Error: Expression: '
            + 'Invalid expression, expected a delimiter, a logical operation, '
            + 'a relational operator or an arithmetic operation'
        elif self.grammeme == Compiler.ERRORISOEX_6:
            return 'Syntax Error: Expression: Invalid start of expression'
        elif self.grammeme == Compiler.ERRORIFST_1:
            return 'Syntax Error: If statement: '
            + 'Expected the reserved word "if"'
        elif self.grammeme == Compiler.ERRORIFST_2:
            return 'Syntax Error: If statement: '
            + 'Expected the reserved word "else" or "endif"'
        elif self.grammeme == Compiler.ERRORWHLOOP:
            return 'Syntax Error: While loop: '
            + 'Expected the reserved word “while”'
        elif self.grammeme == Compiler.ERRORFOR:
            return 'Syntax Error: For loop: Expected the reserved word “while”'
        elif self.grammeme == Compiler.ERROREXIN_0:
            return 'Syntax Error: Expressions: Invalid start of expression'
        elif self.grammeme == Compiler.ERROREXIN_1:
            return 'Syntax Error: Expressions: '
            + 'Invalid expressions, expected a , or a closing parenthesis'
        elif self.grammeme == Compiler.ERRORREAD:
            return 'Syntax Error: Read instruction: '
            + 'Expected the reserved word “read”'
        elif self.grammeme == Compiler.ERRORWRITE:
            return 'Syntax Error: Write instruction: '
            + 'Expected the reserved word “write”'
        elif self.grammeme == Compiler.ERRORENTER:
            return 'Syntax Error: Enter statement: '
            + 'Expected the reserved word “enter”'
        elif self.grammeme == Compiler.ERROREXPECT:
            return 'Syntax Error: '
            + f'Expected a {self.expected}, but found: {self.found}'
        elif self.grammeme == Compiler.ERRORDERIVE:
            return 'Syntax Error: Invalid derivation'
        elif ...:
            ...
        else:
            return 'Unknown error'

    def __str__(self):
        return self.__repr__()


class SemanticAction(Symbol):

    def __init__(self, grammeme: int):
        super().__init__(grammeme)

    def __call__(self, im: Intermediate):
        if self.grammeme == Compiler._ID:
            pass
        elif self.grammeme == Compiler._TYPE:
            pass
        elif self.grammeme == Compiler._FACTOR_ID:
            pass
        elif self.grammeme == Compiler._FACTOR_INT:
            pass
        elif self.grammeme == Compiler._FACTOR_REAL:
            pass
        elif self.grammeme == Compiler._FACTOR_CHAR:
            pass
        elif self.grammeme == Compiler._FACTOR_STR:
            pass
        elif self.grammeme == Compiler._OPERATOR:
            pass
        elif self.grammeme == Compiler._OR:
            pass
        elif self.grammeme == Compiler._AND:
            pass
        elif self.grammeme == Compiler._NOT:
            pass
        elif self.grammeme == Compiler._RELATIONAL:
            pass
        elif self.grammeme == Compiler._ADDITION:
            pass
        elif self.grammeme == Compiler._MULTIPLICATION:
            pass
        elif self.grammeme == Compiler._ASSIGNMENT:
            pass
        elif self.grammeme == Compiler._BOTTOM:
            pass
        elif self.grammeme == Compiler._BOTTOM_D:
            pass
        elif self.grammeme == Compiler._GO_TO_TRUE:
            pass
        elif self.grammeme == Compiler._GO_TO_FALSE:
            pass
        elif self.grammeme == Compiler._GO_TO:
            pass
        elif self.grammeme == Compiler._FILL_JUMP:
            pass
        elif self.grammeme == Compiler._READ:
            pass
        elif self.grammeme == Compiler._WRITE:
            pass
        elif self.grammeme == Compiler._ENTER:
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
