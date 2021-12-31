from prototype.Classes.DataContainers.TensorInterface import Vector


# ODE_STEP(equation, tn = 0.0, xn = X0, optional keyword arguments)

def rk45_step(function, tn: float, xn: Vector, **kw) -> Vector:
    """ solves n+1 step of ODE """
    h = kw['dt']  # is de facto a time step size
    k1 = function(t = tn        , X0 = xn               , **kw)
    k2 = function(t = tn + 0.5*h, X0 = xn + k1 * h * 0.5, **kw)
    k3 = function(t = tn + 0.5*h, X0 = xn + k2 * h * 0.5, **kw)
    k4 = function(t = tn + h    , X0 = xn + k3 * h      , **kw)
    dx = (k1+k2*2+k3*2+k4) * h/6

    return xn + dx




