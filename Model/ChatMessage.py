from time import localtime, struct_time
from Model.Chatter import Chatter


class ChatMessage:
    chatter: Chatter = None
    message: str = ""
    time: struct_time = localtime()

    def __init__(self, chatter, message):
        self.message = message
        self.chatter = chatter
        self.time = localtime()
