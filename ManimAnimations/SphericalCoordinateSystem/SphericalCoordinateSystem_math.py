# uses mathematical (non-ISO) labelling conventions
from manim import *
from typing import Optional


# arrow with stored start and end coordinate arrays
class ptd_arrow:
    def __init__(self, end: any, start: any = [0, 0, 0]) -> None:
        self.start = start
        self.end = end
        self.arrow = Arrow(start=self.start, end=self.end)

    def set_buff(self, buffer: int) -> None:
        self.arrow.buff = buffer

    def set_layer(self, layerInd: int) -> None:
        self.arrow.set_z_index()(layerInd)


class SphericalCoordinateSystem(Scene):
    def construct(self):
        origin = [0, 0, 0]

        # creates x-axis from the upper left of the screen to the bottom right
        axis_x = ptd_arrow(start=origin, end=[-3, -3, 0])
        # creates y-axis from the bottom left of the screen to the upper right
        axis_y = ptd_arrow(start=origin, end=[3, -3, 0])
        # creates z axis from the bottom of the screen up
        axis_z = ptd_arrow(start=origin, end=[0, 3.1, 0])

        # create and position labels for axes
        label_X = Text("X", font_size=48)
        label_X.next_to(axis_x.end, LEFT)
        label_Y = Text("Y", font_size=48)
        label_Y.next_to(axis_y.end, RIGHT)
        label_Z = Text("Z", font_size=48)
        label_Z.next_to(axis_z.end, UP)

        # creates vector r to display spherical coordinate components
        vector_r = ptd_arrow(start=origin, end=[-2.5, -2.5, 0])
        vector_r.arrow.set_color(RED)
        vector_r.set_buff(0)
        vector_r.set_layer(1)

        label_R = Text("R", color=RED, font_size=36)
        label_R.next_to(vector_r, LEFT)

        vector_rt = ptd_arrow(start=origin, end=[1, -2.75, 0])
        vector_rt.arrow.set_color(RED)
        vector_rt.set_buff(0)

        label_RT = label_R.copy()
        label_RT.next_to(vector_rt, LEFT)

        # theta component
        theta = Arc(radius=2.89, start_angle=3.93, angle=1.13,
                    arc_center=origin, color=BLUE)
        label_theta = Text("θ", color=BLUE, font_size=36)
        label_theta.next_to(theta, DOWN)

        # coordinate form label
        left_parenthesis = Text("(", font_size=48)
        right_parenthesis = Text(")", font_size=48)
        r_coord = Text("R, ", color=RED, font_size=48)
        theta_coord = Text("θ", color=BLUE, font_size=48)
        theta_coord2 = Text("θ, ", color=BLUE, font_size=48)
        phi_coord = Text("φ", color=GREEN, font_size=48)

        right_parenthesis.next_to(axis_z, LEFT)
        theta_coord.next_to(right_parenthesis, LEFT)
        r_coord.next_to(theta_coord, LEFT)
        left_parenthesis.next_to(r_coord, LEFT)

        self.play(Create(vector_r))
        self.wait(0.5)
        self.add(label_R)
        self.wait(0.5)

        # animate axes creation and add labels
        self.play(Create(axis_x), Create(axis_y), Create(axis_z))
        self.bring_to_front(vector_r)
        self.wait(0.5)
        self.add(label_X, label_Y, label_Z)
        self.wait(0.5)
        self.play(Transform(vector_r, vector_rt), Transform(
            label_R, label_RT), Create(theta), Create(label_theta))
        self.play(Create(left_parenthesis), Create(r_coord),
                  Create(theta_coord), Create(right_parenthesis))
        self.wait(1)

        # coordinate label repositioning to add phi component
        phi_coord.next_to(right_parenthesis, LEFT)
        theta_coord2.next_to(phi_coord, LEFT)

        # vector r placeholder for phi translation
        r_theta = DashedLine(origin.get_center(), end_RT.get_center())
        self.add(r_theta)

        # phi translation
        end_RTP = Dot([1.64, 2.25, 0])
        vector_RTP = Arrow(origin.get_center(),
                           end_RTP.get_center(), color=RED, buff=0)
        label_RTP = label_R.copy()
        label_RTP.next_to(vector_RTP, RIGHT)

        # phi component
        phi = Arc(radius=3.1, start_angle=5.21, angle=1.89,
                  arc_center=[-0.5, 0., 0.], color=GREEN)
        label_phi = Text("φ", color=GREEN, font_size=36)
        label_phi.next_to(phi, RIGHT)

        self.play(Transform(vector_r, vector_RTP), Transform(
            label_R, label_RTP), Create(phi), Create(label_phi))
        self.play(FadeOut(left_parenthesis), FadeOut(
            r_coord), FadeOut(theta_coord))
        r_coord.next_to(theta_coord2, LEFT)
        left_parenthesis.next_to(r_coord, LEFT)
        self.play(Create(phi_coord), Transform(theta_coord, theta_coord2),
                  Create(r_coord), Create(left_parenthesis))
        self.wait(1)
