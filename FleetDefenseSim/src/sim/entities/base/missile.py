from abc import ABC
from src.sim.entities.kinematics import Position, Velocity
import json
from src.utils.get_data_path import get_data_dir_path
import os

class MissileType(Enum):
    AIM54 = 'aim54C.json'
    
class Missile(ABC):
    def __init__(self):
        self.thrust_curve: list[tuple] = None
        self.pos: Position = None
        self.vel: Velocity = None
        self.cross_sectional_area = None

    @classmethod
    def init_from_json():
        with open(os.path.join(get_data_dir_path, 'entities', 'missiles'))