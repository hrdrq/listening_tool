# -*- coding: utf-8 -*-

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

class Shortcut:

    def __init__(self, ui):
        self.left = QShortcut(QKeySequence("Left"), ui)
        self.right = QShortcut(QKeySequence("Right"), ui)
        self.shift_left = QShortcut(QKeySequence("Shift+Left"), ui)
        self.shift_right = QShortcut(QKeySequence("Shift+Right"), ui)
        self.a = QShortcut(QKeySequence("A"), ui)
        self.d = QShortcut(QKeySequence("D"), ui)
        self.space = QShortcut(QKeySequence("Space"), ui)
