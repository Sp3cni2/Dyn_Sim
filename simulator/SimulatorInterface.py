from abc import ABC, abstractmethod


class ScenarioInterface(ABC):

    """Interfacing of the simulation scenario."""

    @abstractmethod
    def run(self, sim_type):
        """Runs simulation."""
        raise NotImplementedError

    @abstractmethod
    def reset(self) -> None:
        """Resets simulation to initial state."""
        raise NotImplementedError

    @abstractmethod
    def set_model(self, model) -> None:
        """Sets initial model conditions."""
        raise NotImplementedError

    @abstractmethod
    def reset_model(self) -> None:
        """Resets model states to initial conditions."""
        raise NotImplementedError

    @abstractmethod
    def _clear_model(self) -> None:
        """Clears everything about model. Basically deletes any references of model in simulation.
        At least that is the concept right now."""
        raise NotImplementedError
