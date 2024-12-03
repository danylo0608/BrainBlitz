from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from design import design_widgets as DW

class DialogWindow(QDialog):
    def __init__(self, message, question_window):
        super(DialogWindow, self).__init__()
        self.question_window = question_window

        layout = QVBoxLayout(self)
        self.setWindowTitle("Результат")
        self.resize(1000, 700)
        self.setStyleSheet(DW.Fon.fon_color)

        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 40))
        self.label.setStyleSheet(f"color: {DW.Color.label}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setText(message)

        self.btn = QPushButton("Закрити", self)
        self.btn.setFont(QFont("Arial", 15))
        self.btn.setMaximumHeight(80)
        self.btn.setStyleSheet(DW.Btn.btn_design)
        self.btn.clicked.connect(self.def_btn)

        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)
    
    def def_btn(self):
        self.question_window.close()
        self.close() 
