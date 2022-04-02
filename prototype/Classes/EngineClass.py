from dataclasses import dataclass, field
from prototype.Classes.DataContainers.containers import CGVector3D, Vector3D

from prototype.Classes.TankClass import TankClass
from prototype.Classes.methods.engine_methods import engine_init


@dataclass(slots=True)
class EngineClass:
    # UI and 3d graphics properties
    icon_ref: str = field(default=None, repr=False)
    model_ref: str = field(default=None, repr=False)
    texture_ref: str = field(default=None, repr=False)

    name: str = field(default=None)
    mass: float = field(default=None, repr=False)
    fuel_mix: str = field(default=None, repr=False)
    flow_rate: float = field(default=None, repr=False)
    ratio: float = field(default=None, repr=False)
    design_pressure: float = field(default=None, repr=False)

    fuel_source: TankClass = field(default_factory=TankClass, init=False)

    origin: Vector3D = field(default_factory=Vector3D, repr=False)
    anchor: Vector3D = field(default_factory=Vector3D, repr=False)
    dimensions: Vector3D = field(default_factory=Vector3D, repr=False)
    cg_position: CGVector3D = field(default_factory=CGVector3D, repr=False)

    parent_part: object = field(default_factory=object, init=False, repr = False)

    # thrust generation properties:
    Ve: float = field(default=None, repr=False)
    Ae: float = field(default=None, repr=False)

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

    def connect_fuel_source(self, fuel_source) -> None:
        """Assign Tank being drained"""
        self.fuel_source = fuel_source

    def select_parent_part(self,parent_part: object) -> None:
        """Assign part engine gets welded onto."""
        self.parent_part = parent_part

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
