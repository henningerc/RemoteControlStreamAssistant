from PySide2.QtWidgets import QTextEdit

from Model.ChatMessage import ChatMessage
from data import Data


class ChatPanel(QTextEdit):
    def __init__(self, data: Data):
        super().__init__()
        self.setReadOnly(True)
        self.data = data
        self.setStyleSheet("font-size: 24px;")
        self.show_message(data.chat.add_message("Daarin", "Hallo da bin ich!"))

    def show_message(self, msg: ChatMessage):
        text = ('<span style="color: {color}; background-color: {bg_color}">{name}</span> ' +
                '<span class="time">[{time}]: </span> ' +
                '<span class="message">{message}').format(
            color=msg.chatter.foreground_color,
            bg_color=msg.chatter.background_color,
            name=msg.chatter.name,
            time='{0:%H:%M:%S}'.format(msg.time),
            message=msg.message
        )
        self.insertHtml(text)
