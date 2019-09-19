# -*- coding: utf-8 -*-

from lt.base import Base
from lt.ui import Ui
# from lt.article import Article

class Lt(Base):

    def __init__(self):
        # self.article = Article()
        self.ui = Ui(self)

    def show(self):
        self.ui.show()
