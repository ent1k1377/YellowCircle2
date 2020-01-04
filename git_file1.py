import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Random yellow circle')
        self.pushButton.clicked.connect(self.Button)
        self.x = False
        self.lst1 = []
        # !
    def Button(self):
        self.x = True
        self.lst1.append([random.randint(1, 500), random.randint(30, 500), random.randint(1, 500),
                          random.randint(30, 500), random.randint(1, 255), random.randint(1, 255),
                          random.randint(1, 255)])

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.rightClick(qp)
        qp.end()

    def rightClick(self, qp):
        if self.x:
            for i in range(len(self.lst1)):
                qp.setBrush(QColor(self.lst1[i][4], self.lst1[i][5], self.lst1[i][6]))
                qp.drawEllipse(self.lst1[i][0], self.lst1[i][1], self.lst1[i][2], self.lst1[i][3])
            self.update()
            self.Button()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
