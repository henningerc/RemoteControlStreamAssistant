from PySide2.QtWidgets import *
from PySide2.QtCore import QEventLoop
import asyncio
import time


class GUI:
    def __init__(self):
        self.app = QApplication([])
        asyncio.set_event_loop(QEventLoop(self.app))
        self.window = QWidget()
        self.layout = QGridLayout()
        self.label = QLabel("Test")

    def startup(self):
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.label, 0, 0)
        self.window.show()
        self.app.exec_()


# gui = GUI()