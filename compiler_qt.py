import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit)
import os

class compiler(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setLayout(QVBoxLayout())
        self.layout().addLayout(self.head())
        #head contains buttons and labels
        self.layout().addLayout(self.code_to_check())
        #code_to_check contains two QPlainTextEdit to add some code
        self.layout().addLayout(self.analyze())

        self.setGeometry(300,0,550,570)
        self.setWindowTitle('Compiler')
        self.show()

    def head(self):
        btn_open_file = QPushButton("Open file", self)
        btn_open_file.clicked.connect(self.go_to_open)

        btn_edit_code = QPushButton("Edit text", self)
        btn_edit_code.clicked.connect(self.go_to_edit)

        btn_save_changes = QPushButton("Save", self)
        btn_save_changes.clicked.connect(self.go_to_save)

        hlay_win = QHBoxLayout()
        hlay_win.addWidget(btn_open_file)
        hlay_win.addWidget(btn_edit_code)
        hlay_win.addWidget(btn_save_changes)

        return hlay_win

    def code_to_check(self):
        lb_code_to_analyze = QLabel("Code")
        code_to_analyze = QPlainTextEdit()
        lb_analyzed = QLabel("Analyzed code")
        analyzed_code = QPlainTextEdit()
        lb_code_error = QLabel("Error")
        code_error = QPlainTextEdit()

        hlay_win2 = QHBoxLayout()
        hlay_win2.addWidget(lb_code_to_analyze)
        hlay_win2.addWidget(code_to_analyze)
        hlay_win2.addWidget(lb_analyzed)
        hlay_win2.addWidget(analyzed_code)
        hlay_win2.addWidget(lb_code_error)
        hlay_win2.addWidget(code_error)

        return hlay_win2

    def analyze(self):
        analyze_code = QPushButton("Analyze code",self)

        hlay_win3 = QHBoxLayout()
        hlay_win3.addWidget(analyze_code)

        return hlay_win3

    def go_to_open(self):
        pass

    def go_to_edit(self):
        pass

    def go_to_save(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = compiler()
    sys.exit(app.exec())
