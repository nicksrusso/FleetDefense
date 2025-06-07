from src.sim.entities.base.missile import Missile, MissileType, MissileData
import os
import json


class AIM54(Missile):

    def __init__(self):
        self.missile_type = MissileType.AIM54

    @classmethod
    def from_json(cls):
        with open(os.path.join("path/to/data", "entities", "missiles", cls.missile_type.value), "r") as f:
            data = json.load(f)
        missile_data = MissileData(**data)
        return cls(missile_data)
