import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QFileDialog, QListWidget, QListWidgetItem)
from PyQt5.QtCore import (QTimer, QEventLoop)
import os
from lilyac import Lexer, Parser, Intermediate, Token, Error
import time


class compiler(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setLayout(QHBoxLayout())
        self.layout().addLayout(self.head())
        self.layout().addLayout(self.code())
        self.layout().addLayout(self.quadruples())
        self.layout().addLayout(self.optimized_quadruples())

        self.stylesheet= """
        QDialog{
            background-color: #D1EECC
        }

        QPushButton#open_file{
            background-color: #57A99A
        }

        QPushButton#edit_txt{
            background-color: #57A99A
        }

        QPushButton#save_file{
            background-color: #57A99A
        }

        QPushButton#analyze_code{
            background-color: #57A99A
        }

        QPushButton#Execute{
            background-color: #57A99A
        }

        QLabel#lb_code{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_quadruples{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_out{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_opquad{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_opout{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }
        """

        self.setGeometry(0, 30, 1500, 700)
        print(self.height())
        print(self.width())
        self.setWindowTitle('lilyac')
        self.setStyleSheet(self.stylesheet)
        self.show()

    def head(self):
        btn_open_file = QPushButton('Open file', self)
        btn_open_file.setObjectName('open_file')
        btn_open_file.clicked.connect(self.go_to_open)

        btn_edit_text = QPushButton('Edit text', self)
        btn_edit_text.setObjectName('edit_txt')
        btn_edit_text.clicked.connect(self.go_to_edit)

        btn_save_changes = QPushButton('Save', self)
        btn_save_changes.setObjectName('save_file')
        btn_save_changes.clicked.connect(self.go_to_save)

        btn_analyze_code = QPushButton('Analyze', self)
        btn_analyze_code.setObjectName('analyze_code')
        btn_analyze_code.clicked.connect(self.go_to_analyze)

        btn_execute = QPushButton('Execute', self)
        btn_execute.setObjectName('Execute')
        btn_execute.clicked.connect(self.go_to_execute)

        head_layout = QVBoxLayout()
        head_layout.addWidget(btn_open_file)
        head_layout.addWidget(btn_edit_text)
        head_layout.addWidget(btn_save_changes)
        head_layout.addWidget(btn_analyze_code)
        head_layout.addWidget(btn_execute)

        return head_layout

    def code(self):
        lb_code = QLabel("Code")
        lb_code.setObjectName('lb_code')
        self.txt_code = QPlainTextEdit()
        self.txt_code.textChanged.connect(self.on_text_changed)

        code_layout = QVBoxLayout()
        code_layout.addWidget(lb_code)
        code_layout.addWidget(self.txt_code)

        return code_layout

    def on_text_changed(self):
        self.data = self.txt_code.toPlainText() + ' '

    def quadruples(self):
        lb_quadruples = QLabel("Quadruples")
        lb_quadruples.setObjectName('lb_quadruples')
        self.list_quad = QListWidget()

        lb_out = QLabel("Output")
        lb_out.setObjectName('lb_out')
        self.txt_output = QPlainTextEdit()
        self.txt_output.setReadOnly(True)

        quad_layout = QVBoxLayout()
        quad_layout.addWidget(lb_quadruples)
        quad_layout.addWidget(self.list_quad)
        quad_layout.addWidget(lb_out)
        quad_layout.addWidget(self.txt_output)

        return quad_layout

    def optimized_quadruples(self):
        lb_opquadruples = QLabel("Optimized quadruples")
        lb_opquadruples.setObjectName('lb_opquad')
        self.list_opquad = QListWidget()

        lb_opout = QLabel("Optimized output")
        lb_opout.setObjectName('lb_opout')
        self.txt_opout = QPlainTextEdit()
        self.txt_opout.setReadOnly(True)

        opquad_layout = QVBoxLayout()
        opquad_layout.addWidget(lb_opquadruples)
        opquad_layout.addWidget(self.list_opquad)
        opquad_layout.addWidget(lb_opout)
        opquad_layout.addWidget(self.txt_opout)

        return opquad_layout

    def go_to_open(self):
        self.txt_code.setReadOnly(True)
        filename = QFileDialog.getOpenFileName(self, "Open file", "/Documents")
        # filename = QFileDialog.getOpenFileName(self, "Open file", "~/Documents")
        if filename[0]:
            f = open(filename[0], "r", encoding="utf8")
            with f:
                self.data = f.read() + ''
                self.txt_code.appendPlainText(self.data)

    def go_to_edit(self):
        self.txt_code.setReadOnly(False)

    def go_to_save(self):
        filename = QFileDialog.getSaveFileName(self, "Save file", "/Documents")
        # filename = QFileDialog.getSaveFileName(self, "Save file", "~/Documents")
        if filename[0]:
            f = open(filename[0], "w", encoding="utf8")
            with f:
                saving_txt = self.txt_code.toPlainText()
                data = f.write(saving_txt)
                f.close()

    def update_strings(self):
        def stringify_quadruple(quadruple, i):
            operator, op1, op2, result = quadruple
            op1 = op1.lexeme if op1 else ''
            op2 = op2.lexeme if op2 else ''
            if result:
                if isinstance(result, Token):
                    result = result.lexeme
            else:
                result = ''
            line = f'{i}: {operator}\t{op1}\t{op2}\t{result}\n'
            return line

        self.quadruples_str = [stringify_quadruple(quadruple, i) for i, quadruple in enumerate(self.intermediate.quadruples)]
        self.types = [f'{symbol}:{self.intermediate.symbols_table[symbol]}' for symbol in self.intermediate.symbols_table]

    def view_types_quadruples(self):
        self.list_quad.clear()
        self.list_quad.addItems(self.quadruples_str)

    def go_to_analyze(self):
        lexer = Lexer()
        self.parser = Parser()
        self.intermediate = Intermediate()
        i = 0
        while i < len(self.data) and len(self.parser.symbols) > 0:
            if self.parser.is_semantic_action():
                action = self.parser.symbols.pop()
                result = self.intermediate.step(action)
                self.update_strings()
                self.view_types_quadruples()
                if isinstance(result, Error):
                    self.txt_error.appendPlainText(str(result))
                    print(result)
                    return
            else:
                token, i = lexer.generate_token(i, self.data)
                if isinstance(token, Error):
                    error = True
                    print(token)
                    return
                while True:
                    new_token = self.parser.step(token)
                    production_pile_str = [str(token) for token in self.parser.symbols]
                    if isinstance(new_token, Error):
                        error = True
                        print(new_token)
                        return
                    elif isinstance(new_token, Token):
                        break
                    result = self.intermediate.step(new_token)
                    self.update_strings()
                    self.view_types_quadruples()
                    if isinstance(result, Error):
                        error = True
                        print(result)
                        return
                result = self.intermediate.step(token)
                self.update_strings()
                self.view_types_quadruples()
                if isinstance(result, Error):
                    error = True
                    print(result)
                    return

    def go_to_execute(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = compiler()
    sys.exit(app.exec())
