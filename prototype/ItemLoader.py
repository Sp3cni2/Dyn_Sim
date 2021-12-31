from prototype.Builders.PayloadBuilder import PayloadBuilder
from prototype.Builders.TankBuilder import TankBuilder
from prototype.Builders.FuelBuilder import FuelBuilder
from prototype.Builders.EngineBuilder import EngineBuilder
from prototype.Builders.ManifoldBuilder import ManifoldBuilder

from prototype.Classes.FuselageClass import FuselageClass

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":

    #  globals initialization stage:

    PB = PayloadBuilder()
    TB = TankBuilder()
    FB = FuelBuilder()
    EB = EngineBuilder()
    MB = ManifoldBuilder()

    print(FB.names)
    print(EB.names)

    T1 = TB.get_item("T1")
    T1.apply_fuel(FB.get_item("LH2-LOX x600"))
    T1.set_volumes()

    ManifoldEngines = MB.build([EB.get_item("RS-25"), EB.get_item("RS-25"), EB.get_item("RS-25")])

    print(ManifoldEngines.anchor)

    pass
