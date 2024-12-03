from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random

from design import design_widgets as DW
from . import Dialog

timer = 30
used_questions = set()

class QuestionWindow(QDialog):
    def __init__(self):
        super(QuestionWindow, self).__init__()

        layout = QVBoxLayout(self)
        self.setWindowTitle("Питання")
        self.resize(1200, 700)
        self.setStyleSheet(DW.Fon.fon_color)

        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 40))
        self.label.setStyleSheet(f"color: {DW.Color.label}")
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
            btn.setStyleSheet(DW.Btn.btn_design)
            btn.clicked.connect(self.check_answer)
            self.buttons.append(btn)
            layout.addWidget(btn)
        
        # Додавання таймера
        self.label_timer = QLabel(self)
        self.label_timer.setFont(QFont("Arial", 20))
        self.label_timer.setStyleSheet(f"color: {DW.Color.label}")
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
        w = Dialog.DialogWindow(f"Час вийшов! Правильна відповідь: '{self.correct_answer}'", self)
        w.exec_()
        self.close()

    def get_unique_question(self):
        with open('question/question_now.txt', 'r', encoding="utf-8") as f:
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
            w = Dialog.DialogWindow("Правильно!", self)
        else:
            w = Dialog.DialogWindow(f"Неправильно! \nПравильна відповідь: '{self.correct_answer}'", self)
        w.exec_()
