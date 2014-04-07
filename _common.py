"""Defines common units, both SI and imperial."""

from .unit import Unit

pico = 1e-12
nano = 1e-9
micro = 1e-6
milli = 1e-3
centi = 1e-2
deca = 1e1
kilo = 1e3
mega = 1e6
giga = 1e9
tera = 1e12

meter = Unit(1, meter=1)
kilogram = Unit(1, kilogram=1)
second = Unit(1, second=1)
coulomb = Unit(1, coulomb=1)
kelvin = Unit(1, kelvin=1)
mole = Unit(1, mole=1)

millimeter = milli*meter
centimeter = centi*meter
kilometer = kilo*meter

gram = milli*kilogram
dyne = gram*centimeter/second**2
erg = dyne*centimeter

minute = 60*second
hour = 60*minute
day = 24*hour
year = 365*day

newton = kilogram*meter/second**2
joule = newton*meter
volt = joule/coulomb
ampere = coulomb/second
farad = coulomb/volt
pascal = newton/meter**2
kilopascal = kilo*pascal
tesla = newton / (coulomb * meter/second)
ohm = volt/ampere
watt = joule/second
henry = volt/(ampere/second)
milliliter = centimeter**3
liter = kilo*milliliter

inch = 0.0254*meter
foot = 12*inch
yard = 3*foot
mile = 5280*foot

pound = 4.44822*newton
ounce = pound / 16.
slug = pound/(foot/second**2)

bar = 100*kilopascal
hertz = 1/second
