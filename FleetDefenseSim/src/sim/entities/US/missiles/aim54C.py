from FleetDefenseSim.src.sim.entities.models.missile import Missile, MissileData


class AIM54(Missile):
    def __init__(self, missile_data: MissileData):
        super().__init__(missile_data)
