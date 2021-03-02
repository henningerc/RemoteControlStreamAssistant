from functools import partial

from PySide2.QtWidgets import *
import asyncio
from qasync import QEventLoop, QThreadExecutor
from data import Data
from command import Command
from GUI.ControlPanel import ControlPanel


class GUI:
    def __init__(self, dat: Data):
        self.data: Data = dat
        self.app = QApplication()
        self.loop = QEventLoop(self.app)
        # self.window: QWidget = self.define_control_panel()
        self.window = ControlPanel(dat)
        asyncio.set_event_loop(self.loop)
        self.window.show()


