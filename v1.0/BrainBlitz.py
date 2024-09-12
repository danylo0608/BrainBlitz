from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import random

class Color():
    black = 'black'
    fon = '#D0605E'
    white = 'white'
    yellow = 'yellow'
    bc_btn = '#98506D'
    bc_btn_hover = 'yellow' # коли наведено на btn
    label = 'white'


def read_settings(filename):
    settings = {}
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split('=')
            settings[key] = int(value)
    return settings

settings = read_settings('settings.txt')
timer = settings['timer']
rows = settings['rows']
cols = settings['cols']

used_questions = set()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.centr_w = QWidget()
        self.setCentralWidget(self.centr_w)
        self.setWindowTitle("Brain Blitz")
        self.resize(1500, 800)
        self.setStyleSheet(f"background-color: {Color.fon}")
        self.g = QGridLayout(self.centr_w)

        self.btn_play = QPushButton("Грати", self)
        self.btn_play.setFont(QFont("Arial", 25))
        self.btn_play.setMaximumHeight(80)
        self.btn_play.setMaximumWidth(500)
        self.btn_play.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """)
        self.btn_play.clicked.connect(self.def_btn_play)

        self.btn_setting = QPushButton("Налаштування", self)
        self.btn_setting.setFont(QFont("Arial", 25))
        self.btn_setting.setMaximumHeight(80)
        self.btn_setting.setMaximumWidth(500)
        self.btn_setting.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """)
        self.btn_setting.clicked.connect(self.def_btn_setting)

        self.g.addWidget(self.btn_play, 1, 1)
        self.g.addWidget(self.btn_setting, 2, 1)

    def def_btn_play(self):
        self.hide()  

        self.game_window = PlayWindow() 
        self.game_window.show()

    def def_btn_setting(self):
        w = SettingWindow()
        w.exec_()

class SettingWindow(QDialog):
    def __init__(self):
        super(SettingWindow, self).__init__()

        layout = QGridLayout(self)
        self.setWindowTitle("Налаштування")
        self.resize(1000, 700)
        self.setStyleSheet(f"background-color: {Color.fon}")

        self.label_timer = QLabel(self)
        self.label_timer.setText("Таймер (в секундах):")
        self.label_timer.setFont(QFont("Arial", 20))
        self.label_timer.setStyleSheet(f"color: {Color.label}")
        self.label_timer.setAlignment(Qt.AlignCenter)
        self.label_timer.setWordWrap(True)

        self.int_timer = QLineEdit(self)
        self.int_timer.setFont(QFont("Arial", 20))
        self.int_timer.setMaximumHeight(60)
        self.int_timer.setMaximumWidth(400)
        self.int_timer.setStyleSheet(f"color: {Color.label}")

        self.label_rows = QLabel(self)
        self.label_rows.setText("Кількість рядків:")
        self.label_rows.setFont(QFont("Arial", 20))
        self.label_rows.setStyleSheet(f"color: {Color.label}")
        self.label_rows.setAlignment(Qt.AlignCenter)
        self.label_rows.setWordWrap(True)

        self.int_rows = QLineEdit(self)
        self.int_rows.setFont(QFont("Arial", 20))
        self.int_rows.setMaximumHeight(60)
        self.int_rows.setMaximumWidth(400)
        self.int_rows.setStyleSheet(f"color: {Color.label}")

        self.label_cols = QLabel(self)
        self.label_cols.setText("Кількість колонок:")
        self.label_cols.setFont(QFont("Arial", 20))
        self.label_cols.setStyleSheet(f"color: {Color.label}")
        self.label_cols.setAlignment(Qt.AlignCenter)
        self.label_cols.setWordWrap(True)

        self.int_cols = QLineEdit(self)
        self.int_cols.setFont(QFont("Arial", 20))
        self.int_cols.setMaximumHeight(60)
        self.int_cols.setMaximumWidth(400)
        self.int_cols.setStyleSheet(f"color: {Color.label}")

        self.btn_save = QPushButton("Зберегти", self)
        self.btn_save.setFont(QFont("Arial", 20))
        self.btn_save.setMaximumHeight(60)
        self.btn_save.setMaximumWidth(400)
        self.btn_save.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """)
        self.btn_save.clicked.connect(self.def_btn_save)

        layout.addWidget(self.label_timer, 1, 1)
        layout.addWidget(self.int_timer, 1, 2)
        layout.addWidget(self.label_rows, 2, 1)
        layout.addWidget(self.int_rows, 2, 2)
        layout.addWidget(self.label_cols, 3, 1)
        layout.addWidget(self.int_cols, 3, 2)
        layout.addWidget(self.btn_save, 4, 1, 1, 2)

    def def_btn_save(self):
        pass


class PlayWindow(QMainWindow):
    def __init__(self):
        super(PlayWindow, self).__init__()

        self.centr_w = QWidget()
        self.setCentralWidget(self.centr_w)
        self.setWindowTitle("Brain Blitz")
        self.resize(1500, 800)
        self.setStyleSheet(f"background-color: {Color.fon}")

        self.g = QGridLayout(self.centr_w)
       
        self.label_score = 100
        for i in range(cols):
            self.label = QLabel(self)
            self.label.setText(f"{self.label_score}")
            self.label.setFont(QFont("Arial", 25))
            self.label.setStyleSheet(f"color: {Color.label}")
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
                self.btn.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """)
                self.btn.clicked.connect(self.def_btn)
                self.g.addWidget(self.btn, i+1, j)
        
    def def_btn(self):
        sender = self.sender()
        sender.hide()
        w = Question()
        w.exec_()


