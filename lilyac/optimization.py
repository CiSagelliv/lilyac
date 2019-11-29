import lilyac
from lilyac import Token

from typing import List, Dict


jumps = [
    'JF',
    'JT',
    'JI',
]


constants = [
    lilyac.INTEGER,
    lilyac.FLOAT,
    lilyac.FLOATSCI,
    lilyac.CHARACTER,
    lilyac.STRING,
]


def optimize_jumps(quadruples: List):
    for q in quadruples[::-1]:
        if q[0] in jumps:
            i = q[3].lexeme
            if i == len(quadruples):
                continue
            elif quadruples[i][0] == 'JI':
                # Replace chains of inconditional jumps
                q[3] = quadruples[i][3]
    return quadruples


def optimize_temporals(quadruples: List):
    i = 0
    while(i < len(quadruples)):
        q = quadruples[i]
        if q[0] == '=' and is_temporal(q[3]):
            # Assignment of temporal variable
            i = remove_temporal_assignment(quadruples, i)
        elif (q[1] and q[2]) and (is_temporal(q[1]) or is_temporal(q[2])):
            # Use of temporal variable
            i = remove_temporal_use(quadruples, i)
        i += 1
    return quadruples


def remove_temporal_assignment(quadruples: List, i: int):
    ''' If possible, will replace the assignment of a temporal variable
        with its value in the `i`_th element of `quadruples`

        May remove other temporal variables

        Returns the new index of the previously `i`_th quadruple
        as the removal of quadruples may change its position
    '''

    assert i >= 0
    q = quadruples[i]
    assert is_temporal(q[3])

    j = search_temporal(quadruples, q[3])
    k = remove_temporal_use(quadruples, j)

    # Update indices in case of quadruple removal
    i -= j - k
    j = k

    # i: index of temporal variable use
    # j: index of temporal variable creation
    q_j = quadruples[j]

    if is_constant(q_j[1]) and is_constant(q_j[2]):
        q[3] = evaluate_quadruple(q_j)
        del quadruples[j]
        i -= 1

    return i


def remove_temporal_use(quadruples: List, i: int):
    ''' If possible, will recursively replace the use of temporal variables
        with their values in the `i`_th element of `quadruples`

        Returns the new index of the previously `i`_th quadruple
        as the removal of quadruples may change its position
    '''

    assert i >= 0

    q = quadruples[i]
    # i: index of temporal variable use
    # j: index of temporal variable creation
    ''' First factor '''
    if is_temporal(q[1]):
        # Find the index of the quadruple
        # where the temporal variable is created
        k = search_temporal(quadruples, q[1])
        # If this quadruple uses temporal variables; remove them
        j = remove_temporal_use(quadruples, k)
        # Update indices accordingly
        i -= k - j
        k = j
        # Get the quadruple
        q_k = quadruples[k]
        if can_evaluate(q_k):
            q[1] = evaluate_quadruple(q_k)
            i -= 1

    ''' Second factor '''
    if is_temporal(q[2]):
        # Same as before
        k = search_temporal(quadruples, q[2])
        j = remove_temporal_use(quadruples, k)
        i -= k - j
        k = j
        q_k = quadruples[k]
        if can_evaluate(q_k):
            q[2] = evaluate_quadruple(q_k)
            del quadruples[k]
            i -= 1

    # Return index for updating in case of quadruple removal
    return i


def evaluate_quadruple(q):
    ''' Evaluate the result of a quadruple with a simple operation
        returning a token
    '''
    op = q[0]
    if op in lilyac.unary_operators:
        assert is_constant(q[1])
        operator = lilyac.unary_operators[op]
        op1 = get_value(q[1])
        result = operator(op1)
    elif op in lilyac.binary_operators:
        assert is_constant(q[1]) and is_constant(q[2])
        operator = lilyac.binary_operators[op]
        op1 = get_value(q[1])
        op2 = get_value(q[2])
        result = operator(op1, op2)
    else:
        raise Exception('Error in operation: ', q)

    res_type = type(result)
    if res_type == int:
        return Token(lilyac.INTEGER, str(result))
    elif res_type == float and 'e' in str(result):
        return Token(lilyac.FLOATSCI, str(result))
    elif res_type == float:
        return Token(lilyac.FLOAT, str(result))
    elif res_type == str and len(str(result)):
        return Token(lilyac.CHARACTER, result)
    elif res_type == str:
        return Token(lilyac.STRING, result)


def search_temporal(quadruples, temporal):
    ''' Returns the index of the quadruple where a temporal is created
    '''
    for k, q in enumerate(quadruples):
        if (q[3] and type(q[3]) != int
           and q[3].lexeme == temporal.lexeme and q[0] != '='):
            return k


def is_temporal(factor):
    return '.R' in factor.lexeme


def is_constant(factor):
    return factor.grammeme in constants


def can_evaluate(q):
    return q[1].grammeme in constants and q[2].grammeme in constants


def get_value(token):
    if token.grammeme == lilyac.INTEGER:
        return int(token.lexeme)
    elif (token.grammeme == lilyac.FLOAT
          or token.grammeme == lilyac.FLOATSCI):
        return float(token.lexeme)
    elif token.grammeme == lilyac.CHARACTER:
        return token.lexeme
    elif token.grammeme == lilyac.STRING:
        return token.lexeme
