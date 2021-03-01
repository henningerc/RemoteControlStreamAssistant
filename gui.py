from functools import partial

from PySide2.QtWidgets import *
import asyncio
from qasync import QEventLoop, QThreadExecutor
from data import Data
from command import Command


class GUI:
    def __init__(self, dat: Data):
        self.data: Data = dat
        self.app = QApplication()
        self.loop = QEventLoop(self.app)
        self.window = self.define_control_panel()
        asyncio.set_event_loop(self.loop)
        self.layout = QGridLayout()
        self.window.setLayout(self.layout)
        self.window.show()

    def add_button(self, text, x, y):
        button = QPushButton(text)
        button.clicked.connect(self.test)
        self.layout.addWidget(button, x, y)

    def define_control_panel(self) -> QWidget:
        widget = QWidget()
        layout = QGridLayout()

        widget.setLayout(layout)

        for command_id in self.data.commands:
            command = self.data.commands[command_id]
            self.add_control_button(command, layout)
        return widget

    @staticmethod
    def add_control_button(command: Command, layout: QGridLayout):
        button = QPushButton(command.title)
        button.clicked.connect(partial(Command.go, command))

        layout.addWidget(button, command.pos["x"], command.pos["y"])

