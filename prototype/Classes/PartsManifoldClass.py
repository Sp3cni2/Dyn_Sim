from dataclasses import dataclass, field
from typing import List

from prototype.Classes.DataContainers.containers import Vector3D
from prototype.Classes.methods.PartsManifoldMethods import manifold_shape, manifold_dimensions,\
                                                           manifold_barycenter, manifold_mass


@dataclass(slots=True)
class PartManifoldClass:

    """A manifold to store parts that can be equal distributed around central axis"""
    anchor: Vector3D = field(default_factory=Vector3D)  # relative to parent
    dimensions: Vector3D = field(default_factory=Vector3D)  # relative to parent
    cg_position: Vector3D = field(default_factory=Vector3D)  # relative to parent
    mass: float = field(default=None)

    PartsList: List = field(default_factory=List)

    def __post_init__(self):
        manifold_shape(self, rotation=0.0)
        manifold_dimensions(self)
        manifold_barycenter(self)
        manifold_mass(self)
