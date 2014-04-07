from ... import kilogram, meter, second

m = mass = 7.3459e22 * kilogram
r = radius = 3476e3/2 * meter
R = orbital_radius = 3.84393e8 * meter
T = orbital_period = 2.3606e6 * second
t = rotation_period = T


__all__ = [
    "m", "mass",
    "r", "radius",
    "R", "orbital_radius",
    "T", "orbital_period",
    "t", "rotation_period"
]