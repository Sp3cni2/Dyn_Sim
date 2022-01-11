from dataclasses import dataclass, field
from typing import List, Callable
from prototype.Classes.DataContainers.TensorInterface import Vector
from simulator.SimulatorInterface import ScenarioInterface


@dataclass
class BasicSim(ScenarioInterface):

    """Defines a standard N step simulation."""

    model: object = field(init=False, repr=False)  # holds model parameters object

    eom: Callable = field(init=False, default_factory=Callable)
    solver: Callable = field(init=False, default_factory=Callable)
    state_vector: Vector = field(init=False, default_factory=Vector)

    output: List = field(init=False, repr=False)

    def run(self, sim_setup):
        n = 0
        while n <= sim_setup.sim_end:

            kws = {
                "F": 0.0,
                "T": 0.0,
                "I": 1.0,
                "G": 0.0,
                "dt": 0.1,
                "mass": 1.0}
            tn = 0.0  # don't use this
            self.output.append(self.solver(self.eom, tn, self.state_vector, **kws))
            n += sim_setup.sim_step
        pass

    def reset(self):
        pass

    def set_model(self, model):
        pass

    def reset_model(self):
        pass

    def _clear_model(self):
        pass
