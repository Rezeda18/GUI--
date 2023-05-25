from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.acceptDrops()
        self.setFixedWidth(563)
        self.setFixedHeight(333)
        self.setWindowTitle("  ")
        self.label = QLabel(self)
        self.pix = QPixmap('котёнок трассировка.jpg')
        self.label.setPixmap(self.pix)
        self.label.resize(self.pix.width(),
                          self.pix.height())
        self.s = " "
        self.r()

    def r(self):
        self.btn = QPushButton("Сгенерировать список фильмов", self)
        self.btn.setGeometry(113, 233, 337, 50)
        self.btn.setStyleSheet("background-color: rgb(230, 230, 250)")
        self.btn.setFont(QFont("Arial", 12))
        self.cb = QComboBox(self)
        self.cb.addItems([' ','Фильм', 'Сериал'])
        self.cb.setGeometry(113, 63, 337, 50)
        self.cb.setStyleSheet("background-color: rgb(230, 230, 250)")
        self.cb.setFont(QFont("Arial", 16))
        self.l2 = QLabel(self)
        self.l2.setText("Что хотите посмотреть?")
        self.l2.setGeometry(113, 13, 337, 40)
        self.l2.setFont(QFont("Arial", 18))
        self.l = QLabel(self)
        self.l.setText("Впишите жанр ")
        self.l.setGeometry(113, 123, 337, 40)
        self.l.setFont(QFont("Arial", 18))
        self.q = QLineEdit(self)
        self.q.setGeometry(113, 173, 337, 50)
        self.q.setStyleSheet("background-color: rgb(230, 230, 250)")
        self.q.setFont(QFont("Arial", 16))
        self.cb.activated.connect(self.act1)
        self.btn.clicked.connect(self.act)

        self.Dict = {"2": {"детектив": "Шерлок Холмс, Как избежать наказание за убийство,  Менталист ",
                           "фантастика": "Древние,  Уэнсдей,  Академия Амбрелла ",
                           "комедия": "Фея тяжелой атлетики,  Деловое предложение,  Плохой и сумашедший  "},
                     "1": {"детектив": "Код Да Винчи,  Убийство в восточном экспрессе,  Достать ножи  ",
                           "фантастика": "Стражи Галактики, Наследники,  Алиса в зазеркалье  ",
                           "комедия": "Блондинка в законе, "
                                      "Затерянный город, "
                                      "Круэлла  "}}

    def act(self):
            self.s = self.q.text()
            print(self.s)
            self.p = self.Dict[str(self.d)][str(self.s)]
            print(self.p)
            self.msb = QMessageBox()
            self.msb.setStyleSheet("background-color: rgb(230, 230, 250)")
            self.msb.setText(str(self.p))
            self.msb.setFont(QFont("Arial", 16))
            self.msb.exec()
            "QMessageBox.about(self, "   ", str(self.p))"
    def act1(self, index):
            self.d = index
            print(self.d)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())