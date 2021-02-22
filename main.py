import sys
import asyncio
import time

# from PyQt5.QtWidgets import (
from PySide2.QtWidgets import (
    QApplication, QProgressBar)
from qasync import QEventLoop, QThreadExecutor
from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl


app = QApplication(sys.argv)
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

progress = QProgressBar()
progress.setRange(0, 99)
progress.show()

settings = Settings("settings.json")
chatbot = Chatbot(settings, loop)

rc = RemoteControl(settings, loop)

chatbot.set_remote_control(rc)
chatbot.run()
