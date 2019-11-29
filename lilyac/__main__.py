from lilyac import Lexer, Parser, Intermediate, compiler, Token, Error, optimize_jumps, optimize_temporals, Execution
from PyQt5.QtWidgets import QApplication
import sys
import os
import time


def main():
    if len(sys.argv) > 1:
        # If a file is given, compile from CLI
        file = sys.argv[1]
        compile(file)
    else:
        # Open graphical interface
        app = QApplication(sys.argv)
        ex = compiler()
        sys.exit(app.exec())


def __main__():
    main()


def compile(file):
    # Read code
    code: str = ''
    with open(file) as f:
        code = f.read() + ' '
    # Initialize modules
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
                    # Syntax Error
                    error = True
                    print(new_token)
                    return
                elif isinstance(new_token, Token):
                    break
                # Semantic action
                result = intermediate.step(new_token)
                if isinstance(result, Error):
                    # Semantic error
                    error = True
                    print(result)
                    return
            result = intermediate.step(token)
            if isinstance(result, Error):
                error = True
                print(result)
                return
    print('Succesfully compiled')
    print('Optimizing jumps')
    quadruples = optimize_jumps(intermediate.quadruples)
    print('Optimizing temporals')
    quadruples = optimize_temporals(quadruples)
    print('Succesfully optimized')
    save_code(file, quadruples)

    start_time = time.time()
    execution_env = Execution(intermediate.quadruples, intermediate.symbols_table)
    execution_env.execute()
    print('Tiempo ejecución: ', time.time() - start_time)

    start_time = time.time()
    execution_env = Execution(quadruples, intermediate.symbols_table)
    execution_env.execute()
    print('Tiempo ejecución: ', time.time() - start_time)
    print(execution_env.output)


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
