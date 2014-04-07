from . import qe, MeV
from ..general import hbar, c
from ...abbrev import A, m

q = charge = -qe
m = mass = 0.510998928 * MeV / c**2
u = magnetic_moment = 9.284764e-20 * A*m**2

bohr_magneton = qe * hbar / (2 * m)

__all__ = [
    "q", "charge",
    "m", "mass",
    "u", "magnetic_moment",
    "bohr_magneton"
]