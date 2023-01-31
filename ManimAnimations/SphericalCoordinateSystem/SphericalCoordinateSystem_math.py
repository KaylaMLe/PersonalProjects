# uses mathematical (non-ISO) labelling conventions
from manim import *
from ArrowAnim import *


# TODO: organize mobject creation and animation
# obj oriented creation but procedural animation?
class SphericalCoordinateSystem(Scene):
    def __init__(self) -> None:
        self.animationList = []

    def add_anim(self, animGroup: anim_group) -> None:
        self.animationList.append(animGroup)

    def construct(self) -> None:
        origin = [0, 0, 0]
        # creates x-axis from the upper left of the screen to the bottom right
        axis_x = ptd_arrow(end=[-3, -3, 0])
        axis_x.add_label('X', LEFT)
        # creates y-axis from the bottom left of the screen to the upper right
        axis_y = ptd_arrow(end=[3, -3, 0])
        axis_y.add_label('Y', RIGHT)
        # creates z axis from the bottom of the screen up
        axis_z = ptd_arrow(end=[0, 3.1, 0])
        axis_z.add_label('Z', UP)

        # creates vector r to display spherical coordinate components
        vector_r = ptd_arrow(end=[-2.5, -2.5, 0])
        vector_r.add_label('R', LEFT, 36, False)
        vector_r.arrow.set_color(RED)
        vector_r.arrow.buff = 0
        vector_r.set_layer(1)

        vector_rt = ptd_arrow(end=[1, -2.75, 0])
        vector_rt.add_label('R', LEFT, 36, False)
        vector_rt.arrow.set_color(RED)
        vector_rt.arrow.buff = 0

        # coordinate form label
        left_parenthesis = Text("(", font_size=48)
        right_parenthesis = Text(")", font_size=48)
        r_coord = Text("R, ", color=RED, font_size=48)
        theta_coord = Text("θ", color=BLUE, font_size=48)
        theta_coord2 = theta_coord.copy()
        phi_coord = Text("φ", color=GREEN, font_size=48)

        self.add_anim(next_to(axis_z.arrow, right_parenthesis, LEFT))
        self.add_anim(next_to(right_parenthesis, theta_coord, LEFT))
        self.add_anim(next_to(theta_coord, r_coord, LEFT))
        self.add_anim(next_to(r_coord, left_parenthesis, LEFT))

        # animate axes creation and add labels
        self.add_anim(anim_group(anim_type.CREATE, vector_r.arrow))
        self.add_anim(wait(0.5))
        self.add_anim(anim_group(anim_type.ADD, vector_r.label))
        self.add_anim(wait(0.5))
        self.add_anim(anim_group(anim_type.CREATE,
                      axis_x.arrow, axis_y.arrow, axis_z.arrow))

        # theta component
        theta = Arc(radius=2.89, start_angle=3.93, angle=1.13,
                    arc_center=origin, color=BLUE)
        label_theta = Text("θ", color=BLUE, font_size=36)
        self.add_anim(next_to(theta, label_theta, DOWN))

        self.add_anim(anim_group(anim_type.FRONT, vector_r.arrow))
        self.add_anim(wait(0.5))
        self.add_anim(anim_group(anim_type.ADD,
                      axis_x.label, axis_y.label, axis_z.label))
        self.add_anim(wait(0.5))
        self.add_anim(anim_group(anim_type.TRANSFORM,
                      vector_r.arrow, vector_rt.arrow, vector_r.label, vector_rt.label),
                      anim_group(anim_type.CREATE, theta, label_theta,
                                 left_parenthesis, r_coord, theta_coord, right_parenthesis))
        self.add_anim(wait(1))

        # coordinate label repositioning to add phi component
        self.add_anim(next_to(right_parenthesis, phi_coord, LEFT))
        self.add_anim(next_to(phi_coord, theta_coord2, LEFT))

        # vector r placeholder for phi translation
        r_theta = DashedLine(origin, vector_rt.end)
        self.add_anim(anim_group(anim_type.ADD, r_theta))

        # phi translation
        vector_rtp = ptd_arrow(end=[1.64, 2.25, 0])
        vector_rtp.arrow.buff = 0
        vector_rtp.add_label('R', RIGHT, 36, False)

        # phi component
        phi = Arc(radius=3.1, start_angle=5.21, angle=1.89,
                  arc_center=[-0.5, 0., 0.], color=GREEN)
        label_phi = Text("φ", color=GREEN, font_size=36)
        self.add_anim(next_to(phi, label_phi, RIGHT))

        self.add_anim(anim_group(anim_type.TRANSFORM, vector_r.arrow,
                      vector_rtp.arrow, vector_r.label, vector_rtp.label),
                      anim_group(anim_type.CREATE, phi, label_phi),
                      anim_group(anim_type.FADE, left_parenthesis, r_coord, theta_coord))
        self.add_anim(next_to(theta_coord2, r_coord, LEFT))
        left_parenthesis.next_to(r_coord, LEFT)
        self.play(Create(phi_coord), Transform(theta_coord, theta_coord2),
                  Create(r_coord), Create(left_parenthesis))
        self.add_anim(anim_group(anim_type.CREATE, phi_coord, r_coord, left_parenthesis),
                      anim_group(anim_type.TRANSFORM, theta_coord, theta_coord2))
        self.add_anim(wait(1))
