from ...abbrev import kg, m, s, K, C, V, A
from math import pi
from ..general import c, e0, hbar

qe = elementary_charge = 1.602176565e-19 * C
eV = electron_volt = qe * V
MeV = mega_electron_volt = 1e6 * eV

amu = atomic_mass_unit = 931.494061 * MeV/c**2
alpha = fine_structure_constant = qe**2 / (4*pi * c * e0 * hbar)

__all__ = [
    "qe", "elementary_charge",
    "eV", "electron_volt",
    "MeV", "mega_electron_volt",
    "amu", "atomic_mass_unit",
    "alpha", "fine_structure_constant"
]