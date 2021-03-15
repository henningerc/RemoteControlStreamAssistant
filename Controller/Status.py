from typing import Dict

from Controller.StatusLamp import StatusLamp


class Status:
    scene_active: str = ""
    overlay_active: Dict[str, bool] = {}

    scene_lamps: Dict[StatusLamp] = {}
    overlay_lamps: Dict[str, Dict[StatusLamp]] = {}

    def set_scene(self, scene):
        for lamp in self.scene_lamps:
            lamp.status = scene
