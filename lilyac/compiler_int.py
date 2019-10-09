import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QFileDialog, QListWidget, QListWidgetItem)
import os
from lilyac import Lexer, Parser, Intermediate, compiler, Token, Error
from time import sleep


class compiler(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setLayout(QHBoxLayout())
        self.layout().addLayout(self.head())
        self.layout().addLayout(self.code())
        self.layout().addLayout(self.quadruples())
        self.layout().addLayout(self.factor_pile())
        self.layout().addLayout(self.production_pile())

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

        QPushButton#despacito{
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

        QLabel#lb_error{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_factor{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_operator{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#production_pile{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#jump_pile{
            font-family: "Times New Roman", Times, serif;
            font-size: 20px;
            color: green;
        }

        QLabel#lb_type{
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

        btn_analyze_despacito = QPushButton('Analyze despacito', self)
        btn_analyze_despacito.setObjectName('despacito')
        btn_analyze_despacito.clicked.connect(self.go_to_despacito)

        head_layout = QVBoxLayout()
        head_layout.addWidget(btn_open_file)
        head_layout.addWidget(btn_edit_text)
        head_layout.addWidget(btn_save_changes)
        head_layout.addWidget(btn_analyze_code)
        head_layout.addWidget(btn_analyze_despacito)

        return head_layout

    def code(self):
        lb_code = QLabel("Code")
        lb_code.setObjectName('lb_code')
        self.txt_code = QPlainTextEdit()

        code_layout = QVBoxLayout()
        code_layout.addWidget(lb_code)
        code_layout.addWidget(self.txt_code)

        return code_layout

    def quadruples(self):
        lb_quadruples = QLabel("Quadruples")
        lb_quadruples.setObjectName('lb_quadruples')
        #self.txt_quad = QPlainTextEdit()
        self.list_quad = QListWidget()


        lb_type = QLabel("Symbol")
        lb_type.setObjectName('lb_type')
        self.list_type = QListWidget()

        lb_error = QLabel("Error")
        lb_error.setObjectName('lb_error')
        self.txt_error = QPlainTextEdit()
        self.txt_error.setReadOnly(True)

        quad_layout = QVBoxLayout()
        quad_layout.addWidget(lb_quadruples)
        quad_layout.addWidget(self.list_quad)
        quad_layout.addWidget(lb_type)
        quad_layout.addWidget(self.list_type)
        quad_layout.addWidget(lb_error)
        quad_layout.addWidget(self.txt_error)

        return quad_layout

    def factor_pile(self):
        lb_factor = QLabel("factor_pile")
        lb_factor.setObjectName('lb_factor')
        self.list_factor = QListWidget()

        lb_operator = QLabel("operator_pile")
        lb_operator.setObjectName('lb_operator')
        self.list_operator = QListWidget()

        factor_layout = QVBoxLayout()
        factor_layout.addWidget(lb_factor)
        factor_layout.addWidget(self.list_factor)
        factor_layout.addWidget(lb_operator)
        factor_layout.addWidget(self.list_operator)

        return factor_layout

    def production_pile(self):
        lb_production = QLabel("production_pile")
        lb_production.setObjectName('production_pile')
        self.list_production = QListWidget()

        lb_jump = QLabel("jump_pile")
        lb_jump.setObjectName('jump_pile')
        self.list_jump = QListWidget()

        production_layout = QVBoxLayout()
        production_layout.addWidget(lb_production)
        production_layout.addWidget(self.list_production)
        production_layout.addWidget(lb_jump)
        production_layout.addWidget(self.list_jump)

        return production_layout

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
         self.factor_pile_str =[str(factor) for factor in self.intermediate.factor_pile]
         self.production_pile_str =[str(token) for token in self.parser.symbols]
         self.operator_pile_str =[str(token) for token in self.intermediate.operator_pile]
         self.quadruples_str =[str(quadruples) for quadruples in self.intermediate.quadruples]
         self.jump_pile_str =[str(jump) for jump in self.intermediate.jump_pile]
         self.types =[ f'{symbol}:{self.intermediate.symbols_table[symbol]}' for symbol in self.intermediate.symbols_table]

    def view_types_quadruples(self):
        self.list_type.clear()
        self.list_type.addItems(self.types)
        self.list_quad.clear()
        self.list_quad.addItems(self.quadruples_str)


    def view_piles(self):
         self.list_factor.clear()
         self.list_factor.addItems(self.factor_pile_str)
         self.list_operator.clear()
         self.list_operator.addItems(self.operator_pile_str)
         self.list_jump.clear()
         self.list_jump.addItems(self.jump_pile_str)

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
                self.view_piles()
                if isinstance(result, Error):
                    self.txt_error.appendPlainText(str(result))
                    print(result)
                    return
            else:
                token, i = lexer.generate_token(i, self.data)
                if isinstance(token, Error):
                    error = True
                    self.txt_error.appendPlainText(token)
                    self.txt_error.appendPlainText(str(token))
                    print(token)
                    return
                while True:
                    new_token = self.parser.step(token)
                    production_pile_str = [str(token) for token in self.parser.symbols]
                    self.list_production.clear()
                    self.list_production.addItems(production_pile_str)
                    if isinstance(new_token, Error):
                        error = True
                        self.txt_error.appendPlainText(str(new_token))
                        print(new_token)
                        return
                    elif isinstance(new_token, Token):
                        break
                    result = self.intermediate.step(new_token)
                    self.update_strings()
                    self.view_types_quadruples()
                    self.view_piles()
                    if isinstance(result, Error):
                        error = True
                        self.txt_error.appendPlainText(str(result))
                        print(result)
                        return
                result = self.intermediate.step(token)
                self.update_strings()
                self.view_types_quadruples()
                self.view_piles()
                if isinstance(result, Error):
                    error = True
                    self.txt_error.appendPlainText(str(result))
                    print(result)
                    return

    def go_to_despacito(self):
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
                self.view_piles()
                if isinstance(result, Error):
                    self.txt_error.appendPlainText(str(result))
                    print(result)
                    return
            else:
                token, i = lexer.generate_token(i, self.data)
                if isinstance(token, Error):
                    error = True
                    self.txt_error.appendPlainText(token)
                    self.txt_error.appendPlainText(str(token))
                    print(token)
                    return
                while True:
                    new_token = self.parser.step(token)
                    production_pile_str = [str(token) for token in self.parser.symbols]
                    self.list_production.clear()
                    self.list_production.addItems(production_pile_str)
                    if isinstance(new_token, Error):
                        error = True
                        self.txt_error.appendPlainText(str(new_token))
                        print(new_token)
                        return
                    elif isinstance(new_token, Token):
                        break
                    result = self.intermediate.step(new_token)
                    self.update_strings()
                    self.view_types_quadruples()
                    self.view_piles()
                    if isinstance(result, Error):
                        error = True
                        self.txt_error.appendPlainText(str(result))
                        print(result)
                        return
                result = self.intermediate.step(token)
                self.update_strings()
                self.view_types_quadruples()
                self.view_piles()
                if isinstance(result, Error):
                    error = True
                    self.txt_error.appendPlainText(str(result))
                    print(result)
                    return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = compiler()
    sys.exit(app.exec())
