from abc import ABC
from FleetDefenseSim.src.sim.entities.models.radar import Radar
from enum import Enum
from FleetDefenseSim.src.utils.get_data_path import get_data_dir_path
import json
import os
from collections import namedtuple
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity

ShipData = namedtuple("ShipData", ["displacement", "max_speed"])


class ShipClass(Enum):
    Nimitz = ShipData(100000, 40)
    TICONDEROGA = ShipData(9600, 32)
    SPRUANCE = ShipData(8000, 32)
    OLIVER_HAZARD_PERRY = ShipData(4100, 29)


def load_ship_names():
    return json.loads(os.path.join(get_data_dir_path(), "ships", "ship_names.json"))


class Ship(ABC):
    def __init__(self):

        self.ship_class: ShipClass = ""
        self.name = ""
        self.displacement = ""
        self.max_speed = ""
        self.pos: Position = None
        self.vel: Velocity = None
        self.current_speed_kn = None
        self.radars: list[Radar]
