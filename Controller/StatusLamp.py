from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from data import Data
    from GUI.StatusWidget import StatusWidget


class StatusLamp:
    def __init__(self, settings, widget):
        self.operator = settings["operator"]
        self.standard_color = settings.get("default") or "#ffffff"
        self.colors: Dict[str, str] = {}
        self.widget: StatusWidget = widget

        self.status: str = ""

        if settings["operator"] == "scene_active":
            self.colors = settings["scenes"]

    def get_color(self):
        return self.colors.get(self.status) or self.standard_color

    def redraw(self):
        self.widget.repaint()
