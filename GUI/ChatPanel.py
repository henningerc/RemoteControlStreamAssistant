from PySide2.QtWidgets import QTextEdit

from Model.ChatMessage import ChatMessage
from Model.Data import Data


class ChatPanel(QTextEdit):
    def __init__(self, data: Data):
        super().__init__()
        self.setReadOnly(True)
        self.data = data
        data.chat_panel = self
        self.setStyleSheet("font-size: 24px;")

    def show_message(self, msg: ChatMessage):
        text = ('<span style="color: {color}; background-color: {bg_color}">{name}</span> ' +
                '<span class="time">[{time}]: </span> ' +
                '<span class="message">{message}</span><br />').format(
            color=msg.chatter.foreground_color,
            bg_color=msg.chatter.background_color,
            name=msg.chatter.name,
            time='{0:%H:%M:%S}'.format(msg.time),
            message=msg.message
        )
        self.insertHtml(text)
