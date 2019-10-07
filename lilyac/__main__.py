from lilyac import Lexer, Parser, Intermediate, compiler, Token, Error
from PyQt5.QtWidgets import QApplication
import sys


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        code: str = ''
        with open(file) as f:
            code = f.read() + ' '
        lexer = Lexer()
        parser = Parser()
        intermediate = Intermediate()
        i = 0
        error = False
        while i < len(code) and len(parser.symbols) > 0:
            if parser.is_semantic_action():
                action = parser.symbols.pop()
                intermediate.step(action)
            else:
                token, i = lexer.generate_token(i, code)
                if isinstance(token, Error):
                    error = True
                    print(token)
                    break
                while True:
                    new_token = parser.step(token)
                    if isinstance(new_token, Error):
                        error = True
                        print(new_token)
                        break
                    elif isinstance(new_token, Token):
                        break
                    intermediate.step(new_token)
                intermediate.step(token)
        if not error:
            print('Succesfully compiled')
            with open('out.o', 'w') as f:
                f.write('#\tOPERATOR\tOP1\tOP2\tRESULT\n')
                for i, quadruple in enumerate(intermediate.quadruples):
                    operator, op1, op2, result = quadruple
                    line = f'{i}\t{operator}\t{op1}\t{op2}\t{result}\n'
                    print(line)
                    f.write(line)
    else:
        app = QApplication(sys.argv)
        ex = compiler()
        sys.exit(app.exec())


def __main__():
    main()
