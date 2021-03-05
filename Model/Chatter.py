import hashlib
import colorsys


class Chatter:
    name: str = ""
    foreground_color: str = ""
    background_color: str = ""

    def __init__(self, name):
        self.name = name
        self.calculate_colors()

    def calculate_colors(self):
        md5 = hashlib.md5(self.name.encode()).hexdigest()
        fg = colorsys.rgb_to_hsv(*tuple(int(md5[i:i+2], 16)/255 for i in (0, 2, 4)))
        bg = colorsys.rgb_to_hsv(*tuple(int(md5[i:i+2], 16)/255 for i in (6, 8, 10)))

        fg_lighter = False
        if fg[2] > bg[2]:
            fg_lighter = True

        if (fg[2]-bg[2])*(1 if fg_lighter else -1) < 0.5:
            more = (0.5-(fg[2]-bg[2])*(1 if fg_lighter else -1))/2
            fg = (fg[0], fg[1], fg[2] + more * (1 if fg_lighter else -1))
            bg = (bg[0], bg[1], bg[2] - more * (1 if fg_lighter else -1))

        fg_lighter = False
        if fg[1] > bg[1]:
            fg_lighter = True

        if (fg[1]-bg[1])*(1 if fg_lighter else -1) > 0.1:
            more = (0.1-(fg[1]-bg[1])*(-1 if fg_lighter else 1))/2
            fg = (fg[0], fg[1] - more * (1 if fg_lighter else -1), fg[2])
            bg = (bg[0], bg[1] + more * (1 if fg_lighter else -1), bg[2])
        fg = colorsys.hsv_to_rgb(*fg)
        bg = colorsys.hsv_to_rgb(*bg)

        self.foreground_color = '#' + ''.join(tuple(hex(int(i * 255))[2:4] for i in fg))
        self.background_color = '#' + ''.join(tuple(hex(int(i * 255))[2:4] for i in bg))

    def colored_span(self):
        return '<span style="color: ' + self.foreground_color + '; background-color: ' + self.background_color + ';">' \
            + self.name + '</span>'


chatter_names = ["Daarin", "julaha", "Julaha", "Sören", "Sajii", "Anterion", "WasWeißIch"]
for name in chatter_names:
    c = Chatter(name)
    print(c.colored_span())
