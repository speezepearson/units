from numbers import Rational
from collections import Counter

class Dimensions(Counter):
    def __init__(self, _dict=None, **kwargs):
        if _dict is None:
            self.__init__(kwargs)
        else:
            if not all(isinstance(x, Rational) for x in _dict.values()):
                raise TypeError("powers of dimensions must be rational")
            Counter.__init__(self, _dict)
            self.clean()

    def clean(self):
        for key in self.keys():
            if self[key] == 0:
                del self[key]
    def update(self, *args, **kwargs):
        Counter.update(self, *args, **kwargs)
        self.clean()
    def subtract(self, *args, **kwargs):
        Counter.subtract(self, *args, **kwargs)
        self.clean()

    def __neg__(self):
        return Dimensions({dimension: -power
                           for (dimension, power) in self.items()})
    def __add__(self, other):
        result = self.copy()
        result.update(other)
        return result
    def __sub__(self, other):
        result = self.copy()
        result.subtract(other)
        return result
    def __mul__(self, other):
        return Dimensions({dimension: power*other
                           for (dimension, power) in self.items()})

    def __hash__(self):
        result = 0
        for (dimension, power) in self.items():
            result += hash(dimension) + hash(power)
        return result
    def __str__(self):
        if not self:
            return ""
        poss = [(d, v) for d, v in self.items() if v > 0]
        negs = [(d, v) for d, v in self.items() if v < 0]
        result = " ".join(("{}^{}".format(d,v) if v != 1 else d) for d, v in poss) if poss else "1"
        if not negs:
            return result
        result += " / "
        result += " ".join(("{}^{}".format(d,-v) if v != -1 else d) for d, v in negs)
        return result
    def __repr__(self):
        return "Dimensions({0!r})".format(dict(self))
