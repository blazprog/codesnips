# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qtw
# from PyQt5.QtWidgets import QWidget, QApplication, QDialog, \ 
###        QMdiSubWindow
from PyQt5.QtSql import *

conn = QSqlDatabase.database()

class WordBrowse(QSqlTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTable('ozegov')
        self.select()

class EditForm(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('New Edit Form')
        lblWord = qtw.QLabel('Word')
        self.txtWord = qtw.QLineEdit()
        lblDescription = qtw.QLabel('Description')
        self.txtDescription = qtw.QTextEdit()
        self.main_layout = qtw.QVBoxLayout()
        self.main_layout.addWidget(lblWord)
        self.main_layout.addWidget(self.txtWord)
        self.main_layout.addWidget(lblDescription)
        self.main_layout.addWidget(self.txtDescription)
        self.setLayout(self.main_layout)
        self.model = WordBrowse()
        self.mapper = qtw.QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(qtw.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.txtWord, 0)
        self.mapper.addMapping(self.txtDescription, 1)
        self.mapper.toFirst()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ef = EditForm()
    ef.show()
    sys.exit(app.exec_())
