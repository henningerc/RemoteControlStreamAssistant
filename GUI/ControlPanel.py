from PySide2.QtWidgets import QGridLayout, QPushButton, QWidget, QLabel
from PySide2.QtCore import SIGNAL, QSize
from PySide2.QtGui import QIcon

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
        button = QPushButton()
        button.connect(SIGNAL('clicked()'), lambda cmd=command: Command.go(cmd))
        if command.image is not None:
            button.setIconSize(QSize(150, 150))
            button.setIcon(QIcon(command.image))
            button.setStyleSheet("background-color: red;")
        else:
            button.setText(command.title + " (" + command.key + ")")
        layout.addWidget(button, command.pos["x"], command.pos["y"])
