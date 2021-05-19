from typing import Dict, Set, TYPE_CHECKING

from Controller.StatusLamp import StatusLamp

if TYPE_CHECKING:
    from Model.Data import Data


class Status:
    scene_lamps: Set[StatusLamp] = set()
    overlay_lamps: Dict[str, Dict[str, Set[StatusLamp]]] = {}

    def __init__(self, data):
        self.data: Data = data

    async def set_scene(self, scene):
        for lamp in self.scene_lamps:
            lamp.status = scene
            lamp.redraw()

    async def set_overlay_visible(self, scene, source, visibility):
        if scene in self.overlay_lamps:
            if source in self.overlay_lamps[scene]:
                for lamp in self.overlay_lamps[scene][source]:
                    lamp.status = visibility
                    lamp.redraw()

    def register_lamp(self, lamp: StatusLamp):
        if lamp.operator == "scene_active":
            self.scene_lamps.add(lamp)
            return
        if lamp.operator == "scene_item_visible":
            if lamp.scene not in self.overlay_lamps:
                self.overlay_lamps[lamp.scene] = {}
            if lamp.source not in self.overlay_lamps[lamp.scene]:
                self.overlay_lamps[lamp.scene][lamp.source] = set()
            self.overlay_lamps[lamp.scene][lamp.source].add(lamp)
