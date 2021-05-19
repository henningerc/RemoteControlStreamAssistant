import asyncio

from qasync import QEventLoop

from GUI.MainWindow import MainWindow

from Controller.ChatBotController import ChatbotController
from settings import Settings
from remote_control import RemoteControl
from Model.Data import Data
from PySide2.QtWidgets import QApplication

data = Data()
app = QApplication()

loop = QEventLoop(app)
asyncio.set_event_loop(loop)

settings = Settings("settings.json", data)
gui = MainWindow(data)
chatbot = ChatbotController(settings, loop, data)

data.remote_control = RemoteControl(data, loop)
chatbot.set_remote_control(data.remote_control)
chatbot.run()
