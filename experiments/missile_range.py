from FleetDefenseSim.src.sim.entities.US.missiles.aim54C import AIM54
from FleetDefenseSim.src.sim.entities.kinematics import Position, Velocity
import numpy as np

if __name__ == "__main__":

    aim54 = AIM54.from_json()

    alts = np.arange(0, 12001, 3000)

    print()
