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
        theta_coord2 = Text("θ, ", color=BLUE, font_size=48)
        phi_coord = Text("φ", color=GREEN, font_size=48)

        right_parenthesis.next_to(axis_z.arrow, LEFT)
        theta_coord.next_to(right_parenthesis, LEFT)
        r_coord.next_to(theta_coord, LEFT)
        left_parenthesis.next_to(r_coord, LEFT)
        # TODO: separate wait times into separate anim_group items?
        # animate axes creation and add labels
        self.add_anim(anim_group(anim_type.CREATE, 0.5, vector_r.arrow))
        self.add_anim(anim_group(anim_type.ADD, 0.5, vector_r.label))
        self.add_anim(anim_group(anim_type.CREATE, 0,
                      axis_x.arrow, axis_y.arrow, axis_z.arrow))

        # theta component
        theta = Arc(radius=2.89, start_angle=3.93, angle=1.13,
                    arc_center=origin, color=BLUE)
        label_theta = Text("θ", color=BLUE, font_size=36)
        label_theta.next_to(theta, DOWN)

        self.add_anim(anim_group(anim_type.FRONT, 0.5, vector_r.arrow))
        self.add_anim(anim_group(anim_type.ADD, 0.5,
                      axis_x.label, axis_y.label, axis_z.label))
        self.add_anim(anim_group(anim_type.TRANSFORM, 0,
                      vector_r.arrow, vector_rt.arrow))
        # TODO: how to allow multiple concurrent pairs of transforms?
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
