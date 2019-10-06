from typing import List, Dict

from .symbol import Symbol, Token, Error, SemanticAction

# Lexicon
# Terminals
RESERVED: int = 101
IDENTIFIER: int = 102
LIBRARY: int = 103
COMMENTARY: int = 104
INTEGER: int = 105
FLOAT: int = 106
FLOATSCI: int = 107
CHARACTER: int = 108
STRING: int = 109
TIMES_SIGN: int = 110
OVER_SIGN: int = 111
PLUS_SIGN: int = 112
MINUS_SIGN: int = 113
MODULO: int = 114
OR: int = 115
AND: int = 116
NOT: int = 117
LESSTHAN: int = 118
LESSEQUALS: int = 119
GREATERTHAN: int = 120
GREATEREQUALS: int = 121
EQUALS: int = 122
NEQUALS: int = 123
EQUAL_SIGN: int = 124
POINT: int = 125
COMMA: int = 126
COLON: int = 127
SEMICOLON: int = 128
PARENTHESISOPEN: int = 129
PARENTHESISCLOSE: int = 130
BRACKETSOPEN: int = 131
BRACKETSCLOSE: int = 132
SQUAREBOPEN: int = 133
SQUAREBCLOSE: int = 134

# Error States
ERRORIDENTIFIER: int = 501
ERRORLIBRARY: int = 502
ERRORFLOAT: int = 503
ERRORFLOATSCI: int = 504
ERRORCHAR: int = 505
ERROROR: int = 506
ERRORAND: int = 507
ERRORUNKNOWN: int = 599



# Syntax
END_OF_FILE: int = -1
PROGRAM: int = 0
DECL_LIBRARIES: int = 1
DECL_VARIABLES: int = 2
VARIABLES: int = 3
MORE_VARIABLES: int = 4
TYPE: int = 5
STATEMENTS: int = 6
STATEMENT: int = 7
ASSIGNMENT: int = 8
EXPRESSION_0: int = 9
DISJUNCTION: int = 10
EXPRESSION_1: int = 11
CONJUNCTION: int = 12
EXPRESSION_2: int = 13
NEGATION: int = 14
EXPRESSION_3: int = 15
COMPARISON: int = 16
RELATIONAL_OPERATOR: int = 17
EXPRESSION_4: int = 18
ADDITION: int = 19
ADDEND: int = 20
MULTIPLICATION: int = 21
FACTOR: int = 22
IF: int = 23
ELSE: int = 24
WHILE: int = 25
FOR: int = 26
EXPRESSIONS: int = 27
MORE_EXPRESSIONS: int = 28
READ: int = 29
WRITE: int = 30
ENTER: int = 31

#Semantic actions
.ID: int = 701
.TYPE: int = 702
.FACTOR_ID: int = 703
.FACTOR_INT: int = 704
.FACTOR_REAL: int = 705
.FACTOR_CHAR: int = 706
.FACTOR_STR: int = 707
.OPERATOR: int = 708
.OR: int = 709
.AND: int = 710
.NOT: int = 711
.RELATIONAL: int = 712
.ADDITION: int = 713
.MULTIPLICATION: int = 714
.ASSIGNMENT: int = 715
.BOTTOM: int =  716
.BOTTOM_D: int = 717
.GO_TO_TRUE: int = 718
.GO_TO_FALSE: int = 719
.GO_TO: int = 720
.FILL_JUMP: int = 721
.READ: int = 722
.WRITE: int = 723
.ENTER: int =  724

reserved_words: List[str] = [
    'class',
    'begin',
    'end',
    'def',
    'as',
    'integer',
    'float',
    'char',
    'string',
    'boolean',
    'if',
    'else',
    'elseif',
    'endif',
    'for',
    'do',
    'endfor',
    'while',
    'endwhile',
    'function',
    'endfunction',
    'import',
    'null',
    'read',
    'write',
    'enter',
    'principal',
]

