from abc import ABC, abstractmethod
from dataclasses import dataclass
from copy import deepcopy
import json


@dataclass
class Builder(ABC):

    @abstractmethod
    def _build(self, name: str) -> object:
        raise NotImplementedError

    @property
    def names(self):
        """Return list of things this builder can create"""
        return [(n, item["name"]) for n, item in enumerate(self.blueprints)]

    @staticmethod
    def load_item(file: str):
        with open(file, 'rt') as file:
            return Builder.unshell(json.load(file))

    @staticmethod
    def unshell(item: dict) -> list:
        key = [key for key in item.keys()]
        return item[key[0]]

    @staticmethod
    def get_item(self, name: str) -> object:
        raise NotImplementedError