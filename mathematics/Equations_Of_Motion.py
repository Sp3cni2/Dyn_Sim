import numpy as np
from prototype.Classes.DataContainers.containers import \
    Vector3DOF, \
    Vector6DOF, \
    ForceVector2D, \
    ForceVector3D, \
    TorqueVector3D, \
    InertiaTensor3D


def three_dof_eom(t: float,
                  dt: float,
                  X0: Vector3DOF,
                  F: ForceVector2D = ForceVector2D(0.0,0.0),
                  T: float = 0.0,
                  I: float = 1.0,
                  G: float = 9.80665,
                  mass: float = 1.0) -> Vector3DOF:

    """ returns velocities for 3DOF equation of motion """

    dX = Vector3DOF()

    u, w  = X0.u, X0.w
    x, z  = X0.x, X0.z
    q     = X0.q
    theta = X0.theta

    X, Z = F.x*dt, F.z*dt
    M    = T*dt

    sthe, cthe = np.sin(theta), np.cos(theta)

    Tr_ZXe = np.array([[cthe , sthe],
                       [-sthe, cthe]])
    vect = np.array([u, w])
    [dX.x, dX.z] = np.matmul(Tr_ZXe, vect.T)

    dX.u = 1/mass *  X - q * w - G * sthe
    dX.w = 1/mass * -Z + q * u - G * cthe

    dX.q = 1/I * M
    dX.theta = q

    return dX


def six_dof_eom(t: float,
                dt: float,
                X0: Vector6DOF,
                F: ForceVector3D = ForceVector3D(0.0,0,0),
                T: TorqueVector3D = TorqueVector3D(0,0,0),
                I: InertiaTensor3D = InertiaTensor3D(1,1,1,0,0,0),
                Gravity: float = 9.80665,
                mass: float = 1.0) -> Vector6DOF:

    # container for results of the equation
    dX = Vector6DOF()
    """ returns velocities for 6DOF equation of motion """

    u,v,w = X0.u,X0.v,X0.w
    x,y,z = X0.x,X0.y,X0.z
    p,q,r = X0.p,X0.q,X0.r
    phi,theta,psi = X0.phi,X0.theta,X0.psi

    X,Y,Z = F.x*dt,F.y*dt,F.z*dt
    L,M,N = T.l*dt,T.m*dt,T.n*dt

    sphi, cphi = np.sin(phi), np.cos(phi)
    sthe, cthe = np.sin(theta), np.cos(theta)
    spsi, cpsi = np.sin(psi), np.cos(psi)
    tanthe = np.tan(theta)
    try:
        secthe = 1/cthe
    except ZeroDivisionError as E:
        # it is expected that zero division will happen in this equation
        secthe = np.sign(cthe) * float('inf')

    Tr_ZYXe = np.array([[cthe*cpsi,-cphi*spsi + sphi*sthe*cpsi, sphi*spsi + cphi*sthe*cpsi],
                        [cthe*spsi, cphi*cpsi + sphi*sthe*spsi,-sphi*cpsi + cphi*sthe*spsi],
                        [-sthe    , sphi*cthe                 , cphi*cthe                 ]])
    vect = np.array([u, v, w])
    [dX.x,dX.y,dX.z] = np.matmul(Tr_ZYXe,vect.T)

    dX.u = 1/mass *  X + r * v - q * w - Gravity * sthe
    dX.v = 1/mass *  Y + r * u - p * w - Gravity * sphi*cthe
    dX.w = 1/mass * -Z + q * u - p * v - Gravity * cphi*cthe

    dX.p = 1/I.xx * (L + (I.zz - I.yy) * q * r )
    dX.q = 1/I.yy * (M + (I.xx - I.zz) * p * r )
    dX.r = 1/I.zz * (N + (I.yy - I.xx) * p * q )

    dX.phi   = p + (q * sphi + r * cphi) * tanthe
    dX.theta =      q * cphi - r * sphi
    dX.psi   =     (q * sphi + r * cphi) * secthe

    return dX