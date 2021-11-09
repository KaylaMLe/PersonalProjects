# TODO:
# deal with color warning? (line 18 but not 15?)
# animate r vector moving as theta and phi coordinates are altered
# animate theta and phi arcs
# create copy with physics labels conventions
from manim import *


class SphericalCoordinateSystem(Scene):
    def construct(self):
        origin = Dot([0, 0, 0])

        # creates vector r to display spherical coordinate components
        end_R = Dot([-2.5, -2.5, 0])
        vector_R = Arrow(origin.get_center(), end_R.get_center(), color=RED, buff=0)
        vector_R.z_index = 1

        label_R = Text("R", color=RED, font_size=48)
        label_R.next_to(vector_R, LEFT)
        self.play(Create(vector_R))
        self.wait(0.5)
        self.add(label_R)

        # creates x axis from the upper left of the screen to the bottom right
        end_X = Dot([-3, -3, 0])
        axis_X = Arrow(origin.get_center(), end_X.get_center(), buff=0)
        axis_X.z_index = 0
        # creates y axis from the bottom left of the screen to the upper right
        end_Y = Dot([3, -3, 0])
        axis_Y = Arrow(origin.get_center(), end_Y.get_center(), buff=0)
        axis_Y.z_index = 0
        # creates z axis from the bottom of the screen up
        end_Z = Dot([0, 3.1, 0])
        axis_Z = Arrow(origin.get_center(), end_Z.get_center(), buff=0)
        axis_Z.z_index = 0

        # create and position labels for axes
        label_X = Text("X", font_size=48)
        label_X.next_to(end_X, LEFT)
        label_Y = Text("Y", font_size=48)
        label_Y.next_to(end_Y, RIGHT)
        label_Z = Text("Z", font_size=48)
        label_Z.next_to(end_Z, UP)

        # animate axes creation and add labels
        self.play(Create(axis_X), Create(axis_Y), Create(axis_Z))
        self.bring_to_front(vector_R)
        self.wait(1)
        self.add(label_X, label_Y, label_Z)
        self.wait(0.5)