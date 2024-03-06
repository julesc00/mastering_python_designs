"""
Visitor pattern is a way of separating an algorithm from an object structure on which it operates.

Problem:
    - New operations need to be added frequently and the object structure is stable.

Solution:
    - Visitor: declares a Visit operation for each class of Concrete
    - New operations
    - Various elements of an existing class hierarchy
    - ConcreteVisitor: implements each operation declared by Visitor
"""


class House(object):
    def accept(self, visitor):
        """Interface to accept a visitor"""
        # Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        # Note that the visitor now has a reference to the house object
        house.work_on_electricity(self)


if __name__ == "__main__":
    # Create an HVAC specialist
    hvac = HvacSpecialist()

    # Create an electrician
    electrician = Electrician()

    # Create a house
    house = House()

    # Work on the house by the HVAC specialist
    house.accept(hvac)

    # Work on the house by the electrician
    house.accept(electrician)
