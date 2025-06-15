from abc import ABC


class JetEngine(ABC):
    """Abstract base class for all jet entities in the simulation."""

    def __init__(self):
        self.fuel_burn_rate = 0.0  # Fuel burn rate in kg/s
        self.thrust = 0.0  # Thrust produced by the engine in Newtons
        self.throttle = 0.0  # Throttle setting (0.0 to 1.0)
