from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class ObserverClass(ABC):

    """Container class for sensor suite."""

    @abstractmethod
    def get_states(self):
        raise NotImplementedError
