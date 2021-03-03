from typing import Dict

from PySide2.QtWidgets import QWidget, QGridLayout
from PySide2.QtGui import QKeyEvent
from PySide2 import QtCore

from data import Data
from GUI.ControlPanel import ControlPanel
from GUI.keyboard_map import kb_map
from command import Command


class MainWindow(QWidget):
    keys: Dict[QtCore.Qt.Key, Command] = {}

    def __init__(self, dat: Data):
        self.data: Data = dat
        super().__init__()
        self.build()
        self.register_keyboard_shortcuts()

    def build(self):
        control_panel = ControlPanel(self.data)
        self.setLayout(QGridLayout())
        self.layout().addWidget(control_panel)
        self.show()

    def register_keyboard_shortcuts(self):
        for cmd in self.data.commands.values():
            key = kb_map[cmd.key]
            self.keys[key] = cmd

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.keys[event.key()].go()
