from PySide2.QtWidgets import QTextEdit


class ChatPanel(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.add_text()
    pass

    def add_text(self):
        self.insertHtml("<b>Hallo</b> <br />")
        self.insertHtml("<hr /> <br />")
        self.insertHtml("Insert 2")