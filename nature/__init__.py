# nature.py - Information about the universe around us.
#
# Version of 2013-03-12.
#
"""
Constants of nature, attached to units.

Here are some examples of the use of this package.

Example 1: have you ever wondered about the magnitude of the centrifugal force due to the Earth's rotation when you're standing on the equator?

>>> from units.nature.cosmology.earth import radius, rotation_period
>>> from math import pi
>>> w = 2*pi / rotation_period
>>> print radius * w**2
0.0338592695244 meter / second^2

Example 2: did you know the sun pulls on the moon harder than the earth does?

>>> from units.nature.cosmology.moon import R as Rme
>>> from units.nature.cosmology.earth import m as Me, R as Rse
>>> from units.nature.cosmology.sun import mass as Ms
>>> from units.nature import G
>>> print "Earth pull: ", (G*Me/Rme**2)
Earth pull:  0.00269771179779 meter / second^2
>>> print "Sun pull:", (G*Ms/Rse**2)
Sun pull: 0.00680994803445 meter / second^2

Example 3: We address the question, "If 'natural' units are such that Plank's constant, the speed of light, and the gravitational constant all take the value of unity, then what is the natural unit of mass?"

>>> from units.nature import h, c, G
>>> from units import sqrt
>>> # Let's try to get rid of all dimensions of length, then time.
>>> x = h/c**2
>>> y = G/c**3
>>> print x
7.37249667848e-51 second kilogram
>>> print y
2.47692970651e-36 second / kilogram
>>> print sqrt(x/y)
5.45569963218e-08 kilogram

so the natural unit of mass is about 5.5e-05 grams.

"""

from . import general, particles, thermo, materials, cosmology
from .general import *
from .particles import *
from .thermo import *
from .materials import *
from .cosmology import *
