from dataclasses import dataclass, field


@dataclass(slots=True)
class FuelClass:
    icon_ref: str = field(default=None)

    name: str = field(default=None)
    density_oxid: float = field(default=None)
    density_reduc: float = field(default=None)
    k: float = field(default=None)
    Mol: float = field(default=None)
    ratio: float = field(default=None)
    adiabatic_T: float = field(default=None)
    adiabatic_P: float = field(default=None)
