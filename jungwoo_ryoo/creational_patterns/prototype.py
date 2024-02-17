"""
Prototype

Problem:
    - Creating many identical objects individually - expensive.
    - Cloning - an alternative.

Scenario:
    - Mass production
    - Same color, same options, and so on.

Solution:
    - Create a prototypical instance first.
    - Clone it whenever you need a replica.
"""

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object."""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object."""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes."""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.options}"


if __name__ == "__main__":
    car = Car()
    prototype = Prototype()
    prototype.register_object("skylark", car)

    car1 = prototype.clone("skylark")

    print(car1)
