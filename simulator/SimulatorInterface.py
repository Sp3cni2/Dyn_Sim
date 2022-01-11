from abc import ABC, abstractmethod


class ScenarioInterface(ABC):

    """Simulate our rocket in some scenario."""

    @abstractmethod
    def run(self, sim_type):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_model(self, model):
        """Sets initial model variables."""
        pass

    @abstractmethod
    def reset_model(self):
        """Used to set model variables to states at beginning of simulation."""
        pass

    @abstractmethod
    def _clear_model(self):
        """Clears everything about model."""
        pass
