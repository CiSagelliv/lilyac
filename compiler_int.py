import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QPlainTextEdit)
import os

class compiler(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setLayout(QHBoxLayout())
        self.layout().addLayout(self.head())
        self.layout().addLayout(self.code())
        self.layout().addLayout(self.quadruples())
        self.layout().addLayout(self.error())
        self.layout().addLayout(self.factor_pile())
        self.layout().addLayout(self.operator_pile())
        self.layout().addLayout(self.production_pile())
        self.layout().addLayout(self.jump_pile())

        self.setGeometry(0,30,1500,700)
        self.setWindowTitle('Compiler')
        self.show()

    def head(self):
        btn_open_file = QPushButton('Open file', self)
        btn_open_file.clicked.connect(self.go_to_open)

        btn_edit_text = QPushButton('Edit text', self)
        btn_edit_text.clicked.connect(self.go_to_edit)

        btn_save_changes = QPushButton('Save', self)
        btn_save_changes.clicked.connect(self.go_to_save)

        btn_analyze_code = QPushButton('Analyze', self)
        btn_analyze_code.clicked.connect(self.go_to_analyze)

        head_layout = QHBoxLayout()
        head_layout.addWidget(btn_open_file)
        head_layout.addWidget(btn_edit_text)
        head_layout.addWidget(btn_save_changes)
        head_layout.addWidget(btn_analyze_code)

        return head_layout

    def code(self):
        pass

    def quadruples(self):
        pass

    def error(self):
        pass

    def factor_pile(self):
        pass

    def operator_pile(self):
        pass

    def production_pile(self):
        pass

    def jump_pile(self):
        pass

    def go_to_open(self):
        pass

    def go_to_edit(self):
        pass

    def go_to_save(self):
        pass

    def go_to_analyze(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = compiler()
    sys.exit(app.exec())
