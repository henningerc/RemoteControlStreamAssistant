import asyncio
from Model.Command import Command


def go(cmd: Command):
    for c in cmd.commands:
        if c["command"] == "switch_scene":
            asyncio.create_task(cmd.data.remote_control.change_scene(c["scene"]))
            return
        if c["command"] == "switch_overlay":
            asyncio.create_task(cmd.data.remote_control.toggle_scene_item_visibility(c["scene"], c["source"]))
            return
        if c["command"] == "set_scene_lamp":
            asyncio.create_task(cmd.data.status.set_scene(c["scene"]))
            return
