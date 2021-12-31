from dataclasses import dataclass, field
from typing import List, Dict
from copy import deepcopy

from prototype.Builders.BuilderInterface import Builder
from prototype.Classes.EngineClass import EngineClass


@dataclass
class EngineBuilder(Builder):

    """ Builds engine form specified."""

    blueprints: List[Dict] = field(default_factory=list[Dict])  # holds a list of all possible item to build
    items: List[EngineClass] = field(default_factory=list[EngineClass])  # all build items

    def __post_init__(self):

        self.blueprints = Builder.load_item("./parts/Engines.json")
        for item in self.blueprints:
            self.items.append(self._build(item))

    def _build(self, data: dict) -> EngineClass:
        item = EngineClass()
        item.name = data["name"]
        item.icon_ref = data["icon_ref"]
        item.model_ref = data["model_ref"]
        item.texture_ref = data["texture_ref"]
        item.mass = data["mass"]
        item.fuel_mix = data["fuel_mix"]
        item.ratio = data["ratio"]
        item.flow_rate = data["flow_rate"]
        item.design_pressure = data["design_pressure"]
        item.origin.update(data["origin"])
        item.anchor.update(data["anchor"])
        item.dimensions.update(data["dimensions"])
        item.cg_position.update(data["cg_position"])
        return item

    def get_item(self, name: str) -> EngineClass:
        if name not in [name.name for name in self.items]:
            raise ValueError("No such part available")
        return deepcopy([item for item in self.items if item.name == name].pop())
