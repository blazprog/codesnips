# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from two_column_grid import InputGridLayout

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Import data to odoo')
        main_layout = QtWidgets.QVBoxLayout()
        input_layout = InputGridLayout()
        button_layout = QtWidgets.QHBoxLayout()
        # kreiram kontrole
        self.txtHost = input_layout.addControl(QtWidgets.QComboBox(),'Host')
        self.txtHost.addItems(self.readHosts())
        self.txtHost.setEditable(True)

        self.txtDatabase = input_layout.addControl(QtWidgets.QLineEdit(), 'Database')
        self.txtUser = input_layout.addControl(QtWidgets.QLineEdit('admin'), 'User')
        self.txtPassword = input_layout.addControl(QtWidgets.QLineEdit('Mentis2015#'), 'Password')
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
        print (self.txtHost.currentText())
        print (self.txtDatabase.text())
        print (self.txtUser.text())
        print (self.txtPassword.text())

    def readHosts(self):
        with open('hosts.lst', mode='r') as fh:
            hosts = fh.readlines()
        return [host.strip() for host in hosts]

def main():
    qapp = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.setGeometry(200, 300, 800, 190)
    dialog.show()
    sys.exit(qapp.exec_())

main()

