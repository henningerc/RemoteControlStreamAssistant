import asyncio
from PySide2.QtWidgets import *
from PySide2.QtCore import QEventLoop

import simpleobsws

from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl
from gui import GUI

settings = Settings("settings.json")
loop = asyncio.get_event_loop()
chatbot = Chatbot(settings, loop)

rc = RemoteControl(settings, loop)

chatbot.set_remote_control(rc)
chatbot.run()
