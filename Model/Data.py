from typing import Optional, TYPE_CHECKING, Dict
from Model.Chat import Chat
from Controller.Status import Status

if TYPE_CHECKING:
    from Controller import RemoteControlController
    import settings
    from Model.Command import Command
    from GUI.ChatPanel import ChatPanel


class Data:
    def __init__(self):
        self.remote_control: Optional[RemoteControlController.RemoteControlController] = None
        self.settings: Optional[settings.Settings] = None
        self.commands: Optional[Dict[str, Command]] = {}
        self.chat: Chat = Chat()
        self.status: Status = Status(self)

        self.chat_panel: ChatPanel = None
