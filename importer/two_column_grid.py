# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *

class InputGridLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.rows = 0

    def addInputControl(self, input_ctl, label_text):
        lbl = QLabel(label_text)
        self.addWidget(lbl, self.rows, 0)
        self.addWidget(input_ctl, self.rows, 1)
        self.rows += 1

    def addControl(self, input_ctl, label_text):
        lbl = QLabel(label_text)
        self.addWidget(lbl, self.rows, 0)
        self.addWidget(input_ctl, self.rows, 1)
        self.rows += 1
        return input_ctl
