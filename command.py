import data


class Command:
    def __init__(self, settings, dat: data.Data):
        self.id = settings["id"]
        self.title = settings["title"]
        self.commands = settings["commands"]
        self.data = dat
        string: str = settings["position"]
        position = string.replace(" ", "").split(",")
        self.pos = {"x": int(position[0]), "y": int(position[1])}
        print(self.pos)

    def run(self):
        for c in self.commands:
            if c["command"] == "switch_scene":
                pass # self.data.remote_control.change_scene(c["scene"])
