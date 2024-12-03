from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from design import design_widgets as DW
from . import Question_

cols = 7
rows = 4

class PlayWindow(QMainWindow):
    def __init__(self, height, width):
        super(PlayWindow, self).__init__()

        self.centr_w = QWidget()
        self.setCentralWidget(self.centr_w)
        self.setWindowTitle("Brain Blitz")
        self.resize(width, height)
        self.setStyleSheet(DW.Fon.fon_color)

        self.g = QGridLayout(self.centr_w)
       
        self.label_score = 100
        for i in range(cols):
            self.label = QLabel(self)
            self.label.setText(f"{self.label_score}")
            self.label.setFont(QFont("Arial", 25))
            self.label.setStyleSheet(f"color: {DW.Color.label}")
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setMaximumHeight(100)

            self.label_score += 100

            self.g.addWidget(self.label, 0, i)
        
        self.score = 0
        for i in range(rows):
            for j in range(cols):
                self.score += 1
                self.btn = QPushButton(self)
                self.btn.setText(f"{self.score}")
                self.btn.setFont(QFont("Arial", 15))
                self.btn.setMaximumHeight(80)
                self.btn.setStyleSheet(DW.Btn.btn_design)
                self.btn.clicked.connect(self.def_btn)
                self.g.addWidget(self.btn, i+1, j)
        
    def def_btn(self):
        sender = self.sender()
        sender.hide()
        w = Question_.QuestionWindow()
        w.exec_()
