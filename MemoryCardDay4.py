from PyQt5.Qt import QLabel, QGroupBox, QButtonGroup, QPushButton, QRadioButton, QApplication, QWidget, QMainWindow, \
    QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

class QuestionForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memo Card')
        self.resize(400, 300)

        # Создание виджетов
        self.question_label = QLabel('Вопрос', self)

        self.res_label = QLabel('Энцы', self)
        self.correct_label = QLabel('Правильно/Неправильно', self)

        self.correct_layout = QVBoxLayout()

        self.central_widget = QWidget()
        self.Radio_GroupBox = QGroupBox('Варианты ответа', self)
        self.Answer_GroupBox = QGroupBox('Результат теста', self)

        self.Radio_Group = QButtonGroup()
        self.rbtn_1 = QRadioButton('Вариант 1', self)
        self.rbtn_2 = QRadioButton('Вариант 2', self)
        self.rbtn_3 = QRadioButton('Вариант 3', self)
        self.rbtn_4 = QRadioButton('Вариант 4', self)

        self.Radio_Group.addButton(self.rbtn_1)
        self.Radio_Group.addButton(self.rbtn_2)
        self.Radio_Group.addButton(self.rbtn_3)
        self.Radio_Group.addButton(self.rbtn_4)

        self.answer_button = QPushButton('Ответить', self)

        self.layout = QVBoxLayout()
        self.answer_layout = QHBoxLayout()
        self.answer_layout_left = QVBoxLayout()
        self.answer_layout_right = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        self.ask_list = [self.rbtn_1, self.rbtn_2, self.rbtn_3, self.rbtn_4]

        # Объект класса Question
        q = Question('Государственный язык бразилии', 'Португальский', 'Английский', 'Русский', 'Финикийский')
        self.q = q

        self.question_list = []
        self.question_list.append(Question('Государственный язык бразилии', 'Португальский', 'Английский', 'Русский', 'Финикийский'))
        self.question_list.append(Question('На каком континенте живут китайцы?', 'Азия', 'Европа', 'Северная Америка', 'Австралия'))
        self.question_list.append(Question('На каком языке говорят в Германии', 'Немецкий', 'Германский', 'Украинский', 'Английский'))
        self.question_list.append(Question('Какое население в России', '146 млн', '4', '1 млн', '3 млрд'))
        self.question_list.append(Question('В каком году появилась Франция?', '1792', 'вчера', '2012', '1000'))
        shuffle(self.question_list)
        self.cur_question = -1

        self.stat = 0
        self.countQ = 0
        self.countA = 0

        self.Answer_GroupBox.hide()
        self.setUp_UI()
        #self.ask(q)

        self.next_question()
        self.answer_button.clicked.connect(self.click_Ok)

    def setUp_UI(self):
        # Закрепление левого лэйаута
        self.answer_layout_left.addWidget(self.rbtn_1)
        self.answer_layout_left.addWidget(self.rbtn_2)

        # Создание лэйаутов для лэйблов в ответном группбоксе(РАССКАЗАТЬ)
        self.correct_layout.addWidget(self.correct_label, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.correct_layout.addWidget(self.res_label, alignment=Qt.AlignHCenter, stretch=2)

        # Закрепление правого лэйаута
        self.answer_layout_right.addWidget(self.rbtn_3)
        self.answer_layout_right.addWidget(self.rbtn_4)

        # Установка alignment и spacing для радиокнопок
        self.answer_layout_left.setAlignment(Qt.AlignTop)
        self.answer_layout_left.setSpacing(50)

        self.answer_layout_right.setAlignment(Qt.AlignTop)
        self.answer_layout_right.setSpacing(50)

        # Слияние правого и левого лэйаутов
        self.answer_layout.addLayout(self.answer_layout_left)
        self.answer_layout.addLayout(self.answer_layout_right)

        # И помещение в группбоксы вопросительный и ответный соответственно(РАССКАЗАТЬ)
        self.Radio_GroupBox.setLayout(self.answer_layout)

        self.Answer_GroupBox.setLayout(self.correct_layout)
        # Установка alignment и spacing для кнопки и лэйбла
        self.button_layout.addWidget(self.answer_button)

        self.question_label.setAlignment(Qt.AlignCenter)

        self.button_layout.setAlignment(Qt.AlignCenter)
        self.button_layout.setSpacing(20)

        # Создание лэйаута для центрального виджета
        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.Radio_GroupBox)
        self.layout.addWidget(self.Answer_GroupBox)
        self.layout.addLayout(self.button_layout)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def show_result(self):
        self.Radio_GroupBox.hide()
        self.Answer_GroupBox.show()
        self.answer_button.setText('Следующий вопрос')

    def show_question(self):
        self.Radio_GroupBox.show()
        self.Answer_GroupBox.hide()
        self.answer_button.setText('Ответить')
        self.Radio_Group.setExclusive(False)
        for self.button in self.Radio_Group.buttons():
            self.button.setChecked(False)
        self.Radio_Group.setExclusive(True)

    def start_test(self):
        if self.answer_button.text() == 'Ответить':
            self.show_result()
        else:
            self.show_question()









    def ask(self, q:Question):
        self.q = q
        shuffle(self.ask_list)
        self.ask_list[0].setText(self.q.right_answer)
        self.ask_list[1].setText(self.q.wrong1)
        self.ask_list[2].setText(self.q.wrong2)
        self.ask_list[3].setText(self.q.wrong3)
        self.question_label.setText(self.q.question)
        self.res_label.setText(self.q.right_answer)
        self.Radio_Group.setExclusive(False)
        for self.button in self.Radio_Group.buttons():
            self.button.setChecked(False)
        self.Radio_Group.setExclusive(True)
        self.Radio_GroupBox.show()
        self.Answer_GroupBox.hide()
        self.status_Q()

    def check_answer(self):
        if self.ask_list[0].isChecked():
            self.show_correct('Правильно!')
        else:
            self.show_correct('Неправильно!')


    def show_correct(self, res):
        self.res = res
        self.correct_label.setText(self.res)
        self.Answer_GroupBox.show()
        self.Radio_GroupBox.hide()
        self.countQ += 1
        self.status_Q()

    def next_question(self):
        if self.cur_question == len(self.question_list):
            self.cur_question = -1
        self.cur_question += 1
        self.ask(self.question_list[self.cur_question])

    def click_Ok(self):

        if self.answer_button.text() == 'Ответить':
            self.answer_button.setText('Следующий вопрос')
            self.check_answer()
        else:
            self.answer_button.setText('Ответить')
            self.next_question()


    def status_Q(self):
        print('--------------------------')
        print('Статистика')
        print('Всего вопросов:', self.countQ)
        if self.ask_list[0].isChecked():
            self.countA += 1
        print('Правильных ответов:', self.countA)
        try:
            self.stat = self.countA / self.countQ * 100
        except:
            self.stat = 0
        print('Рейтинг:', self.stat,'%')
        print('--------------------------')






app = QApplication([])
quest = QuestionForm()
quest.show()
app.exec()