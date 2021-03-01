import data


class Command:
    def __init__(self, settings, dat: data.Data):
        self.id = settings["id"]
        self.title = settings["title"]
        self.commands = settings["commands"]
        self.data = dat

    def run(self):
        for c in self.commands:
            if c["command"] == "switch_scene":
                self.data.remote_control.change_scene(c["scene"])
