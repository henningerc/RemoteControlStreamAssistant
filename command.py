import data
import asyncio


class Command:
    def __init__(self, settings, dat: data.Data):
        self.id = settings["id"]
        self.title = settings["title"]
        self.commands = settings["commands"]
        self.data = dat
        string: str = settings["position"]
        position = string.replace(" ", "").split(",")
        self.pos = {"x": int(position[0]), "y": int(position[1])}
        self.key = settings["key"]
        print(self.pos)

    def go(self):
        for c in self.commands:
            if c["command"] == "switch_scene":
                asyncio.create_task(self.data.remote_control.change_scene(c["scene"]))
                return
            if c["command"] == "switch_overlay":
                asyncio.create_task(self.data.remote_control.toggle_scene_item_visibility(c["scene"], c["source"]))
                return
