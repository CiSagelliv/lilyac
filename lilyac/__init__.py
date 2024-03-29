from .symbol import Symbol, Token, Error, SemanticAction, Type
from .lexer import Lexer
from .parser import Parser
from .intermediate import Intermediate

from typing import List, Dict


''' Lexicon '''
''' Terminal states

    Code values: 101 - 199
'''
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

from .optimization import optimize_jumps, optimize_temporals
from .execution import Execution
from .compiler_int import compiler

''' Lexical Errors

    Code values: 501 - 599
'''
ERRORIDENTIFIER: int = 501
ERRORLIBRARY: int = 502
ERRORFLOAT: int = 503
ERRORFLOATSCI: int = 504
ERRORCHAR: int = 505
ERROROR: int = 506
ERRORAND: int = 507
ERRORUNKNOWNL: int = 599


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


''' Transition matrix

    Defines the transition function δ of the lexer's automaton
    δ: Q ✖ S -> Q

    Q := States
    S := Input alphabet

    Rows correspond to states
    Columns correspond to symbols from the alphabet
'''
transitions: List[List[int]] = [
    [2,   1,   1,   1,   1,   2,   10,  599, 19,  7,   20,  21,  22,  35,  16,  18,  0,   23,  25,  27,  28,  30,  34,  36,  126, 128, 129, 130, 131, 132, 133, 134, 599],
    [2,   1,   1,   1,   1,   2,   2,   3,   101, 101, 101, 101, 101, 4,   101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101],
    [2,   2,   2,   2,   2,   2,   2,   3,   102, 102, 102, 102, 102, 4,   102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102],
    [2,   2,   2,   2,   2,   2,   2,   501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501],
    [502, 502, 5,   502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502],
    [502, 502, 502, 6,   502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502],
    [502, 103, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502],
    [111, 111, 111, 111, 111, 111, 111, 111, 8,   111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
    [8,   8,   6,   7,   8,   8,   8,   8,   9,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8],
    [8,   8,   6,   7,   8,   8,   8,   8,   9,   104, 8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8,   8],
    [105, 105, 105, 105, 105, 105, 10,  105, 105, 105, 105, 105, 105, 11,  105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105],
    [503, 503, 503, 503, 503, 503, 12,  503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503],
    [13,  13,  106, 106, 106, 106, 12,  106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106],
    [504, 504, 504, 504, 504, 504, 15,  504, 504, 504, 14,  14,  504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504],
    [504, 504, 504, 504, 504, 504, 15,  504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504],
    [107, 107, 107, 107, 107, 107, 15,  107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107],
    [17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  108, 17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17],
    [505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 108, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505],
    [18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  109, 18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18,  18],
    [110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110],
    [112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112],
    [113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113],
    [114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114],
    [506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 24,  506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506, 506],
    [115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115],
    [507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 26,  507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507],
    [116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116],
    [117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 33,  117, 117, 117, 117, 117, 117, 117, 117, 117, 117],
    [118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 29,  118, 118, 118, 118, 118, 118, 118, 118, 118, 118],
    [119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119, 119],
    [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 31,  120, 120, 120, 120, 120, 120, 120, 120, 120, 120],
    [121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121],
    [122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122],
    [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123],
    [124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 124, 32,  124, 124, 124, 124, 124, 124, 124, 124, 124, 124],
    [125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125],
    [127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127]
]


''' Syntax '''
''' Non-terminal Symbols

    Code values: -1 - 100
'''
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


''' Syntax Errors

    Code values: 601 - 699
'''
ERRORPH_0: int = 601
ERRORPH_1: int = 602
ERROREVD: int = 603
ERROREVID: int = 604
ERRORVARD: int = 605
ERRORINVTY: int = 606
ERROREVST: int = 607
ERRORISOST_O: int = 608
ERRORISOST_1: int = 609
ERRORISOEX_0: int = 610
ERRORINVE_0: int = 611
ERRORISOEX_1: int = 612
ERRORINVE_1: int = 613
ERRORISOEX_2: int = 614
ERRORINVE_2: int = 615
ERRORISOEX_3: int = 616
ERRORINVE_3: int = 617
ERRORINVE_4: int = 618
ERRORISOEX_4: int = 619
ERRORINVE_5: int = 620
ERRORISOEX_5: int = 621
ERRORINVE_6: int = 622
ERRORISOEX_6: int = 623
ERRORIFST_1: int = 624
ERRORIFST_2: int = 625
ERRORWHLOOP: int = 626
ERRORFOR: int = 627
ERROREXIN_0: int = 628
ERROREXIN_1: int = 629
ERRORREAD: int = 630
ERRORWRITE: int = 631
ERRORENTER: int = 632
ERROREXPECT: int = 633
ERRORDERIVE: int = 634
ERRORUNKNOWNP: int = 699


''' Prediction Matrix

    Used by the parser to determine appropiate derivation of
    non-terminal symbols according to encountered terminal symbol

    Defines the prediction function P for the grammar

    P: V ✖ Σ -> R

    V := Non-terminal symbols
    Σ := Terminal symbols
    R := Productions

    Rows correspond to non-terminal symbols
    Columns correspond to terminal symbols
'''
predictions: List[List[int]] = [
    [0,   601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 0,   601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601, 601],
    [2,   602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 1,   602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602, 602],
    [603, 603, 4,   3,   603, 603, 603, 603, 603, 603, 4,   603, 603, 603, 4,   603, 603, 4,   603, 603, 603, 603, 603, 4,   4,   4,   603, 4,   603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603, 603],
    [604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 5,   604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604, 604],
    [605, 605, 605, 605, 7,   605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 605, 6,   605, 605, 605, 605, 605, 605, 605, 605, 605],
    [606, 606, 606, 606, 606, 8,   9,   10,  11,  12,  606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606, 606],
    [607, 607, 14,  607, 607, 607, 607, 607, 607, 607, 13,  14,  607, 14,  13,  607, 14,  13,  14,  607, 607, 607, 607, 13,  13,  13,  607, 13,  607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607, 607],
    [608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 16,  608, 608, 608, 18,  608, 608, 17,  608, 608, 608, 608, 608, 19,  20,  21,  608, 15,  608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608, 608],
    [609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 22,  609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609, 609],
    [610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 23,  610, 610, 23,  23,  23,  23,  23,  610, 610, 610, 610, 610, 610, 610, 23,  610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 610, 23,  610, 610, 610, 610, 610, 610],
    [611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 24,  611, 611, 611, 611, 611, 611, 611, 611, 611, 611, 25,  25,  25,  611, 25,  611, 611, 611, 611, 611],
    [612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 26,  612, 612, 26,  26,  26,  26,  26,  612, 612, 612, 612, 612, 612, 612, 26,  612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 612, 26,  612, 612, 612, 612, 612, 612],
    [613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 613, 27,  613, 613, 613, 613, 613, 613, 613, 613, 613, 28,  28,  28,  613, 28,  613, 613, 613, 613, 613],
    [614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 29,  614, 614, 29,  29,  29,  29,  29,  614, 614, 614, 614, 614, 614, 614, 29,  614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 614, 29,  614, 614, 614, 614, 614, 614],
    [615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 31,  615, 615, 31,  31,  31,  31,  31,  615, 615, 615, 615, 615, 615, 615, 30,  615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 615, 31,  615, 615, 615, 615, 615, 615],
    [616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 32,  616, 616, 32,  32,  32,  32,  32,  616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 616, 32,  616, 616, 616, 616, 616, 616],
    [617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 617, 34,  34,  617, 33,  33,  33,  33,  33,  33,  617, 617, 34,  34,  34,  617, 34,  617, 617, 617, 617, 617],
    [618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 37,  38,  39,  40,  35,  36,  618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618, 618],
    [619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 41,  619, 619, 41,  41,  41,  41,  41,  619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 619, 41,  619, 619, 619, 619, 619, 619],
    [620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 620, 42,  43,  620, 44,  44,  620, 44,  44,  44,  44,  44,  44,  620, 620, 44,  44,  44,  620, 44,  620, 620, 620, 620, 620],
    [621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 45,  621, 621, 45,  45,  45,  45,  45,  621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 621, 45,  621, 621, 621, 621, 621, 621],
    [622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 622, 46,  47,  49,  49,  48,  49,  49,  622, 49,  49,  49,  49,  49,  49,  622, 622, 49,  49,  49,  622, 49,  622, 622, 622, 622, 622],
    [623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 50,  623, 623, 51,  52,  53,  54,  55,  623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 623, 56,  623, 623, 623, 623, 623, 623],
    [624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 57,  624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624, 624],
    [625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 58,  625, 59,  625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625, 625],
    [626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 60,  626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626, 626],
    [627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 61,  627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627, 627],
    [628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 62,  628, 628, 62,  62,  62,  62,  62,  628, 628, 628, 628, 628, 628, 628, 62,  628, 628, 628, 628, 628, 628, 628, 628, 628, 628, 628,  62, 628, 628, 628, 628, 628, 628],
    [629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 629, 63,  629, 629, 629, 64,  629, 629, 629, 629, 629],
    [630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 65,  630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630, 630],
    [631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 66,  631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631, 631],
    [632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 67,  632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632, 632]
]


''' Semantics '''
''' Semantic actions

    Code values: 1001 - 1099
'''
_ID: int = 1001
_TYPE: int = 1002
_FACTOR_ID: int = 1003
_FACTOR_INT: int = 1004
_FACTOR_REAL: int = 1005
_FACTOR_CHAR: int = 1006
_FACTOR_STR: int = 1007
_OPERATOR: int = 1008
_OR: int = 1009
_AND: int = 1010
_NOT: int = 1011
_RELATIONAL: int = 1012
_ADDITION: int = 1013
_MULTIPLICATION: int = 1014
_ASSIGNMENT: int = 1015
_BOTTOM: int = 1016
_BOTTOM_D: int = 1017
_GO_TO_TRUE: int = 1018
_GO_TO_FALSE: int = 1019
_GO_TO: int = 1020
_GO_TO_BACK: int = 1021
_FILL_JUMP: int = 1022
_FILL_JUMP_1: int = 1023
_BOTTOM_F: int = 1024
_BOTTOM_F_D: int = 1025
_READWRITE: int = 1026
_READWRITE_O: int = 1027
_INCREMENT: int = 1028
_FOR_COMPARISON: int = 1029
_ENTER: int = 1030


''' Semantic Errors

    Code values: 701 - 799
'''
ERRORTYPEOP: int = 701
ERRORUNDECL: int = 702
ERRORDOUBLDECL: int = 703
ERRORUNKNOWNS: int = 799


''' Productions

    Productions R of the context-free grammar of the language
    Missing key values correspond to empty derivations

    R: V -> (V U Σ)*

    Note:
        Semantic actions are inserted in the productions
        to avoid having to traverse the syntax diagrams twice
'''
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
        SemanticAction(_BOTTOM_F),
        Symbol(VARIABLES),
        Token(RESERVED, 'as'),
        Symbol(TYPE),
        SemanticAction(_TYPE),
        SemanticAction(_BOTTOM_F_D),
        Token(SEMICOLON, ';'),
        Symbol(DECL_VARIABLES),
    ],
    5: [
        Token(IDENTIFIER),
        SemanticAction(_ID),
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
        SemanticAction(_FACTOR_ID),
        Token(EQUAL_SIGN, '='),
        SemanticAction(_OPERATOR),
        Symbol(EXPRESSION_0),
        SemanticAction(_ASSIGNMENT),
    ],
    23: [
        Symbol(EXPRESSION_1),
        Symbol(DISJUNCTION),
    ],
    24: [
        Token(OR, '||'),
        SemanticAction(_OPERATOR),
        Symbol(EXPRESSION_0),
        SemanticAction(_OR),
    ],
    26: [
        Symbol(EXPRESSION_2),
        Symbol(CONJUNCTION),
    ],
    27: [
        Token(AND, '&&'),
        SemanticAction(_OPERATOR),
        Symbol(EXPRESSION_1),
        SemanticAction(_AND),
    ],
    29: [
        Symbol(NEGATION),
        Symbol(EXPRESSION_3),
        SemanticAction(_NOT),
    ],
    30: [
        Token(NOT, '!'),
        SemanticAction(_OPERATOR),
    ],
    32: [
        Symbol(EXPRESSION_4),
        Symbol(COMPARISON),
    ],
    33: [
        Symbol(RELATIONAL_OPERATOR),
        SemanticAction(_OPERATOR),
        Symbol(EXPRESSION_4),
        SemanticAction(_RELATIONAL),
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
        SemanticAction(_OPERATOR),
        Symbol(EXPRESSION_4),
        SemanticAction(_ADDITION),
    ],
    43: [
        Token(MINUS_SIGN, '-'),
        SemanticAction(_OPERATOR),
        Symbol(EXPRESSION_4),
        SemanticAction(_ADDITION),
    ],
    45: [
        Symbol(FACTOR),
        Symbol(MULTIPLICATION),
    ],
    46: [
        Token(TIMES_SIGN, '*'),
        SemanticAction(_OPERATOR),
        Symbol(ADDEND),
        SemanticAction(_MULTIPLICATION),
    ],
    47: [
        Token(OVER_SIGN, '/'),
        SemanticAction(_OPERATOR),
        Symbol(ADDEND),
        SemanticAction(_MULTIPLICATION),
    ],
    48: [
        Token(MODULO, '%'),
        SemanticAction(_OPERATOR),
        Symbol(ADDEND),
        SemanticAction(_MULTIPLICATION),
    ],
    50: [
        Token(IDENTIFIER),
        SemanticAction(_FACTOR_ID),
    ],
    51: [
        Token(INTEGER),
        SemanticAction(_FACTOR_INT),
    ],
    52: [
        Token(FLOAT),
        SemanticAction(_FACTOR_REAL),
    ],
    53: [
        Token(FLOATSCI),
        SemanticAction(_FACTOR_REAL),
    ],
    54: [
        Token(CHARACTER),
        SemanticAction(_FACTOR_CHAR),
    ],
    55: [
        Token(STRING),
        SemanticAction(_FACTOR_STR),
    ],
    56: [
        Token(PARENTHESISOPEN, '('),
        SemanticAction(_BOTTOM),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
        SemanticAction(_BOTTOM_D),
    ],
    57: [
        Token(RESERVED, 'if'),
        SemanticAction(_BOTTOM),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
        SemanticAction(_GO_TO_FALSE),
        Symbol(STATEMENTS),
        Symbol(ELSE),
        SemanticAction(_BOTTOM_D),
        Token(RESERVED, 'endif'),
        SemanticAction(_FILL_JUMP),
    ],
    58: [
        SemanticAction(_FILL_JUMP_1),
        Token(RESERVED, 'else'),
        SemanticAction(_GO_TO),
        Symbol(STATEMENTS),
    ],
    60: [
        Token(RESERVED, 'while'),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSION_0),
        Token(PARENTHESISCLOSE, ')'),
        SemanticAction(_GO_TO_FALSE),
        Symbol(STATEMENTS),
        Token(RESERVED, 'endwhile'),
        SemanticAction(_GO_TO_BACK),
        SemanticAction(_FILL_JUMP),
    ],
    61: [
        Token(RESERVED, 'for'),
        Token(PARENTHESISOPEN, '('),
        Symbol(ASSIGNMENT),
        SemanticAction(_FOR_COMPARISON),
        Token(COLON, ':'),
        Symbol(EXPRESSION_0),
        SemanticAction(_RELATIONAL),
        Token(PARENTHESISCLOSE, ')'),
        SemanticAction(_GO_TO_TRUE),
        Symbol(STATEMENTS),
        SemanticAction(_INCREMENT),
        Token(RESERVED, 'endfor'),
        SemanticAction(_GO_TO_BACK),
        SemanticAction(_FILL_JUMP),
    ],
    62: [
        Symbol(EXPRESSION_0),
        SemanticAction(_READWRITE),
        Symbol(MORE_EXPRESSIONS),
    ],
    63: [
        Token(COMMA, ','),
        Symbol(EXPRESSIONS),
    ],
    65: [
        Token(RESERVED, 'read'),
        SemanticAction(_OPERATOR),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSIONS),
        Token(PARENTHESISCLOSE, ')'),
        SemanticAction(_READWRITE_O),
    ],
    66: [
        Token(RESERVED, 'write'),
        SemanticAction(_OPERATOR),
        Token(PARENTHESISOPEN, '('),
        Symbol(EXPRESSIONS),
        Token(PARENTHESISCLOSE, ')'),
        SemanticAction(_READWRITE_O),
    ],
    67: [
        Token(RESERVED, 'enter'),
        SemanticAction(_ENTER),
    ],
}


''' Operators whose quadruple are of the form:
        [operator, None, None, op]
'''
special_operators = {
    'write': Type.write,
    'read': Type.read,
}


''' Operators whose quadruple are of the form:
    [operator, None, None, result]
'''
nullary_operators = {
    'JI': Type.JI,
    'enter': Type.enter,
}


''' Operators whose quadruple are of the form:
        [operator, op1, None, result]
'''
unary_operators = {
    r'!': lambda x: not x,
    'JF': Type.JF,
    'JT': Type.JT,
}


''' Operators whose quadruple are of the form:
    [operator, op1, op2, result]
'''
binary_operators = {
    r'+': lambda x, y: x + y,
    r'-': lambda x, y: x - y,
    r'*': lambda x, y: x * y,
    r'/': lambda x, y: x / y,
    r'%': lambda x, y: x % y,
    r'||': lambda x, y: x or y,
    r'&&': lambda x, y: x and y,
    r'<': lambda x, y: x < y,
    r'<=': lambda x, y: x <= y,
    r'>': lambda x, y: x > y,
    r'>=': lambda x, y: x >= y,
    r'==': lambda x, y: x == y,
    r'!=': lambda x, y: x != y,
}
