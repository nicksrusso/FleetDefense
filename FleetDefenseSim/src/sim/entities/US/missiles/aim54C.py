from FleetDefenseSim.src.sim.entities.base.missile import Missile, MissileType, MissileData
import os
import json
from FleetDefenseSim.src.utils.get_data_path import get_data_dir_path


class AIM54(Missile):
    missile_type = MissileType.AIM54

    @classmethod
    def from_json(cls):
        with open(os.path.join(get_data_dir_path(), "entities", "missiles", cls.missile_type.value), "r") as f:
            data = json.load(f)
        missile_data = MissileData(**data)
        return cls(missile_data)
