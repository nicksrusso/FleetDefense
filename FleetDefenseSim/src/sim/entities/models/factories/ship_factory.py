import json
import os
from FleetDefenseSim.src.sim.entities.models.ship import ShipClass, Ship, ShipData, load_ship_names
from FleetDefenseSim.src.sim.entities.US.ships.Nimitz import Nimitz

from FleetDefenseSim.src.utils.get_data_path import get_data_dir_path


class ShipFactory:
    ship_classes = {ShipClass.Nimitz: Nimitz}

    # We don't want to instantiate 2 instances of a ship with the same name, create a set we can pull from
    @classmethod
    def __init_names(cls):
        if not hasattr(cls, "remaining_names"):
            ship_names_dict = load_ship_names()
            cls.remaining_names = {ship_class: set(ship_names_dict[ship_class.name.title()]) for ship_class in ShipClass}

    @classmethod
    def create_ship(cls, ship_class: ShipClass) -> Ship:
        cls.__init_names()
        # Load ship class data (fixed path from "missiles" to "ships")
        file_path = os.path.join(get_data_dir_path(), "entities", "ships", ship_class.value)
        with open(file_path, "r") as f:
            data = json.load(f)
        ship_data = ShipData(**data)

        # Create the ship instance
        ship_class_type = cls.ship_classes[ship_class]
        ship = ship_class_type(ship_data)

        # Assign a unique name
        if not cls.remaining_names[ship_class]:
            raise ValueError(f"No more unique names available for {ship_class.name}")
        name = cls.remaining_names[ship_class].pop()
        ship.name = name

        return ship
