from abc import ABC
from src.sim.entities.base.radar import Radar
from enum import Enum


class ShipClass(Enum):
    Nimitz = "Nimitz"
    Ticonderoga = "Ticonderoga"
    Spruance = "Spruance"
    OliverHazardPerry = "OliverHazardPerry"


class Ship(ABC):
    def __init__(self):

        self.ship_class: ShipClass = ""
        self.name = ""
        self.displacement = ""
        self.max_speed = ""
        self.current_speed = ""
        self.radars: list[Radar]
