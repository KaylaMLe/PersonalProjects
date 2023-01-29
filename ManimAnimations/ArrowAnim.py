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


class anim_type(Enum):
    ADD = 1
    CREATE = 2
    TRANSFORM = 3


class anim_group:
    def __init__(self, anim: anim_type, delaySeconds: int, *mobjects: Mobject) -> None:
        self.anim = anim
        self. delaySeconds = delaySeconds
        self.mobjects = mobjects
