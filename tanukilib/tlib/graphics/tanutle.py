from tlib.graphics.graphics import (
    gen_white_canvas,
    draw_line,
    persist_img
)
from tlib.math import Coordinate
from math import cos, sin, radians


class Tanutle:
    """Imitates Turtle"""

    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        self.cvs = gen_white_canvas(w, h)
        self.cur_coord = self.home()
        self.angle = 0.
        self.command_buf = []
        self.velocity = 0.

    def home(self) -> Coordinate:
        """
        Set current coordinate pointer to home position.
        Home position is half of canvas width and half of canvas height
        """
        h_x = self.width // 2
        h_y = self.height // 2
        h_c = Coordinate(h_x, h_y)
        self.cur_coord = h_c
        return h_c

    def left(self, angle: int) -> None:
        """turn left by specified angle"""
        self.angle -= 90
        if self.angle < 0:
            self.angle = 360 + self.angle

    def forward(self, length: float) -> None:
        """move forward by the given length"""
        c_x, c_y = self.cur_coord.as_tuple2d()
        next_loc_x = int(c_x + length * cos(radians(self.angle)))
        next_loc_y = int(c_y + length * sin(radians(self.angle)))
        draw_line(self.cvs, (c_x, c_y), (next_loc_x, next_loc_y))
        self.cur_coord = Coordinate(next_loc_x, next_loc_y)

    def save(self, fpath: str) -> None:
        """Save the current canvas to specified fpath"""
        persist_img(self.cvs, fpath)
