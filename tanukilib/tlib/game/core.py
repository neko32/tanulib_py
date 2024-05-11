from tlib.math.math import Coordinate
from tlib.graphics import Rect
from enum import Enum


class RectCoordLocState(Enum):
    """
    Indicate location state of specified coordinate against the specified rect.
    State is either of inside or outside or at edge
    """
    INSIDE = 1
    AT_EDGE = 0
    OUTSIDE = -1


def get_locstate_rect_coord_2d(rect: Rect, coord: Coordinate) -> RectCoordLocState:
    """Detect location state of the specified coordinate against the specified rect"""
    x_left = rect.loc_x
    x_right = rect.loc_x + rect.width
    y_top = rect.loc_y
    y_bottom = rect.loc_y + rect.height
    if coord.x > x_left and coord.x < x_right and coord.y > y_top and coord.y < y_bottom:
        return RectCoordLocState.INSIDE
    if (coord.x == x_left or coord.x == x_right) and coord.y >= y_top and coord.y <= y_bottom:
        return RectCoordLocState.AT_EDGE
    if coord.x >= x_left and coord.x <= x_right and (coord.y == y_top or coord.y == y_bottom):
        return RectCoordLocState.AT_EDGE
    else:
        return RectCoordLocState.OUTSIDE


def is_within_rect(state: RectCoordLocState) -> bool:
    """Convert RecordCoordLocState to bool if it's INSIDE or AT, true. else false"""
    return state.value >= 0
