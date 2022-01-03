from abc import ABC
from dataclasses import dataclass, field
from typing import List
from prototype.Classes.DataContainers.containers import Vector6DOF


@dataclass(slots=True)
class Generic3DDynamic(ABC):
    """ Abstract of object undergoing dyamics simulation """

    States: Vector6DOF = field(default_factory=Vector6DOF)  # states object is in now
    d_States: Vector6DOF = field(default_factory=Vector6DOF)  # change in states object will undergo on end of step
    Parts: List[object] = field(default_factory=List)  # a manifold of all elements
    # a list of objects, means it might as well just be sole engine flying around


@dataclass
class RocketModel:
# this just holds initial schematics for further customization by user and then sent to factory
    def __post_init__(self):
        """Should populate parts with a certain schematic in mind;
        rocket consists of
                            rocket engine(manifold),
                            fuel and oxidizer tanks,
                            fuselage,
                            optionally: controller, sensor suite, payload;
        therefore here we ask user to tell our factory what their rocket looks like;
        e.g. manifold of 4 RS-25 engines, one hydrogen tank and one oxygen tank,
        automatic controller(linked controller function),
        some kind of sensor model(added delay, saturation, etc.),
        and some payload,
        then fuselage is drawn as some primitive geometry over that
        """
        # Parts = [RS25x4Manifold(),LH2Tank(),LO2Tank(),SimpleAttitude(),TestSensorSuite(),Payload25kgCube(),]
        self.Parts.append(...)
    ...
# TODO: I probably spam too many classes...

