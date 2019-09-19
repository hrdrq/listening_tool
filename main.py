# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from lt import Lt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lt = Lt()
    lt.show()
    sys.exit(app.exec_())
