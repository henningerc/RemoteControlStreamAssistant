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


async def master():
    await first_50()
    with QThreadExecutor(1) as exec:
        await loop.run_in_executor(exec, last_50)


async def first_50():
    for i in range(50):
        progress.setValue(i)
        await asyncio.sleep(.1)


def last_50():
    for i in range(50, 100):
        loop.call_soon_threadsafe(progress.setValue, i)
        time.sleep(.1)


settings = Settings("settings.json")
loop = asyncio.get_event_loop()
chatbot = Chatbot(settings, loop)

rc = RemoteControl(settings, loop)

chatbot.set_progress(progress)

chatbot.set_remote_control(rc)
chatbot.run()
