"""Quantities relating to thermodynamics and statistical mechanics."""

from ..abbrev import kg, m, s, K, J, kPa, mol
from math import pi
from .general import hbar, c

nA = avogadros_number = avogadro_constant = long(6.02214129e+23)
kB = boltzmann_constant = 1.38065e-23 * J/K
R = ideal_gas_constant = nA/mol * kB
sigma = stefan_boltzmann_constant = pi**2/60 * kB**4 / (60 * c**2 * hbar**3)
stp_T = 273.15 * K
stp_P = 100 * kPa
satp_T = 298.15 * K
satp_P = 100 * kPa

__all__ = [
    "nA", "avogadros_number", "avogadro_constant",
    "kB", "boltzmann_constant",
    "R", "ideal_gas_constant",
    "sigma", "stefan_boltzmann_constant",
    "stp_T",
    "stp_P",
    "satp_T",
    "satp_P"
]