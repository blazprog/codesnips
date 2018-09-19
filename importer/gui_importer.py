# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Import data to odoo')
        main_layout = QtWidgets.QVBoxLayout()
        input_layout = QtWidgets.QGridLayout()
        button_layout = QtWidgets.QHBoxLayout()
        # kreiram kontrole
        lblHost = QtWidgets.QLabel('Host')
        self.txtHost = QtWidgets.QLineEdit('https://localhost:8069')
        lblDatabase = QtWidgets.QLabel('Database')
        self.txtDatabase = QtWidgets.QLineEdit()
        lblUser = QtWidgets.QLabel('User')
        self.txtUser = QtWidgets.QLineEdit('admin')
        lblPassword = QtWidgets.QLabel('Password')
        self.txtPassword = QtWidgets.QLineEdit('Mentis2015#')
        # dodam jih na layout
        input_layout.addWidget(lblHost, 0, 0)
        input_layout.addWidget(self.txtHost, 0, 1)
        input_layout.addWidget(lblDatabase, 1, 0 )
        input_layout.addWidget(self.txtDatabase, 1, 1)
        input_layout.addWidget(lblUser, 2, 0 )
        input_layout.addWidget(self.txtUser, 2, 1)
        input_layout.addWidget(lblPassword, 3, 0 )
        input_layout.addWidget(self.txtPassword, 3, 1)
        # kreiram ukazne gumbe
        self.pbImport = QtWidgets.QPushButton('Import')
        self.pbClose = QtWidgets.QPushButton('Close')
        # ukazne gumbe povezem z metodami
        self.pbImport.clicked.connect(self.import_data)
        self.pbClose.clicked.connect(self.close)
        #ukazne gumbe na layout
        button_layout.addStretch(1)
        button_layout.addWidget(self.pbImport)
        button_layout.addWidget(self.pbClose)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def import_data(self):
        print('Imprting data to odoo')

def main():
    qapp = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.setGeometry(200, 300, 600, 190)
    dialog.show()
    sys.exit(qapp.exec_())

main()

