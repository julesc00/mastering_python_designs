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


class Composite(Component):
    """Concrete class and maintain the tree recursive structure"""
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print(f"{self.name}")
        for i in self.children:
            i.component_function()


if __name__ == "__main__":
    # Build a composite submenu1
    sub1 = Composite("submenu1")
    # Create a new child sub_submenu11
    sub11 = Child("sub_submenu11")
    # Create a new child sub_submenu12
    sub12 = Child("sub_submenu12")

    # Add the sub_submenu11 and sub_submenu12 to submenu1
    sub1.append_child(sub11)
    sub1.append_child(sub12)

    # Build a top-level composite menu
    top = Composite("top_menu")
    sub2 = Child("submenu2")

    top.append_child(sub1)
    top.append_child(sub2)

    top.component_function()
