from typing import Dict, Set, TYPE_CHECKING

from Controller.StatusLamp import StatusLamp

if TYPE_CHECKING:
    from data import Data


class Status:
    scene_active: str = ""
    overlay_active: Dict[str, bool] = {}

    scene_lamps: Set[StatusLamp] = set()
    overlay_lamps: Dict[str, Set[StatusLamp]] = {}

    def __init__(self, data):
        self.data: Data = data

    async def set_scene(self, scene):
        for lamp in self.scene_lamps:
            lamp.status = scene
            lamp.redraw()

    def register_lamp(self, lamp: StatusLamp):
        if lamp.operator == "scene_active":
            self.scene_lamps.add(lamp)
