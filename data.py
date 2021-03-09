from typing import Optional, TYPE_CHECKING, Dict
from Model.Chat import Chat

if TYPE_CHECKING:
    import remote_control
    import settings
    import command


class Data:
    def __init__(self):
        self.remote_control: Optional[remote_control.RemoteControl] = None
        self.settings: Optional[settings.Settings] = None
        self.commands: Optional[Dict[str, command.Command]] = {}
        self.chat: Chat = Chat()
