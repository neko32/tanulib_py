from unittest import TestCase, main
from tlib.graphics.graphics import Rect
from tlib.math.math import Coordinate
from tlib.game.core import *
from functools import partial


class GameCoreTest(TestCase):

    def test_border_check(self):
        r = Rect(100, 100, 200, 200)
        get_c = partial(get_locstate_rect_coord_2d, rect=r)
        inside_p = Coordinate(130, 130)
        self.assertEqual(get_c(coord=inside_p), RectCoordLocState.INSIDE)
        self.assertTrue(is_within_rect(get_c(coord=inside_p)))
        edge_xleft = Coordinate(100, 200)
        edge_xright = Coordinate(300, 200)
        edge_ytop = Coordinate(200, 100)
        edge_ybottom = Coordinate(200, 300)
        edge_xy_topleft = Coordinate(100, 300)
        edge_xy_bottomright = Coordinate(300, 100)
        out_left = Coordinate(50, 120)
        out_right = Coordinate(301, 140)
        out_top = Coordinate(170, 99)
        out_bottom = Coordinate(170, 301)
        out_diagup = Coordinate(10, 10)
        out_diagbottom = Coordinate(310, 400)
        self.assertEqual(get_c(coord=edge_xleft), RectCoordLocState.AT_EDGE)
        self.assertEqual(get_c(coord=edge_xright), RectCoordLocState.AT_EDGE)
        self.assertEqual(get_c(coord=edge_ytop), RectCoordLocState.AT_EDGE)
        self.assertEqual(get_c(coord=edge_ybottom), RectCoordLocState.AT_EDGE)
        self.assertTrue(is_within_rect(get_c(coord=edge_ytop)))
        self.assertEqual(
            get_c(coord=edge_xy_topleft),
            RectCoordLocState.AT_EDGE
        )
        self.assertEqual(
            get_c(coord=edge_xy_bottomright),
            RectCoordLocState.AT_EDGE
        )
        self.assertEqual(get_c(coord=out_left), RectCoordLocState.OUTSIDE)
        self.assertEqual(get_c(coord=out_right), RectCoordLocState.OUTSIDE)
        self.assertEqual(get_c(coord=out_top), RectCoordLocState.OUTSIDE)
        self.assertEqual(get_c(coord=out_bottom), RectCoordLocState.OUTSIDE)
        self.assertEqual(
            get_c(coord=out_diagbottom),
            RectCoordLocState.OUTSIDE
        )
        self.assertEqual(get_c(coord=out_diagup), RectCoordLocState.OUTSIDE)
        self.assertFalse(is_within_rect(get_c(coord=out_diagup)))


if __name__ == "__main__":
    main()
