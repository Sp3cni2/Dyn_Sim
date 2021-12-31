from dataclasses import dataclass, field
from typing import List

from prototype.Classes.methods.PartsManifoldMethods import manifold_shape, manifold_dimensions, manifold_barycenter
from prototype.Classes.PartsManifoldClass import PartManifoldClass


@dataclass
class ManifoldBuilder:

    @staticmethod
    def build(ItemList: List) -> PartManifoldClass:
        return PartManifoldClass(PartsList=ItemList)
