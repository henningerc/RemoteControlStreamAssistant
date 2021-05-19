from typing import Dict

from PySide2.QtWidgets import QWidget, QGridLayout, QSplitter
from PySide2.QtGui import QKeyEvent
from PySide2 import QtCore

from Model.Data import Data
from GUI.ControlPanel import ControlPanel
from GUI.keyboard_map import kb_map
from GUI.ChatPanel import ChatPanel
from Model.Command import Command
from Controller.CommandController import go


class MainWindow(QWidget):
    keys: Dict[QtCore.Qt.Key, Command] = {}

    def __init__(self, dat: Data):
        self.data: Data = dat
        super().__init__()
        self.build()
        self.register_keyboard_shortcuts()

    def build(self):
        control_panel = ControlPanel(self.data)
        splitter = QSplitter(QtCore.Qt.Horizontal)
        chat_panel = ChatPanel(self.data)

        splitter.addWidget(chat_panel)
        splitter.addWidget(control_panel)
        self.setLayout(QGridLayout())
        self.layout().addWidget(splitter)
        self.show()

    def register_keyboard_shortcuts(self):
        for cmd in self.data.commands.values():
            key = kb_map[cmd.key]
            self.keys[key] = cmd

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() in self.keys.keys():
            go(self.keys[event.key()])
