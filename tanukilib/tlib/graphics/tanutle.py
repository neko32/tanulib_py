from tlib.graphics.graphics import (
    gen_white_canvas,
    draw_line,
    persist_img,
    BGRA
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
        self._pen_down = True
        self._pen_size = 1
        self._pen_color = BGRA(0, 0, 0)

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

    def left(self, angle: int = 90) -> None:
        """turn left by specified angle"""
        if angle < 0 or angle > 360:
            raise Exception("angle must be 0 <= angle <= 360")
        self.angle -= angle
        if self.angle < 0:
            self.angle = 360 + self.angle

    def right(self, angle: int) -> None:
        """turn right by specified angle"""
        if angle < 0 or angle > 360:
            raise Exception("angle must be 0 <= angle <= 360")
        self.angle += angle
        if self.angle >= 360:
            self.angle = 360 - self.angle

    def forward(self, length: float) -> None:
        """move forward by the given length"""
        c_x, c_y = self.cur_coord.as_tuple2d()
        next_loc_x = int(c_x + length * cos(radians(self.angle)))
        next_loc_y = int(c_y + length * sin(radians(self.angle)))
        if self._pen_down:
            draw_line(
                a=self.cvs,
                st=(c_x, c_y),
                end=(next_loc_x, next_loc_y),
                line_thickness=self._pen_size,
                color=self._pen_color
            )
        self.cur_coord = Coordinate(next_loc_x, next_loc_y)

    def backward(self, length: float) -> None:
        """move backward by the given length"""
        c_x, c_y = self.cur_coord.as_tuple2d()
        next_loc_x = int(c_x - length * cos(radians(self.angle)))
        next_loc_y = int(c_y - length * sin(radians(self.angle)))
        if self._pen_down:
            draw_line(
                a=self.cvs,
                st=(c_x, c_y),
                end=(next_loc_x, next_loc_y),
                line_thickness=self._pen_size,
                color=self._pen_color
            )
        self.cur_coord = Coordinate(next_loc_x, next_loc_y)

    def set_x(self, x: int) -> None:
        """set xloc"""
        if x < 0 or x > self.width:
            raise Exception(f"x must be 0 <= x <= {self.width}")
        self.cur_coord = Coordinate(x, self.cur_coord.y)

    def set_y(self, y: int) -> None:
        """set yloc"""
        if y < 0 or y > self.height:
            raise Exception(f"y must be 0 <= y <= {self.height}")
        self.cur_coord = Coordinate(self.cur_coord.x, y)

    def reset_angle(self) -> None:
        """Reset angle to 0"""
        self.angle = 0

    def pen_up(self) -> None:
        """Set pen up. While pen up and when you forward/backword, no line is drawn."""
        self._pen_down = False

    def pen_down(self) -> None:
        """Set pen down. While pen down and when you forward/backword, line is drawn."""
        self._pen_down = True

    def pen_size(self, siz: int) -> None:
        """Set pen size."""
        self._pen_size = siz

    def pen_color(self, color: BGRA) -> None:
        """Set pen color."""
        self._pen_color = color

    def save(self, fpath: str) -> None:
        """Save the current canvas to specified fpath"""
        persist_img(self.cvs, fpath)
