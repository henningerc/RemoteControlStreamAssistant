from typing import Dict, List

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QColor
from PySide2.QtCore import Qt

from Controller.StatusLamp import StatusLamp


class StatusWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lamps: List[StatusLamp] = []

    def paintEvent(self, e):
        self.resize(len(self.lamps) * 30, 30)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        i = 0
        for lamp in self.lamps:
            self.draw_circle(painter, i, lamp.get_color())
            i += 1

    def draw_circle(self, painter: QPainter, position, color):
        col = QColor(*tuple(int(color[i:i + 2], 16) for i in (1, 3, 5)))
        painter.setBrush(col)
        painter.setPen(col)
        painter.drawEllipse(position * 30 + 2, 2, 25, 25)

    def register_lamp(self, lamp: StatusLamp):
        self.lamps.append(lamp)
