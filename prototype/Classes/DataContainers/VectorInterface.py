from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class GenericVector(Tensor):

    """A 1xM tensor"""

