"""Quantities relating to universal constants that aren't characteristics of particles."""

from ..abbrev import kg, m, s, N, A, J
from math import pi

h = planck_constant = 6.62606957e-34 * J*s
hbar = reduced_planck_constant = planck_constant / (2*pi)
c = speed_of_light = 299792458 * m/s
u0 = magnetic_constant = permeability_of_free_space = 4e-07*pi * N/A**2
e0 = electric_constant = permittivity_of_free_space = 1 / (c**2 * u0)
G = gravitational_constant = 6.67384e-11 * m**3/(kg*s**2)

__all__ = [
    "h", "planck_constant",
    "hbar", "reduced_planck_constant",
    "c", "speed_of_light",
    "u0", "magnetic_constant",
    "e0", "electric_constant",
    "G", "gravitational_constant",
]