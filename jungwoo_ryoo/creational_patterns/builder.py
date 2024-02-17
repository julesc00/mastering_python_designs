"""
Problem:
    Excessive number of constructors.

    The Builder pattern is a design pattern designed to provide a flexible solution
    to various object creation problems in object-oriented programming. The intent
    of the Builder design pattern is to separate the construction of a complex
    object from its representation.

    Remove unnecessary complexity.

Solution:
    - Director
    - Abstract builder--Interfaces
    - Concrete builder--Implements the interfaces defined by the Abstract Builder
    - Product--The complex object to be created
"""


class Director:
    """Director class"""
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract builder"""
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete builder"""
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car:
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f"{self.model} | {self.tires} | {self.engine}"


if __name__ == "__main__":
    c_builder = SkyLarkBuilder()
    director = Director(c_builder)
    director.construct_car()
    car = director.get_car()

    print(car)
