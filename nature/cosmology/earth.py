from ... import kilogram, meter, second, day

m = mass = 5.9727e24 * kilogram
r_eq = equatorial_radius = 6.378137e6 * meter
r_pol = polar_radius = 6.35691e6 * meter
r = radius = (equatorial_radius + polar_radius) / 2
g = surface_gravity = 9.80665 * meter/second**2
land_area = 148.847e12 * meter**2
R = AU = astronomical_unit = orbital_radius = 139597870700 * meter
T = orbital_period = sidereal_year = 3.1558149e7 * second
t = rotation_period = day * ( 1 - 1 / ( 1 + orbital_period / day ) )

tropical_year = 31556925.2 * second

__all__ = [
    "m", "mass",
    "r_eq", "equatorial_radius",
    "r_pol", "polar_radius",
    "r", "radius",
    "g", "surface_gravity",
    "land_area",
    "R", "AU", "astronomical_unit", "orbital_radius",
    "T", "sidereal_year",
    "t", "rotation_period"
    "tropical_year",
]