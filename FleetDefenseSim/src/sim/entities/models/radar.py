from abc import ABC


class Radar(ABC):
    """Abstract base class for all radars"""

    def __init__(self):
        self.frequency = 0.0
        self.transmit_power = 0.0
        self.pulse_width = 0.0
