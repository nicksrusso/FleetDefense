from abc import ABC
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity
from enum import Enum
from pydantic import BaseModel


class FlightDeckType(Enum):
    VF = "vf.json"
