from manim import *
from numpy import ndarray


# arrow with stored start and end coordinate arrays
class ptd_arrow:
    def __init__(self, end: any, start: any = [0, 0, 0]) -> None:
        self.start = start
        self.end = end
        self.arrow = Arrow(start=self.start, end=self.end)

    def set_layer(self, layerInd: int) -> None:
        self.arrow.set_z_index(layerInd)

    def add_label(self, text: str, pos: ndarray, fontSize: int = 48, nextToEnd: bool = True) -> None:
        self.label = Text(text, font_size=fontSize)
        if nextToEnd:
            self.label.next_to(self.end, pos)
        else:
            self.label.next_to(self.arrow, pos)


# different methods to add an object to a scene
class anim_type(Enum):
    # objects appear without an animation
    ADD = 1
    # objects' creation is animated
    # the exact animation depends on the type of object
    CREATE = 2
    # mobjects are morphed into the next mobject in the group
    # the number of mobjects passed must be even
    TRANSFORM = 3
    # fades out mobjects
    FADE = 4
    # an object is brought to the top layer of a scene
    FRONT = 5
    # a delay between animations
    WAIT = 6


# groups together animation type and delay after animation with the relevant mobjects
class anim_group:
    def __init__(self, anim: anim_type, *mobjects: Mobject, waitSeconds: float = 0) -> None:
        self.anim = anim

        if anim == anim_type.WAIT:
            self.time = waitSeconds
        else:
            self.mobjects = Group(mobjects)
