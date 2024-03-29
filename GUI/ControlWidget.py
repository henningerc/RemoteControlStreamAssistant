from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton
from PySide2.QtCore import SIGNAL, QSize
from PySide2.QtGui import QIcon

from Controller.StatusLamp import StatusLamp
from Model.Command import Command
from Controller.CommandController import go
from GUI.StatusWidget import StatusWidget


class ControlWidget(QWidget):
    def __init__(self, command):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.add_control_button(command)
        self.add_status_widget(command)

    def add_control_button(self, command: Command):
        button = QPushButton()
        button.connect(SIGNAL('clicked()'), lambda cmd=command: go(cmd))
        if command.image is not None:
            button.setIconSize(QSize(150, 150))
            button.setIcon(QIcon(command.image))
        else:
            button.setText(command.title + " (" + command.key + ")")
        self.layout.addWidget(button, 0, 0)

    def add_status_widget(self, command):
        sw = StatusWidget()
        if command.status is not None:
            for i in command.status:
                lamp = StatusLamp(i, sw)
                sw.register_lamp(lamp)
                command.data.status.register_lamp(lamp)
        self.layout.addWidget(sw, 1, 0)