class Question(QDialog):
    def __init__(self):
        super(Question, self).__init__()

        layout = QVBoxLayout(self)
        self.setWindowTitle("Питання")
        self.resize(1200, 700)
        self.setStyleSheet(f"background-color: {Color.fon}")

        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 40))
        self.label.setStyleSheet(f"color: {Color.label}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)

        self.question, self.correct_answer, self.wrong_answers = self.get_unique_question()
        self.label.setText(self.question)

        self.buttons = []
        all_answers = [self.correct_answer] + self.wrong_answers
        random.shuffle(all_answers)  
        
        for answer in all_answers:
            btn = QPushButton(answer, self)
            btn.setFont(QFont("Arial", 15))
            btn.setMaximumHeight(80)
            btn.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """)
            btn.clicked.connect(self.check_answer)
            self.buttons.append(btn)
            layout.addWidget(btn)
        
        # Додавання таймера
        self.label_timer = QLabel(self)
        self.label_timer.setFont(QFont("Arial", 20))
        self.label_timer.setStyleSheet(f"color: {Color.label}")
        self.label_timer.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_timer)

        # Ініціалізація таймера
        self.remaining_time = timer  # кількість секунд, визначена в налаштуваннях
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # оновлення кожну секунду

        self.update_timer()  # Показати початковий час

    def update_timer(self):
        if self.remaining_time > 0:
            self.label_timer.setText(f"Таймер: {self.remaining_time} секунд")
            self.remaining_time -= 1
        else:
            self.timer.stop()
            self.time_up()

    def time_up(self):
        w = Dialog(f"Час вийшов! Правильна відповідь: '{self.correct_answer}'", self)
        w.exec_()
        self.close()

    def get_unique_question(self):
        with open('question.txt', 'r', encoding="utf-8") as f:
            contents = f.readlines()

        available_questions = [q.strip() for q in contents if q.split('|')[0].strip() not in used_questions]
        
        if not available_questions:
            return "Всі питання вже використані!", "", []

        random_question_answer = random.choice(available_questions)
        question, correct_answer, *wrong_answers = random_question_answer.split('|')
        used_questions.add(question.strip())
        return question.strip(), correct_answer.strip(), [ans.strip() for ans in wrong_answers]

    def check_answer(self):
        sender = self.sender()
        if sender.text() == self.correct_answer:
            w = Dialog("Правильно!", self)
        else:
            w = Dialog(f"Неправильно! \nПравильна відповідь: '{self.correct_answer}'", self)
        w.exec_()

class Dialog(QDialog):
    def __init__(self, message, question_window):
        super(Dialog, self).__init__()
        self.question_window = question_window

        layout = QVBoxLayout(self)
        self.setWindowTitle("Результат")
        self.resize(1000, 700)
        self.setStyleSheet(f"background-color: {Color.fon}")

        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 40))
        self.label.setStyleSheet(f"color: {Color.label}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setText(message)

        self.btn = QPushButton("Закрити", self)
        self.btn.setFont(QFont("Arial", 15))
        self.btn.setMaximumHeight(80)
        self.btn.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """)
        self.btn.clicked.connect(self.def_btn)

        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)
    
    def def_btn(self):
        self.question_window.close()
        self.close() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
