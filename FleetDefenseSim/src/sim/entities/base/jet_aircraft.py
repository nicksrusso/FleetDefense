from abc import ABC


class JetAircraft(ABC):
    """Abstract base class for all jet entities in the simulation."""

    def __init__(self):
        self.pos = None  # Position of the jet
        self.vel = None  # Velocity of the jet
        self.sensors = []
