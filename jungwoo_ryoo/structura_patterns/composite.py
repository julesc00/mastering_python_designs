"""
Composite pattern is a structural design pattern that lets you compose objects into tree structures and
then work with these structures as if they were individual objects.

Solution:
    - Component
    - Child
    - Composite
"""


class Component:
    """Abstract class"""
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """Concrete class"""
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print(f"{self.name}")
