import sys
from fractions import Fraction
from . import dimensions, unit, abbrev
from .dimensions import Dimensions
from .unit import Unit, MismatchedUnitsException

def root(x, n):
    return x**Fraction(1, n)
def sqrt(x):
    return root(x, 2)

from ._common import *

from . import nature