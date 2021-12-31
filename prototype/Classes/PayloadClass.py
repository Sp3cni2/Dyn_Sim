from dataclasses import dataclass, field
from prototype.Classes.DataContainers.containers import CGVector3D, Vector3D


@dataclass(slots=True)
class PayloadClass:
    name: str = field(default=None)
    origin: Vector3D = field(default_factory=Vector3D)
    anchor: Vector3D = field(default_factory=Vector3D)
    dimensions: Vector3D = field(default_factory=Vector3D)
    cg_position: CGVector3D = field(default_factory=CGVector3D)
    mass: float = field(default=None)
    shape: str = field(default=None)

    @property
    def offset(self):
        return self.origin + self.anchor