from time import localtime, struct_time
from datetime import datetime
from Model.Chatter import Chatter


class ChatMessage:
    chatter: Chatter = None
    message: str = ""
    time: datetime = datetime.now()

    def __init__(self, chatter, message):
        self.message = message
        self.chatter = chatter
        self.time = datetime.now()
