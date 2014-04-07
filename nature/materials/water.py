from ...abbrev import g, K, mol
from ..thermo import stp_T

molar_mass = 18.0153 * g/mol
freezing_1atm = stp_T - 20*K
boiling_1atm = freezing_1atm + 100*K

__all__ = [
    "molar_mass",
    "freezing_1atm",
    "boiling_1atm",
]