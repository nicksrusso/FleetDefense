from abc import ABC
from enum import Enum
from FleetDefenseSim.src.utils.get_data_path import get_data_dir_path
import json
import os
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity
from pydantic import BaseModel


class ShipClass(Enum):
    Nimitz = "Nimitz.json"
    Ticonderoga = "Ticonderoga.json"
    Spruance = "Spruance.json"
    Oliverhazardperry = "Oliverhazardperry.json"


class ShipData(BaseModel):
    name: str = None
    displacement: float = None
    max_speed_kn: float = None
    pos: Position = None
    vel: Velocity = None
    current_speed_kn: float = None
    # radars: list[Radar] = None # omitting for now, radars not implemented


def load_ship_names():
    with open(os.path.join(get_data_dir_path(), "entities", "ships", "ship_names.json"), "r") as f:
        ship_names = json.load(f)
    return {entry["class"]: entry["ships"] for entry in ship_names}


class Ship(ABC):
    def __init__(self, ship_data: ShipData):
        for field in ship_data.__fields__:
            setattr(self, field, getattr(ship_data, field))
