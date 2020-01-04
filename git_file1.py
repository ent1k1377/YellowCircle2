import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPainterPath


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellowcircle.ui', self)
        self.setWindowTitle('Random yellow circle')
        self.pushButton_1.clicked.connect(self.Button)
        self.x = False
        self.lst1 = []

    def Button(self):
        self.x = True
        self.lst1.append([random.randint(1, 500), random.randint(30, 500), random.randint(1, 500),
                       random.randint(30, 500)])

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.rightClick(qp)
        qp.end()

    def rightClick(self, qp):
        if self.x:
            for i in range(len(self.lst1)):
                qp.setBrush(QColor('yellow'))
                qp.drawEllipse(self.lst1[i][0], self.lst1[i][1], self.lst1[i][2], self.lst1[i][3])
            self.update()
            self.Button()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
