import sys
import asyncio
import time

from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl
from gui import GUI

# from PyQt5.QtWidgets import (
from PySide2.QtWidgets import (
    QApplication, QProgressBar)
from asyncqt import QEventLoop, QThreadExecutor


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


st = Settings("settings.json")
cb = Chatbot(st, loop)
cb.run()

with loop:
    loop.run_until_complete(master())
    loop.run_forever()
