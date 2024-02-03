"""
Learn how to create simple factory which helps to hide logic
of creating objects.
"""

from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """Person representation"""
    @abstractmethod
    def create(self, name):
        pass


class HR(Person):
    """HR class"""
    def create(self, name):
        print(f"HR {name} is created")


class Engineer(Person):
    """Engineer class"""
    def create(self, name):
        print(f"Engineer {name} is created")


class PersonFactory(object):
    @classmethod
    def create_person(cls, designation, name):
        eval(designation)().create(name)


if __name__ == "__main__":
    p_designation = input("Enter the designation: ")
    p_name = input("Enter the name: ")
    PersonFactory.create_person(p_designation, p_name)
