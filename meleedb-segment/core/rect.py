#!/usr/bin/python
import numpy as np


class Rect:

    def __init__(self, top, left, height, width):
        self.top = int(top)
        self.left = int(left)
        self.height = int(height)
        self.width = int(width)

    def __str__(self):
        return '{height}x{width}+{top}+{left}'.format(**self.__dict__)

    def __repr__(self):
        return '{height}x{width}+{top}+{left}'.format(**self.__dict__)

    def __and__(self, other):
        """Return the intersection of ''self'' and ''other''.
        """
        overlap_left = max(self.left, other.left)
        overlap_top = max(self.top, other.top)
        overlap_right = min(self.left + self.width, other.left + other.width)
        overlap_bottom = min(self.top + self.height, other.top + other.height)

        if overlap_left > overlap_right or overlap_top > overlap_bottom:
            return None
        else:
            return Rect(overlap_top,
                        overlap_left,
                        overlap_bottom - overlap_top,
                        overlap_right - overlap_left)

    def to_mask(self, height, width):
        mask = np.zeros((height, width, 3))

        mask[self.top:(self.top + self.height + 1),
             self.left:(self.left + self.width + 1)] = (1, 1, 1)

        return mask.astype(np.uint8)
