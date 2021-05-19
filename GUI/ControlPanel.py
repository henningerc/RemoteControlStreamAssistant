from PySide2.QtWidgets import QGridLayout, QWidget

from Model.Data import Data
from GUI.ControlWidget import ControlWidget


class ControlPanel(QWidget):
    def __init__(self, dat: Data):
        super().__init__()
        self.data: Data = dat
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setup_buttons()

    def setup_buttons(self):
        for command_id in self.data.commands:
            command = self.data.commands[command_id]
            self.layout.addWidget(ControlWidget(command), command.pos["x"], command.pos["y"])
