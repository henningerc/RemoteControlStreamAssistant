import asyncio

from qasync import QEventLoop

from GUI.MainWindow import MainWindow

from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl
from data import Data
from PySide2.QtWidgets import QApplication

data = Data()
app = QApplication()

loop = QEventLoop(app)
asyncio.set_event_loop(loop)

settings = Settings("settings.json", data)
gui = MainWindow(data)
chatbot = Chatbot(settings, loop, data)

data.remote_control = RemoteControl(settings, loop)
chatbot.set_remote_control(data.remote_control)
chatbot.run()
