from dataclasses import dataclass, field

from .TensorInterface import InertiaTensor, Vector


@dataclass(slots=True)
class InertiaTensor3D(InertiaTensor):
    """ Inertia tensor in 3d space """
    xx: float = field(default=None)
    yy: float = field(default=None)
    zz: float = field(default=None)
    xy: float = field(default=None)
    xz: float = field(default=None)
    yz: float = field(default=None)


@dataclass(slots=True)
class Vector3DOF(Vector):

    """ 3 degrees of freedom tensor """

    u: float = field(default=None)
    x: float = field(default=None)

    w: float = field(default=None)
    z: float = field(default=None)

    q: float = field(default=None)
    theta: float = field(default=None)


@dataclass(slots=True)
class Vector6DOF(Vector):

    """ 6 degrees of freedom tensor """

    u: float = field(default=None)
    x: float = field(default=None)

    v: float = field(default=None)
    y: float = field(default=None)

    w: float = field(default=None)
    z: float = field(default=None)

    p: float = field(default=None)
    phi: float = field(default=None)

    q: float = field(default=None)
    theta: float = field(default=None)

    r: float = field(default=None)
    psi: float = field(default=None)


@dataclass(slots=True)
class TorqueVector3D(Vector):
    """ 3D vector of Torque. """
    l: float = field(default=None)
    m: float = field(default=None)
    n: float = field(default=None)


@dataclass(slots=True)
class ForceVector2D(Vector):
    """ 2D vector of Forces. """
    x: float = field(default=None)
    z: float = field(default=None)


@dataclass(slots=True)
class ForceVector3D(Vector):
    """ 3D vector of Forces. """
    x: float = field(default=None)
    y: float = field(default=None)
    z: float = field(default=None)


@dataclass(slots=True)
class CGVector3D(Vector):
    """ 3D vector of Center of Mass. """
    x: float = field(default=None)
    y: float = field(default=None)
    z: float = field(default=None)


@dataclass(slots=True)
class Vector3D(Vector):
    """ 3D vector """
    x: float = field(default=None)
    y: float = field(default=None)
    z: float = field(default=None)
