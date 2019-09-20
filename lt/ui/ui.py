# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import QWidget, QMainWindow, QWidget, QHBoxLayout, QLabel
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
        self.width = 800
        self.height = 45


        self.shortcut = Shortcut(self)
        self.player = Player(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.widget = QWidget()
        self.time_label = QLabel('', self)
        self.sub_label = QLabel('', self)
        self.prev_sub_label = QLabel('', self)
        self.sub_label.move(100, 15)
        self.prev_sub_label.move(100, 0)
        self.sub_label.setFixedWidth(650)
        self.prev_sub_label.setFixedWidth(650)
        self.sub_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.prev_sub_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.shortcut.a.activated.connect(self.player.add)
        self.shortcut.d.activated.connect(self.open_dictionary)
        self.shortcut.space.activated.connect(self.player.play_pause)
        self.shortcut.left.activated.connect(self.player.repeat)
        self.shortcut.shift_left.activated.connect(self.player.back)
        # self.shortcut.down.activated.connect(self.view.to_next_sentence)
        # self.shortcut.ctrl_up.activated.connect(self.view.to_first_sentence)
        # self.shortcut.ctrl_down.activated.connect(self.view.to_last_sentence)
        # self.shortcut.slash.activated.connect(self.view.play_sentence)
        # self.shortcut.underline.activated.connect(self.view.play_sentence)
        # self.shortcut.dot.activated.connect(self.view.play_paragraph)
        # self.shortcut.e.activated.connect(self.view.tool_bar.show_edit)

    def update_sub(self, sub, prev_sub):
        self.sub_label.setText(sub)
        self.prev_sub_label.setText(prev_sub)

    def update_time(self, now, total):
        # print(now, '/', total)
        self.time_label.setText('{}:{} / {}:{}'.format(now//60, now%60, total//60, total%60))

    def open_dictionary(self):
        word = self.sub_label.selectedText()
        if word:
            os.system('open dict:///' + word)
