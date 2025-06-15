from FleetDefenseSim.src.sim.entities.models.missile import MissileType, MissileData, Missile
from FleetDefenseSim.src.sim.entities.US.missiles.aim54C import AIM54
import json
import os
from FleetDefenseSim.src.utils.get_data_path import get_data_dir_path


class MissileFactory:
    missile_classes = {
        MissileType.AIM54: AIM54,
    }
    MISSILE_FILES = {
        MissileType.AIM54: "aim54C.json",
    }

    @staticmethod
    def create_missile(missile_type: MissileType) -> Missile:
        file_path = os.path.join(get_data_dir_path(), "entities", "missiles", MISSILE_FILES[missile_type])
        with open(file_path, "r") as f:
            data = json.load(f)
        missile_data = MissileData(**data)
        missile_class = MissileFactory.missile_classes[missile_type]
        return missile_class(missile_data)
