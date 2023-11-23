import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Draw_circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()

    def circle(self, qp):
        color = QColor('yellow')
        x, y = randint(10, 590), randint(10, 590)
        d = randint(2, min(x, y, 800 - x, 600 - y) * 2)
        qp.setBrush(color)
        qp.drawEllipse(x - d // 2, y - d // 2, d, d)


def exept_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw_circle()
    ex.show()
    sys.exepthook = exept_hook
    sys.exit(app.exec())
