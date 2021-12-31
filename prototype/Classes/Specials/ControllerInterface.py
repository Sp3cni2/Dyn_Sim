from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class ControllerClass(ABC):
    """controller design"""

    @abstractmethod
    def get_state_error(self):
        raise NotImplementedError

    @abstractmethod
    def get_control_output(self):
        raise NotImplementedError
