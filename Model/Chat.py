from typing import Dict, List

from Model.Chatter import Chatter
from Model.ChatMessage import ChatMessage


class Chat:
    chatters: Dict[str, Chatter] = {}
    messages: List[ChatMessage] = []

    def add_message(self, chatter: str, text: str) -> ChatMessage:
        if chatter not in self.chatters.keys():
            self.chatters[chatter] = Chatter(chatter)

        c = self.chatters[chatter]
        msg = ChatMessage(c, text)
        self.messages.append(msg)
        return msg
