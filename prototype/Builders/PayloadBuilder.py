from dataclasses import dataclass, field
from typing import List, Dict
from copy import deepcopy

from prototype.Builders.BuilderInterface import Builder
from prototype.Classes.PayloadClass import PayloadClass


@dataclass
class PayloadBuilder(Builder):

    """ Builds engine form specified."""

    blueprints: List[Dict] = field(default_factory=list[Dict])  # holds a list of all possible item to build
    items: List[PayloadClass] = field(default_factory=list[PayloadClass])

    def __post_init__(self):

        self.blueprints = Builder.load_item("./parts/Payloads.json")
        for item in self.blueprints:
            self.items.append(self._build(item))

    def _build(self, data: dict) -> PayloadClass:
        item = PayloadClass()
        item.name = data["name"]
        item.mass = data["mass"]
        item.shape = data["shape"]
        item.origin.update(data["origin"])
        item.anchor.update(data["anchor"])
        item.dimensions.update(data["dimensions"])
        item.cg_position.update(data["cg_position"])
        return item

    def get_item(self, name: str) -> PayloadClass:
        if name not in [name.name for name in self.items]:
            raise ValueError("No such part available")
        return deepcopy([item for item in self.items if item.name == name].pop())
