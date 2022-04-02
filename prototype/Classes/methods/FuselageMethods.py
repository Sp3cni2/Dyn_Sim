import numpy as np
from statistics import harmonic_mean


def cross_sections(cls):

    pass


def barycenter(cls):

    cls.cg_position.x = harmonic_mean([part.cg_position.x for part in cls.PartsList],
                                      [part.mass for part in cls.PartsList])
    cls.cg_position.y = harmonic_mean([part.cg_position.y for part in cls.PartsList],
                                      [part.mass for part in cls.PartsList])
    cls.cg_position.z = harmonic_mean([part.cg_position.z for part in cls.PartsList],
                                      [part.mass for part in cls.PartsList])


def inertia(cls):
    pass