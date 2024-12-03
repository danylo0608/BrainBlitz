from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys 

from design import design_widgets as DW
from game import Game

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.centr_w = QWidget()
        self.setCentralWidget(self.centr_w)
        self.centr_w.setStyleSheet(DW.Fon.fon_color)
        self.setWindowTitle("Brain Blitz")
        self.resize(1500, 800)
        
        self.btn_logo = QPushButton("", self)
        self.btn_logo.setMinimumSize(500, 500)
        self.btn_logo.setStyleSheet("""
            QPushButton {
                border: none;
                background-image: url('design/image/logoNotBC.png');
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        self.btn_play = QPushButton("Грати", self)
        self.btn_play.setFont(QFont("Arial", 25))
        self.btn_play.setMaximumHeight(80)
        self.btn_play.setMaximumWidth(500)
        self.btn_play.setStyleSheet(DW.Btn.btn_design)
        self.btn_play.clicked.connect(self.def_btn_play)

        # self.btn_setting = QPushButton("Налаштування", self)
        # self.btn_setting.setFont(QFont("Arial", 25))
        # self.btn_setting.setMaximumHeight(80)
        # self.btn_setting.setMaximumWidth(500)
        # self.btn_setting.setStyleSheet(DW.Btn.btn_design)
        # self.btn_setting.clicked.connect(self.def_btn_setting)

        self.g = QGridLayout(self.centr_w)
        self.g.addWidget(self.btn_logo, 0, 1)
        self.g.addWidget(self.btn_play, 1, 1)
        # self.g.addWidget(self.btn_setting, 2, 1)

    def def_btn_play(self):
        self.hide()  

        self.game_window = Game.PlayWindow(self.size().height(), self.size().width())
        self.game_window.show()

    # def def_btn_setting(self):
    #     # w = SettingWindow()
    #     # w.exec_()
    #     pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("design/image/logo.png"))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
