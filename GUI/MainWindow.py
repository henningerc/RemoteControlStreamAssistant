from PySide2.QtWidgets import QWidget, QApplication, QGridLayout

from data import Data
from GUI.ControlPanel import ControlPanel


class MainWindow(QWidget):
    def __init__(self, dat: Data):
        self.data: Data = dat
        super().__init__()
        self.build()

    def build(self):
        control_panel = ControlPanel(self.data)
        self.setLayout(QGridLayout())
        self.layout().addWidget(control_panel)
        self.show()

