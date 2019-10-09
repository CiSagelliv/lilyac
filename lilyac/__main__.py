from lilyac import Lexer, Parser, Intermediate, compiler, Token, Error
from PyQt5.QtWidgets import QApplication
import sys
import os


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        compile(file)
    else:
        app = QApplication(sys.argv)
        ex = compiler()
        sys.exit(app.exec())


def __main__():
    main()


def compile(file):
    code: str = ''
    with open(file) as f:
        code = f.read() + ' '
    lexer = Lexer()
    parser = Parser()
    intermediate = Intermediate()
    i = 0
    while i < len(code) and len(parser.symbols) > 0:
        if parser.is_semantic_action():
            action = parser.symbols.pop()
            result = intermediate.step(action)
            if isinstance(result, Error):
                print(result)
                return
        else:
            token, i = lexer.generate_token(i, code)
            if isinstance(token, Error):
                error = True
                print(token)
                return
            while True:
                new_token = parser.step(token)
                if isinstance(new_token, Error):
                    error = True
                    print(new_token)
                    return
                elif isinstance(new_token, Token):
                    break
                result = intermediate.step(new_token)
                if isinstance(result, Error):
                    error = True
                    print(result)
                    return
            result = intermediate.step(token)
            if isinstance(result, Error):
                error = True
                print(result)
                return
    print('Succesfully compiled')
    save_code(file, intermediate.quadruples)


def save_code(file, quadruples):
    file = file.replace('/', '_')
    if not os.path.exists('out'):
        os.makedirs('out')
    with open(f'out/{file}.q', 'wb') as f:
        header = '#,OPERATOR,OP1,OP2,RESULT\n'
        encoded_header = bytes(header, 'utf-8')
        f.write(encoded_header)
        for i, quadruple in enumerate(quadruples):
            operator, op1, op2, result = quadruple
            op1 = op1.lexeme if op1 else ''
            op2 = op2.lexeme if op2 else ''
            if result:
                if isinstance(result, Token):
                    result = result.lexeme
            else:
                result = ''
            line = f'{i},{operator},{op1},{op2},{result}\n'
            encoded_line = bytes(line, 'utf-8')
            f.write(encoded_line)
