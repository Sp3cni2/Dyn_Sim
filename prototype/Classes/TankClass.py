from dataclasses import dataclass, field

from prototype.Classes.DataContainers.containers import CGVector3D, Vector3D
from prototype.Classes.FuelClass import FuelClass


@dataclass(slots=True)
class TankClass:

    name: str = field(default=None)
    shape: str = field(default=None, repr=False)
    mass_empty: float = field(default=None, repr=False)
    volume_efficiency: float = field(default=None, repr=False)
    available_fuel: float = field(default=None, init=False, repr=False)
    available_oxidizer: float = field(default=None, init=False, repr=False)

    Fuel: FuelClass = field(default_factory=FuelClass)

    origin: Vector3D = field(default_factory=Vector3D, repr=False)  # this is where object origin is placed
    anchor: Vector3D = field(default_factory=Vector3D, repr=False)  # relative to parent
    dimensions: Vector3D = field(default_factory=Vector3D, repr=False)
    cg_position: CGVector3D = field(default_factory=CGVector3D, repr=False)

    @property
    def offset(self) -> Vector3D:
        return self.origin + self.anchor

    @property
    def total_volume(self) -> float:
        """assumes it's a cylindrical shape"""
        return self.dimensions.x * self.dimensions.y * self.dimensions.z * 3.141592 / 4 * 1e3

    @property
    def fuel_volume(self) -> float:
        """Calculates volume of fuel."""
        return self.volume_efficiency * self.total_volume / (1 + self.Fuel.ratio)

    @property
    def fuel_mass(self) -> float:
        """Calculates mass of fuel."""
        return self.fuel_volume * self.Fuel.density_reduc

    @property
    def oxidizer_volume(self) -> float:
        """Calculates volume of oxidizer."""
        return self.volume_efficiency * self.total_volume * self.Fuel.ratio / (1 + self.Fuel.ratio)

    @property
    def oxidizer_mass(self) -> float:
        """calculates mass of oxidizer."""
        return self.oxidizer_volume * self.Fuel.density_oxid

    def apply_fuel(self, Fuel: FuelClass) -> None:
        """Assign Fuel to a Tank."""
        self.Fuel = Fuel

    def set_volumes(self) -> None:
        """Sets initial fuel values."""
        self.available_fuel = self.fuel_mass
        self.available_oxidizer = self.oxidizer_mass
