from . import qe, MeV
from ..general import hbar, c

q = charge = qe
m = mass = 938.272046 * MeV / c**2

nuclear_magneton = qe * hbar / (2 * m)
u = magnetic_moment = 2.792847356 * nuclear_magneton

__all__ = [
    "q", "charge",
    "m", "mass",
    "u", "magnetic_moment",
    "nuclear_magneton"
]