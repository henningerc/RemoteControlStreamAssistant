import asyncio

from qasync import QEventLoop

from GUI.MainWindow import MainWindow

from Controller.ChatBotController import ChatbotController
from Model.Settings import Settings
from Controller.RemoteControlController import RemoteControlController
from Model.Data import Data
from PySide2.QtWidgets import QApplication

data = Data()
app = QApplication()

loop = QEventLoop(app)
asyncio.set_event_loop(loop)

settings = Settings("settings.json", data)
gui = MainWindow(data)
chatbot = ChatbotController(settings, loop, data)

data.remote_control = RemoteControlController(data, loop)
chatbot.set_remote_control(data.remote_control)
asyncio.create_task(data.status.check_stati())
chatbot.run()