derivations: Dict = {
    0: [
        Symbol(DECL_LIBRARIES),
        Token(RESERVED, 'class'),
        Token(IDENTIFIER),
        Token(RESERVED, 'begin'),
        Symbol(DECL_VARIABLES),
        Symbol(STATEMENTS),
        Token(RESERVED, 'end'),
    ],
    1: [
        Token(RESERVED, 'import'),
        Token(LIBRARY),
        Token(SEMICOLON, ';'),
        Symbol(DECL_LIBRARIES),
    ],
    3: [
        Token(RESERVED, 'def'),
        Symbol(VARIABLES),
        Token(RESERVED, 'as'),
        Symbol(TYPE),
        Token(SEMICOLON, ';'),
        Symbol(DECL_VARIABLES),
    ],
    5: [
        Token(IDENTIFIER),
        Symbol(MORE_VARIABLES),
    ],
    6: [
        Token(COMMA, ','),
        Symbol(VARIABLES),
    ],
    8: [
        Token(RESERVED, 'integer'),
    ],
    9: [
        Token(RESERVED, 'float'),
    ],
    10: [
        Token(RESERVED, 'char'),
    ],
    11: [
        Token(RESERVED, 'string'),
    ],
    12: [
        Token(RESERVED, 'boolean'),
    ],
    13: [
        Symbol(STATEMENT),
        Token(SEMICOLON, ';'),
        Symbol(STATEMENTS),
    ],
    15: [
        Symbol(ASSIGNMENT),
    ],
    16: [
        Symbol(IF),
    ],
    17: [
        Symbol(WHILE),
    ],
    18: [
        Symbol(FOR),
    ],
    19: [
        Symbol(READ),
    ],
    20: [
        Symbol(WRITE),
    ],
    21: [
        Symbol(ENTER),
    ],
    22: [
        Token(IDENTIFIER),
        Token(EQUAL_SIGN, '='),
        Symbol(EXPRESSION_0),
    ],
    23: [
        Symbol(EXPRESSION_1),
        Symbol(DISJUNCTION),
    ],
    24: [
        Token(OR, '||'),
        Symbol(EXPRESSION_0),
    ],
    26: [
        Symbol(EXPRESSION_2),
        Symbol(CONJUNCTION),
    ],
    27: [
        Token(AND, '&&'),
        Symbol(EXPRESSION_1),
    ],
    29: [
        Symbol(NEGATION),
        Symbol(EXPRESSION_3),
    ],
    30: [
        Token(NOT, '!'),
    ],
    32: [
        Symbol(EXPRESSION_4),
        Symbol(COMPARISON),
    ],
    33: [
        Symbol(RELATIONAL_OPERATOR),
        Symbol(EXPRESSION_4),
    ],
    35: [
        Token(EQUALS, '=='),
    ],
    36: [
        Token(NEQUALS, '!='),
    ],
    37: [
        Token(LESSTHAN, '<'),
    ],
    38: [
        Token(LESSEQUALS, '<='),
    ],
    39: [
        Token(GREATERTHAN, '>'),
    ],
    40: [
        Token(GREATEREQUALS, '>='),
    ],
    41: [
        Symbol(ADDEND),
        Symbol(ADDITION),
    ],
    42: [
        Token(PLUS_SIGN, '+'),
        Symbol(EXPRESSION_4),
    ],
    43: [
        Token(MINUS_SIGN, '-'),
        Symbol(EXPRESSION_4),
    ],
    45: [
        Symbol(FACTOR),
        Symbol(MULTIPLICATION),
    ],
    46: [
        Token(TIMES_SIGN, '*'),
        Symbol(ADDEND),
    ],
    47: [
        Token(OVER_SIGN, '/'),
        Symbol(ADDEND),
    ],
    48: [
        Token(MODULO, '%'),
        Symbol(ADDEND),
    ],
    50: [
        Token(IDENTIFIER),
    ],
    51: [
        Token(INTEGER),
    ],
    52: [
        Token(FLOAT),
    ],
    53: [
        Token(FLOATSCI),
    ],
    54: [
        Token(CHARACTER),
    ],
    55: [
        Token(STRING),
    ],
    56: [
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
    ],
    57: [
        Token(RESERVED, 'if'),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
        Symbol(STATEMENTS),
        Symbol(ELSE),
        Token(RESERVED, 'endif'),
    ],
    58: [
        Token(RESERVED, 'else'),
        Symbol(STATEMENTS),
    ],
    60: [
        Token(RESERVED, 'while'),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
        Symbol(STATEMENTS),
        Token(RESERVED, 'endwhile'),
    ],
    61: [
        Token(RESERVED, 'for'),
        Token(PARENTHESISOPEN, '('),
        Symbol(ASSIGNMENT),
        Token(COLON, ':'),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
        Symbol(STATEMENTS),
        Token(RESERVED, 'endfor'),
    ],
    62: [
        Symbol(EXPRESSION_0),
        Symbol(MORE_EXPRESSIONS),
    ],
    63: [
        Token(COMMA, ','),
        Symbol(EXPRESSIONS),
    ],
    65: [
        Token(RESERVED, 'read'),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSIONS),
        Token(PARENTHESISCLOSE, ')'),
    ],
    66: [
        Token(RESERVED, 'write'),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSIONS),
        Token(PARENTHESISCLOSE, ')'),
    ],
    67: [
        Token(RESERVED, 'enter'),
    ],
}
