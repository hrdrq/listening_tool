# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

from lt.base import Base
# from lt.ui.list import List
# from lt.ui.view import View
from lt.shortcut import Shortcut
from lt.player import Player

class Ui(QMainWindow):

    def __init__(self, lt):
        super().__init__()
        self.lt = lt
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 40


        self.shortcut = Shortcut(self)
        self.player = Player()
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.shortcut.a.activated.connect(self.player.add)
        self.shortcut.space.activated.connect(self.player.play_pause)
        # self.shortcut.down.activated.connect(self.view.to_next_sentence)
        # self.shortcut.ctrl_up.activated.connect(self.view.to_first_sentence)
        # self.shortcut.ctrl_down.activated.connect(self.view.to_last_sentence)
        # self.shortcut.slash.activated.connect(self.view.play_sentence)
        # self.shortcut.underline.activated.connect(self.view.play_sentence)
        # self.shortcut.dot.activated.connect(self.view.play_paragraph)
        # self.shortcut.e.activated.connect(self.view.tool_bar.show_edit)
