from FleetDefenseSim.src.sim.entities.models.ship import Ship, ShipData


class Nimitz(Ship):
    def __init__(self, ship_data: ShipData):
        super().__init__(ship_data)
