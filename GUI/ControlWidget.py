from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton
from PySide2.QtCore import SIGNAL, QSize
from PySide2.QtGui import QIcon

from Controller.StatusLamp import StatusLamp
from command import Command
from GUI.StatusWidget import StatusWidget


class ControlWidget(QWidget):
    def __init__(self, command):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.add_control_button(command)
        self.add_status_widget()

    def add_control_button(self, command: Command):
        button = QPushButton()
        button.connect(SIGNAL('clicked()'), lambda cmd=command: Command.go(cmd))
        if command.image is not None:
            button.setIconSize(QSize(150, 150))
            button.setIcon(QIcon(command.image))
            button.setStyleSheet("background-color: red;")
        else:
            button.setText(command.title + " (" + command.key + ")")
        self.layout.addWidget(button, 0, 0)

    def add_status_widget(self):
        sw = StatusWidget()
        sw.register_lamp(StatusLamp())
        self.layout.addWidget(sw, 1, 0)

