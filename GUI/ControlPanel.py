from PySide2.QtWidgets import QGridLayout, QPushButton, QWidget
from PySide2.QtCore import SIGNAL

from command import Command
from data import Data


class ControlPanel(QWidget):
    def __init__(self, dat: Data):
        super().__init__()
        self.data: Data = dat
        layout = QGridLayout()
        self.setLayout(layout)
        self.setup_buttons()

    def setup_buttons(self):
        for command_id in self.data.commands:
            command = self.data.commands[command_id]
            self.add_control_button(command, self.layout())

    @staticmethod
    def add_control_button(command: Command, layout: QGridLayout):
        button = QPushButton(command.title + " (" + command.key + ")")
        button.connect(SIGNAL('clicked()'), lambda cmd=command: Command.go(cmd))
        layout.addWidget(button, command.pos["x"], command.pos["y"])
