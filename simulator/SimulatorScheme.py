from abc import ABC, abstractmethod


class ScenarioABC(ABC):

    """Simulate our rocket in some scenario."""

    @abstractmethod
    def run(self, sim_type):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_model(self, model):
        pass

    @abstractmethod
    def reset_model(self):
        pass

    @abstractmethod
    def _clear_model(self):
        pass
