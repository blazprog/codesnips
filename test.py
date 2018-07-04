# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def show_window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    show_window()
def ss():

