import lilyac

jumps = [
    'JF',
    'JT',
    'JI',
]

def optimize_jumps(quadruples):
    for q in quadruples[::-1]:
        if q[0] in jumps:
            i = q[3]
            if quadruples[i][0] == 'JI':
                q[3] = quadruples[i][3]
    return quadruples
