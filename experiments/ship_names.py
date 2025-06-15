from FleetDefenseSim.src.sim.entities.models.factories.ship_factory import ShipFactory
from FleetDefenseSim.src.sim.entities.models.ship import ShipClass

nimitz1 = ShipFactory.create_ship(ShipClass.Nimitz)
nimitz2 = ShipFactory.create_ship(ShipClass.Nimitz)

print()
