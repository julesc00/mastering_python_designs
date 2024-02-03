"""
Problem it solves:
    The user expectation yields multiple related objects.

Solution:
    The abstract factory pattern provides an interface for creating families of related or dependent
    objects without specifying their concrete classes.

    Abstract Factory is a super factory that creates other factories. It is also called a factory of factories.
"""

from abc import ABCMeta, abstractmethod


class Dog:
    """A simple dog class"""
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Dog object"""
        return Dog("Hope")

    def get_food(self):
        """Return a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """PetStore houses our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is '{pet}'!")
        print(f"Our pet says hello by '{pet.speak()}'")
        print(f"Its food is '{pet_food}'")


if __name__ == "__main__":
    # Create a Concrete Factory
    factory = DogFactory()

    # Create a pet store housing our Abstract Factory
    shop = PetStore(factory)

    # Invoke the utility method to display the details of our pet
    shop.show_pet()
