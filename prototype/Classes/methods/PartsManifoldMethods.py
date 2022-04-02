import numpy as np
from statistics import harmonic_mean


def manifold_shape(cls, rotation=0.0) -> None:

    """defines positions of parts around some central axis, for balance purposes."""

    n = len(cls.PartsList)  # how many parts in manifold
    segment = np.pi * 2 / n
    if not n < 2:
        # takes widest element in manifold for separation radius
        # consider allowing custom radius
        radius = max([part.dimensions.z for part in cls.PartsList])
    else:
        radius = 0.0

    for i, part in enumerate(cls.PartsList):
        part.anchor.update([0,
                            np.cos(segment * i + rotation) * radius,
                            np.sin(segment * i + rotation) * radius])


def manifold_dimensions(cls):

    """Finds dimensions of manifold."""
    # correctly sum dimensions of parts.

    cls.dimensions.x = max([dims.dimensions.x for dims in cls.PartsList])
    cls.dimensions.y = max([dims.dimensions.y for dims in cls.PartsList])
    if len(cls.PartsList) >= 2:
        cls.dimensions.y += min([dims.dimensions.y for dims in cls.PartsList])
    cls.dimensions.z = max([dims.dimensions.z for dims in cls.PartsList])
    if len(cls.PartsList) >= 2:
        cls.dimensions.z += min([dims.dimensions.z for dims in cls.PartsList])


def manifold_barycenter(cls):

    """Finds weighted center of a group of points."""

    cls.cg_position.x = harmonic_mean([part.cg_position.x for part in cls.PartsList],
                                      [part.mass for part in cls.PartsList])
    cls.cg_position.y = harmonic_mean([part.cg_position.y for part in cls.PartsList],
                                      [part.mass for part in cls.PartsList])
    cls.cg_position.z = harmonic_mean([part.cg_position.z for part in cls.PartsList],
                                      [part.mass for part in cls.PartsList])


def manifold_mass(cls):
    cls.mass = sum([part.mass for part in cls.PartsList])
