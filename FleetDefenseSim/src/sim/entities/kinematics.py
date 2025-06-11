from collections import namedtuple
import numpy as np
from scipy.integrate import solve_ivp


Position = namedtuple("pos", ["x", "y", "z"])
Velocity = namedtuple("vel", ["vx", "vy", "vz"])

# Physical constants
R_e = 6371000.0  # Earth's radius in meters
GM = 3.986004418e14  # Gravitational parameter in m^3/s^2
RHO_0 = 1.225  # Sea-level air density in kg/m^3
H = 8400.0  # Scale height in meters


def derivatives(t, state, Cd, A, mass):
    """
    Compute the derivatives of the state vector for ODE integration.

    Parameters:
    - t: Time (s)
    - state: State vector [x, y, z, vx, vy, vz]
    - Cd: Drag coefficient (dimensionless)
    - A: Cross-sectional area (m^2)
    - mass: Mass of the object (kg)

    Returns:
    - List of derivatives [vx, vy, vz, ax, ay, az]
    """
    x, y, z, vx, vy, vz = state

    # Distance from Earth's center
    r = np.sqrt(x**2 + y**2 + z**2)

    # Altitude above Earth's surface
    h = max(r - R_e, 0)  # Ensure non-negative altitude

    # Air density using exponential model
    rho = RHO_0 * np.exp(-h / H)

    # Speed (magnitude of velocity)
    v = np.sqrt(vx**2 + vy**2 + vz**2)

    # Gravitational acceleration (towards Earth's center)
    if r > 0:
        grav_acc = -(GM / r**3) * np.array([x, y, z])
    else:
        grav_acc = np.array([0.0, 0.0, 0.0])

    # Drag acceleration (opposite to velocity)
    if v > 0:
        drag_acc = -(0.5 * rho * v * Cd * A / mass) * np.array([vx, vy, vz])
    else:
        drag_acc = np.array([0.0, 0.0, 0.0])

    # Total acceleration
    acc = grav_acc + drag_acc

    # State derivatives: dx/dt = v, dv/dt = a
    return [vx, vy, vz, acc[0], acc[1], acc[2]]


def propagate(position, velocity, time, Cd, A, mass):
    """
    Propagate position and velocity in ECEF coordinates over a given time.

    Parameters:
    - position: Initial Position(x, y, z) in meters
    - velocity: Initial Velocity(vx, vy, vz) in m/s
    - time: Propagation time in seconds
    - Cd: Drag coefficient (dimensionless)
    - A: Cross-sectional area in m^2
    - mass: Mass of the object in kg

    Returns:
    - Tuple of (final_position, final_velocity) as named tuples
    """
    # Initial state vector
    state0 = [position.x, position.y, position.z, velocity.vx, velocity.vy, velocity.vz]

    # Time span for integration
    t_span = (0, time)

    # Solve the ODE system
    sol = solve_ivp(
        fun=derivatives,
        t_span=t_span,
        y0=state0,
        args=(Cd, A, mass),
        method="RK45",  # Runge-Kutta 4(5) method
        t_eval=[time],  # Evaluate solution at final time
    )

    # Check if integration was successful
    if sol.success:
        final_state = sol.y[:, 0]  # Extract state at t=time
        final_pos = Position(x=final_state[0], y=final_state[1], z=final_state[2])
        final_vel = Velocity(vx=final_state[3], vy=final_state[4], vz=final_state[5])
        return final_pos, final_vel
    else:
        raise ValueError("Numerical integration failed")
