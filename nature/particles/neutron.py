from . import qe, MeV
from ..general import hbar, c
from .proton import nuclear_magneton

q = charge = 0
m = mass = 939.565379 * MeV / c**2

u = magnetic_moment = -1.9130427 * nuclear_magneton

__all__ = [
    "q", "charge",
    "m", "mass",
    "u", "magnetic_moment"
]