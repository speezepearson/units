"""Quantities relating to universal constants that are characteristics of particles.

Contains a submodule for each of several particles, the submodule defining various characteristics. Conventions for names of characteristics:

- q : charge
- m : mass
- u : magnetic moment
"""

from .general import *
from . import electron, proton, neutron