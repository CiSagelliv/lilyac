import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QFileDialog)
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
        """

        self.setGeometry(0, 30, 1500, 700)
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

        head_layout = QVBoxLayout()
        head_layout.addWidget(btn_open_file)
        head_layout.addWidget(btn_edit_text)
        head_layout.addWidget(btn_save_changes)
        head_layout.addWidget(btn_analyze_code)

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
        txt_quad = QPlainTextEdit()

        lb_error = QLabel("Error")
        lb_error.setObjectName('lb_error')
        txt_error = QPlainTextEdit()

        quad_layout = QVBoxLayout()
        quad_layout.addWidget(lb_quadruples)
        quad_layout.addWidget(txt_quad)
        quad_layout.addWidget(lb_error)
        quad_layout.addWidget(txt_error)

        return quad_layout

    def factor_pile(self):
        lb_factor = QLabel("factor_pile")
        lb_factor.setObjectName('lb_factor')
        txt_factor = QPlainTextEdit()

        lb_operator = QLabel("operator_pile")
        lb_operator.setObjectName('lb_operator')
        txt_operator = QPlainTextEdit()

        factor_layout = QVBoxLayout()
        factor_layout.addWidget(lb_factor)
        factor_layout.addWidget(txt_factor)
        factor_layout.addWidget(lb_operator)
        factor_layout.addWidget(txt_operator)

        return factor_layout

    def production_pile(self):
        lb_production = QLabel("production_pile")
        lb_production.setObjectName('production_pile')
        txt_production = QPlainTextEdit()

        lb_jump = QLabel("jump_pile")
        lb_jump.setObjectName('jump_pile')
        txt_jump = QPlainTextEdit()

        production_layout = QVBoxLayout()
        production_layout.addWidget(lb_production)
        production_layout.addWidget(txt_production)
        production_layout.addWidget(lb_jump)
        production_layout.addWidget(txt_jump)

        return production_layout

    def go_to_open(self):
        self.txt_code.setReadOnly(True)
        filename = QFileDialog.getOpenFileName(self, "Open file", "/Documents")
        # filename = QFileDialog.getOpenFileName(self, "Open file", "~/Documents")
        if filename[0]:
            f = open(filename[0], "r", encoding="utf8")
            with f:
                data = f.read()
                self.txt_code.appendPlainText(data)

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

    def go_to_analyze(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = compiler()
    sys.exit(app.exec())
