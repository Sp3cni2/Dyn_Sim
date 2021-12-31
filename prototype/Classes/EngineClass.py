from dataclasses import dataclass, field
from prototype.Classes.DataContainers.containers import CGVector3D, Vector3D

from prototype.Classes.TankClass import TankClass
from prototype.Classes.methods.engine_methods import engine_init


@dataclass(slots=True)
class EngineClass:
    # UI and 3d graphics properties
    icon_ref: str = field(default=None)
    model_ref: str = field(default=None)
    texture_ref: str = field(default=None)

    Tank: TankClass = field(default_factory=TankClass, init=False)

    name: str = field(default=None)
    mass: float = field(default=None)
    fuel_mix: str = field(default=None)
    flow_rate: float = field(default=None)
    ratio: float = field(default=None)
    design_pressure: float = field(default=None)

    origin: Vector3D = field(default_factory=Vector3D)
    anchor: Vector3D = field(default_factory=Vector3D)
    dimensions: Vector3D = field(default_factory=Vector3D)
    cg_position: CGVector3D = field(default_factory=CGVector3D)

    parent: object = field(default_factory=object)

    # thrust generation properties:
    Ve: float = field(default=None)
    Ae: float = field(default=None)

    @property
    def offset(self) -> float:
        return self.origin + self.anchor

    @property
    def fuel_flow(self) -> float:
        """Flow in Kg per second"""
        return self.flow_rate / (self.Tank.Fuel.ratio + 1)

    @property
    def oxidizer_flow(self) -> float:
        """Flow in Kg per second"""
        return self.fuel_flow * self.Tank.Fuel.ratio

    @property
    def _fuel_present(self, tick_length: float = 1.0) -> bool:
        """Is fuel available for another tick."""
        return not any([self.Tank.available_fuel <= self.fuel_flow * tick_length,
                        self.Tank.available_oxidizer <= self.oxidizer_flow * tick_length])

    @property
    def generate_thrust(self, tick_length: float = 1.0) -> float:
        return (self.Ve * self.flow_rate + self._pressure_part) * self._fuel_present * tick_length

    @property
    def _pressure_part(self, pa: float = 101325.15):
        return self.Ae * (self.Tank.Fuel.adiabatic_P * 101325.15 - pa)

    def connect_tank(self, Tank) -> None:
        """Assign Tank being drained"""
        self.Tank = Tank

    def setup_engine(self, ratio):
        self.Ve, self.Ae = engine_init(self.design_pressure,
                                       self.Tank.Fuel.k, self.Tank.Fuel.Mol,
                                       self.Tank.Fuel.adiabatic_T, self.Tank.Fuel.adiabatic_P*101325.15,
                                       self.flow_rate,
                                       ratio=ratio, Pe=101325.15)

    def flow_drain_tick(self, tick_length: float = 1.0) -> None:
        """Drains from tanks, tick length dependant"""
        self.Tank.available_fuel -= self.fuel_flow * tick_length
        self.Tank.available_oxidizer -= self.oxidizer_flow * tick_length
