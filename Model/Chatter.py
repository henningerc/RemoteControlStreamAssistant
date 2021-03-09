from Controller.ColorController import calculate_colors


class Chatter:
    name: str = ""
    foreground_color: str = ""
    background_color: str = ""

    def __init__(self, name):
        self.name = name
        colors = calculate_colors(name)
        self.foreground_color = colors[0]
        self.background_color = colors[1]

    def colored_span(self):
        return '<span style="color: ' + self.foreground_color + '; background-color: ' + self.background_color + ';">' \
            + self.name + '</span>'
