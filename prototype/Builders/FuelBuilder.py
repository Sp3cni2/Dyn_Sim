from dataclasses import dataclass, field
from typing import List, Dict
from copy import deepcopy

from prototype.Builders.BuilderInterface import Builder
from prototype.Classes.FuelClass import FuelClass


@dataclass
class FuelBuilder(Builder):

    """ Builds fuel form specified."""

    blueprints: List[Dict] = field(default_factory=list[Dict])  # holds a list of all possible item to build
    items: List[FuelClass] = field(default_factory=list[FuelClass])

    def __post_init__(self):

        self.blueprints = Builder.load_item("./parts/Fuels.json")
        for item in self.blueprints:
            self.items.append(self._build(item))

    def _build(self, data: dict) -> FuelClass:
        item = FuelClass()
        item.name = data["name"]
        item.icon_ref = data["icon_ref"]
        item.density_oxid = data["density_oxid"]
        item.density_reduc = data["density_reduc"]
        item.k = data["k"]
        item.Mol = data["Mol"]
        item.ratio = data["ratio"]
        item.adiabatic_T = data["adiabatic_T"]
        item.adiabatic_P = data["adiabatic_P"]
        return item

    def get_item(self, name: str) -> FuelClass:
        if name not in [name.name for name in self.items]:
            raise ValueError("No such part available")
        return deepcopy([item for item in self.items if item.name == name].pop())
