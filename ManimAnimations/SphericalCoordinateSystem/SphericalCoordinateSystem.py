# TODO:
# adjust axes and stylize
# add spherical coordinate labels (mathematical)
# create copy with physics labels conventions
from manim import *


class SphericalCoordinateSystem(Scene):
    def construct(self):
        # creates z axis from the bottom of the screen up
        origin_Z = Dot([0, -3, 0])
        end_Z = Dot([0, 3, 0])
        axis_Z = Arrow(origin_Z.get_center(), end_Z.get_center())
        # creates y axis from the bottom left of the screen to the upper right
        origin_Y = Dot([-3, -3, 0])
        end_Y = Dot([3, 3, 0])
        axis_Y = Arrow(origin_Y.get_center(), end_Y.get_center())
        # creates x axis from the upper left of the screen to the bottom right
        origin_X = Dot([-3, 3, 0])
        end_X = Dot([3, -3, 0])
        axis_X = Arrow(origin_X.get_center(), end_X.get_center())

        self.play(Create(axis_X))
        self.play(Create(axis_Y))
        self.play(Create(axis_Z))