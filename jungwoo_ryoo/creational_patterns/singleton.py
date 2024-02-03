"""
Problem:
    Global variable in an object-oriented way.
    Borg design pattern is a way to share state between objects so that they can be used as a global variable.

Solution:
    Module--Shared by multiple objects.
    Borg design pattern--Computer networking acronyms.
"""


class Borg:
    """The Borg design pattern."""
    _shared_state = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):
    """The Singleton class."""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


if __name__ == "__main__":
    # Create a singleton object and add our first acronym
    x = Singleton(HTTP="Hyper Text Transfer Protocol")
    print(x)

    # Create another singleton object and if it refers to the same attribute dictionary by adding another acronym
    y = Singleton(SNMP="Simple Network Management Protocol")
    print(y)

    print(id(x))
    print(id(y))
