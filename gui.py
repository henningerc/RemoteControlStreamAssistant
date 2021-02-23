from PySide2.QtWidgets import *
import sys
import asyncio
from qasync import QEventLoop, QThreadExecutor


class GUI:
    def __init__(self):
        self.app = QApplication([])
        self.loop = QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)
        self.window = QWidget()
        self.layout = QGridLayout()
        self.label = QLabel("Test")
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.label, 0, 0)
        self.window.show()

    def add_button(self, text, x, y):
        button = QPushButton(text)
        button.clicked.connect(self.test)
        self.layout.addWidget(button, x, y)

    def test(self):
        print("Test")