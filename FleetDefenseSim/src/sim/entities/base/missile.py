from abc import ABC
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity
from enum import Enum
from pydantic import BaseModel
from typing import List, Tuple


class MissileType(Enum):
    AIM54 = "aim54C.json"


class MissileData(BaseModel):
    thrust_curve: List[Tuple[float, float]] = None
    pos: Position = None
    vel: Velocity = None
    cross_sectional_area: float = None
    burn_time: float = None
    launch_mass: float = None
    propellant_mass: float = None


class Missile(ABC):
    def __init__(self, missile_data: MissileData):
        for field in missile_data.__fields__:
            setattr(self, field, getattr(missile_data, field))
