from dataclasses import dataclass, field
from typing import List, Dict
from copy import deepcopy

from prototype.Builders.BuilderInterface import Builder
from prototype.Classes.TankClass import TankClass


@dataclass
class TankBuilder(Builder):

    """ Builds engine form specified."""

    blueprints: List[Dict] = field(default_factory=list[Dict])  # holds a list of all possible item to build
    items: List[TankClass] = field(default_factory=list[TankClass])

    def __post_init__(self):

        self.blueprints = Builder.load_item("./parts/Tanks.json")
        for item in self.blueprints:
            self.items.append(self._build(item))

    def _build(self, data: dict) -> TankClass:
        item = TankClass()
        item.name = data["name"]
        item.mass_empty = data["mass_empty"]
        item.shape = data["shape"]
        item.volume_efficiency = data["efficiency"]
        item.origin.update(data["origin"])
        item.anchor.update(data["anchor"])
        item.dimensions.update(data["dimensions"])
        item.cg_position.update(data["cg_position"])
        return item

    def get_item(self, name: str) -> TankClass:
        if name not in [name.name for name in self.items]:
            raise ValueError("No such part available")
        return deepcopy([item for item in self.items if item.name == name].pop())
