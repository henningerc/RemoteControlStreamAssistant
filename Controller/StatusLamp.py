from typing import Dict


class StatusLamp:
    status: str = ""
    colors: Dict[str, str] = {}
    standard_color: str = "#ff0000"

    def get_color(self):
        return self.colors.get(self.status) or self.standard_color
