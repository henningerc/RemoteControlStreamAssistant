from PySide2.QtWidgets import *
import sys
import typing
import asyncio
import time
from asyncqt import QEventLoop, QThreadExecutor


class GUI:
    def __init__(self):
        self.app = QApplication([])
        self.loop = QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)
        self.window = QWidget()
        self.layout = QGridLayout()
        self.label = QLabel("Test")

    def startup(self):
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.label, 0, 0)
        self.window.show()

        with self.loop:
            sys.exit(self.loop.run_forever())
# gui = GUI()