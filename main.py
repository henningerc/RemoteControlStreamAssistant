from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl
from gui import GUI
from data import Data


data = Data()

settings = Settings("settings.json", data)
gui = GUI(data)
loop = gui.loop
chatbot = Chatbot(settings, loop)

data.remote_control = RemoteControl(settings, loop)
chatbot.set_remote_control(data.remote_control)
chatbot.run()
