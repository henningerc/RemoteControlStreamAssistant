import hashlib


def calculate_colors(name: str):
    md5 = hashlib.md5(name.encode()).hexdigest()

    fg = tuple(int(md5[i:i + 2], 16) for i in (0, 2, 4))
    bg = tuple(int(md5[i:i + 2], 16) for i in (6, 8, 10))

    lumin = int(0.2126 * fg[0] + 0.7152 * fg[1] + 0.0722 * fg[2])
    if lumin <= 127:
        bg = tuple(lighter_quarter(i) for i in bg)
    else:
        bg = tuple(darker_quarter(i) for i in bg)

    foreground_color = '#' + ''.join(tuple(hex(int(i * 255))[2:4] for i in fg))
    background_color = '#' + ''.join(tuple(hex(int(i * 255))[2:4] for i in bg))

    return foreground_color, background_color


def lighter_quarter(color: int):
    return 255-int((255-color)/4)


def darker_quarter(color: int):
    return int(color/3)
