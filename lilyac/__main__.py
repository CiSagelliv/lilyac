from lilyac import Lexer, Parser, Intermediate, compiler
from PyQt5.QtWidgets import QApplication
import sys


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        code: str = ''
        with open(file) as f:
            code = f.read()

        lexer = Lexer()
        parser = Parser()
        intermediate = Intermediate()
    else:
        app = QApplication(sys.argv)
        ex = compiler()
        sys.exit(app.exec())


def __main__():
    main()
