from abc import ABC
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity
from enum import Enum
from pydantic import BaseModel
from typing import List, Tuple


class FlightDeckType(Enum):
    NimitzDeck = "nimitz_deck.json"
    TicoderogaDeck = "ticonderoga_deck.json"


class FlightDeck(BaseModel):
    pass


class FlightDeck(ABC):
    def __init__():
        pass


class HeloDeck(FlightDeck):
    def __init__():
        pass


class CVDeck(FlightDeck):
    def __init__(self):
        self.helo_deck = HeloDeck()
