from chatbot import Chatbot
from settings import Settings
from remote_control import RemoteControl
from gui import GUI

gui = GUI()

loop = gui.loop

settings = Settings("settings.json")
chatbot = Chatbot(settings, loop)

rc = RemoteControl(settings, loop)

chatbot.set_remote_control(rc)
chatbot.run()
