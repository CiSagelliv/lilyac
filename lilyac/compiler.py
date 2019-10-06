from lilyac import Lexer, Parser, Intermediate
# Add logic for compiler


def __main__():
    file = sys.argv[1]
    code: str = ''
    with open(file) as f:
        code = f.read()

    lexer = Lexer()
    parser = Parser()
    intermediate = Intermediate()
