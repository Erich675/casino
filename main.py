from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QLineEdit, QMessageBox
)
from random import choices

ap = QApplication([])
win = QWidget()
win.setWindowTitle('Казиноскам')
win.resize(900, 600)

money = 10000
money_win = 1000000
money_label = QLabel("Счет: " + str(money))

color_input = QLineEdit('')
color_input.setPlaceholderText('Выбери цвет, на который хотите сделать ставку: ')

dep_input = QLineEdit('')
dep_input.setPlaceholderText('Ставка: ')


color_win = QLabel('Тут будет какой цвет победил')

result = QLabel('Итог: ')

btn = QPushButton(text='Запустить раунд')
def error_message():
    msg = QMessageBox()
    msg.setWindowTitle("Ошибка")
    msg.setText('Неправильно, попробуйте ещё раз!')
    msg.exec_()



def play():
    global money
    colors = ['красный', 'зелёный', 'чёрный']
    color = choices(colors, [45, 10, 45])[0]
    print(color)
    if color_input.text() and dep_input.text():
        try:
            if color_input.text() in colors and int(dep_input.text()):
                color_win.setText(color)
                dep = int(dep_input.text())

                if color_input.text() == color:
                    money += dep
                    money_label.setText("Счет: " + str(money))
                    result.setText("+ " + str(dep))
                else:
                    money -= dep
                    result.setText("- " + str(dep))
                    money_label.setText("Счет: " + str(money))
            else:
                error_message()
                color_input.clear()
                dep_input.clear()
        except Exception as e:
            print(e)
            error_message()
            color_input.clear()
            dep_input.clear()
    else:
        error_message()
        color_input.clear()
        dep_input.clear()


v = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()
h6 = QHBoxLayout()

h1.addWidget(money_label, alignment=Qt.AlignCenter)
h2.addWidget(color_input, alignment=Qt.AlignCenter)
h3.addWidget(dep_input, alignment=Qt.AlignCenter)
h4.addWidget(color_win, alignment=Qt.AlignCenter)
h5.addWidget(result, alignment=Qt.AlignCenter)
h6.addWidget(btn, alignment=Qt.AlignCenter)

v.addLayout(h1)
v.addLayout(h2)
v.addLayout(h3)   
v.addLayout(h4)
v.addLayout(h5)
v.addLayout(h6)

win.setLayout(v)

btn.clicked.connect(play)

win.show()

ap.exec_()
