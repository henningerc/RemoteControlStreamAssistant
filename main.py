from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl
from gui import GUI
from data import Data

gui = GUI()

loop = gui.loop

data = Data()

settings = Settings("settings.json", data)
chatbot = Chatbot(settings, loop)

rc = RemoteControl(settings, loop)
gui.add_button("Test", 1, 1)
chatbot.set_remote_control(rc)
chatbot.run()
