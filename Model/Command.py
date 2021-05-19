from Model import Data


class Command:
    def __init__(self, settings, dat: Data.Data):
        self.id = settings["id"]
        self.title = settings["title"]
        self.commands = settings["commands"]
        self.image = settings.get("image")
        self.color = settings.get("color")
        self.data = dat
        string: str = settings["position"]
        position = string.replace(" ", "").split(",")
        self.pos = {"x": int(position[0]), "y": int(position[1])}
        self.key = settings["key"]
        self.status = settings.get("status")
