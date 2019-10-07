from lilyac import Lexer, Parser, Intermediate, compiler, Token, Error
from PyQt5.QtWidgets import QApplication
import sys
import os


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
                result = intermediate.step(action)
                if isinstance(result, Error):
                    error = True
                    print(result)
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
                    result = intermediate.step(new_token)
                    if isinstance(result, Error):
                        error = True
                        print(result)
                result = intermediate.step(token)
                if isinstance(result, Error):
                    error = True
                    print(result)
        if not error:
            print('Succesfully compiled')
            save_code(file, intermediate.quadruples)
    else:
        app = QApplication(sys.argv)
        ex = compiler()
        sys.exit(app.exec())


def __main__():
    main()


def save_code(file, quadruples):
    file = file.replace('/', '_')
    if not os.path.exists('out'):
        os.makedirs('out')
    with open(f'out/{file}.q', 'wb') as f:
        f.write(b'#,OPERATOR,OP1,OP2,RESULT\n')
        for i, quadruple in enumerate(quadruples):
            operator, op1, op2, result = quadruple
            op1 = op1.lexeme if op1 else ''
            op2 = op2.lexeme if op2 else ''
            line = f'{i},{operator},{op1},{op2},{result}\n'
            encoded_line = bytes(line, 'utf-8')
            f.write(encoded_line)
