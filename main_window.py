# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qtw
# from PyQt5.QtWidgets import QMainWindow, QApplication, 
# QMdiArea, QMdiSubWindow
from PyQt5.QtSql import QSqlDatabase

from edit_form import EditForm



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        menubar = self.menuBar()
        newAction = qtw.QAction('New', self)
        newAction.triggered.connect(self.showEditForm)

        editAction = qtw.QAction('Edit', self)
        # editdAction.triggered.connect(qtw.qApp.quit)

        exitAction = qtw.QAction('Exit', self)
        exitAction.triggered.connect(qtw.qApp.quit)

        fileMenu  = menubar.addMenu('File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(editAction)
        fileMenu.addAction(exitAction)
        self.showMaximized()
        

    def showEditForm(self):
        print ('Editing form')
        sub = QMdiSubWindow()
        sub.setWidget(EditForm())
        self.mdi.addSubWindow(sub)
        sub.show()



def my_boo(param):
    for i in range(10):
        print i

def my_foo(param):
    print 'It''s my foo'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    db = QSqlDatabase.addDatabase("QPSQL")
    db.setDatabaseName('ozegov')
    ok = db.open()
    if ok:
        my_foo()
        print ('Successfully connected')
    sys.exit(app.exec_())
