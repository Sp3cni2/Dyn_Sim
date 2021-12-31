from dataclasses import dataclass, field
from typing import List

from prototype.Classes.DataContainers.containers import Vector3D, CGVector3D
from prototype.Classes.PartsManifoldClass import PartManifoldClass


@dataclass
class FuselageClass:
    name: str = field(default=None)

    origin: Vector3D = field(default_factory=Vector3D)
    anchor: Vector3D = field(default_factory=Vector3D)
    dimensions: Vector3D = field(default_factory=Vector3D)  # sum of its parts
    cg_position: CGVector3D = field(default_factory=CGVector3D)
    mass: float = field(default=None)  # sum of its parts

    cross_area_front: float = field(default=None)
    cross_area_side: float = field(default=None)
    cross_area_top: float = field(default=None)
    center_of_pressure: Vector3D = field(default_factory=Vector3D)

    # TODO: This or an unknown range of Manifold classes...
    # this seems a bit better for sanity, manifold can be anything
    # but manifolds are going to be necessary

    Engines: List[PartManifoldClass] = field(default_factory=List[PartManifoldClass])
    Tanks: List[PartManifoldClass] = field(default_factory=List[PartManifoldClass])
    Payloads: List[PartManifoldClass] = field(default_factory=List[PartManifoldClass])
