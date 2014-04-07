from .dimensions import Dimensions
from numbers import Number, Rational
from functools import total_ordering

class MismatchedUnitsException(ValueError):
    pass

@total_ordering
class Unit(object):
    def __init__(self, value, **kwargs):
        self.value = value
        self.dimensions = Dimensions(kwargs)

    def __hash__(self):
        return hash(self.value) + hash(self.dimensions)
    def __neg__(self):
        return Unit(-self.value, **self.dimensions)
    def __abs__(self):
        return Unit(abs(self.value), **self.dimensions)
    def __nonzero__(self):
        return not self.value == 0
    def __str__(self):
        return "{0} {1}".format(self.value, self.dimensions)
    def __repr__(self):
        return "Unit({0!r}, **{1!r})".format(self.value, self.dimensions)

    # Coercion:
    def __float__(self):
        if self.dimensions:
            raise MismatchedUnitsError("can't coerce Unit with dimensions to number")
        return float(self.value)
    def __int__(self):
        if self.dimensions:
            raise MismatchedUnitsError("can't coerce Unit with dimensions to number")
        return int(self.value)

    def __eq__(self, other):
        if isinstance(other, Unit):
            if self.dimensions != other.dimensions:
                raise MismatchedUnitsError("can't compare Units of different dimensions")
            return self.value == other.value
        elif isinstance(other, Number):
            return float(self) == other
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Unit):
            if self.dimensions != other.dimensions:
                raise MismatchedUnitsError("can't compare Units of different dimensions")
            return self.value == other.value
        elif isinstance(other, Number):
            return float(self) == other
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Unit):
            if self.dimensions != other.dimensions:
                raise MismatchedUnitsError("can't add Units of different dimensions")
            return Unit(self.value+other.value, **self.dimensions)
        elif isinstance(other, Number):
            return Unit(self.float(self) + other)
        return NotImplemented
    def __radd__(self, other):
        if isinstance(other, Number):
            return other + float(self)
        return NotImplemented

    def __sub__(self, other): 
        if isinstance(other, (Unit, Number)):
            return self + (-other)
        return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, Number):
            return other - float(self)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Unit):
            return Unit(self.value*other.value, **(self.dimensions+other.dimensions))
        elif isinstance(other, Number):
            return Unit(self.value*other, **self.dimensions)
        return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Unit):
            return Unit(self.value/other.value, **(self.dimensions-other.dimensions))
        elif isinstance(other, Number):
            return Unit(self.value/other, **self.dimensions)
        return NotImplemented

    def __rdiv__(self, other): 
        if isinstance(other, Number):
            return Unit(other/self.value, **(-self.dimensions))
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Rational):
            return Unit(self.value**other, **(self.dimensions*other))
        try:
            base = float(self)
        except MismatchedUnitsException:
            return NotImplemented
        else:
            return base**other
    def __rpow__(self, other):
        return other**float(self)
