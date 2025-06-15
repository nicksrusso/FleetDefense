from abc import ABC
from FleetDefenseSim.src.sim.entities.models.radar import Radar
from enum import Enum
from FleetDefenseSim.src.utils.get_data_path import get_data_dir_path
import json
import os
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity
from pydantic import BaseModel


class ShipClass(Enum):
    Nimitz = "Nimitz.json"
    TICONDEROGA = "Ticonderoga.json"
    SPRUANCE = "Spruance.json"
    OLIVER_HAZARD_PERRY = "OliverHazardPerry.json"


class ShipData(BaseModel):
    name: str = None
    displacement: float = None
    max_speed_kn: float = None
    pos: Position = None
    vel: Velocity = None
    current_speed_kn = None
    radars: list[Radar] = None


def load_ship_names():
    return json.loads(os.path.join(get_data_dir_path(), "ships", "ship_names.json"))


class Ship(ABC):
    def __init__(self, ship_data: ShipData):
        for field in ship_data.__fields__:
            setattr(self, field, getattr(ship_data, field))
