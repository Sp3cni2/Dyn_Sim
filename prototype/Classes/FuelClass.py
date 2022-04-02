from dataclasses import dataclass, field


@dataclass(slots=True)
class FuelClass:

    """Fuel is a predefined mixture of oxidizing agent and reducing agent with thermodynamic properties."""

    icon_ref: str = field(default=None, repr=False)

    name: str = field(default=None)
    density_oxid: float = field(default=None, repr=False)
    density_reduc: float = field(default=None, repr=False)
    k: float = field(default=None, repr=False)
    Mol: float = field(default=None, repr=False)
    ratio: float = field(default=None, repr=False)
    adiabatic_T: float = field(default=None, repr=False)
    adiabatic_P: float = field(default=None, repr=False)
