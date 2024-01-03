"""
The Abstract Factory Pattern

Since the abstract factory pattern is a generalization of the factory method pattern, it offers
the same benefits, it makes tracking an object creation easier, it decouples object creation
from object usage, and it gives us the potential to improve the memory usage and
performance of our application.

But, a question is raised: How do we know when to use the factory method versus using an
abstract factory? The answer is that we usually start with the factory method which is
simpler. If we find out that our application requires many factory methods, which it makes
sense to combine to create a family of objects, we end up with an abstract factory.

A benefit of the abstract factory that is usually not very visible from a user's point of view
when using the factory method is that it gives us the ability to modify the behavior of our
application dynamically (at runtime) by changing the active factory method. The classic
example is the ability to change the look and feel of an application (for example, Apple-like,
Windows-like, and so on) for the user while the application is in use, without the need to
terminate it and start it again.

Let's start with the kid's game. It is called FrogWorld. The main hero is a frog who enjoys
eating bugs. Every hero needs a good name, and in our case, the name is given by the user
at runtime. The interact_with() method is used to describe the interaction of the frog
with an obstacle (for example, a bug, puzzle, and other frogs) as follows:
"""


class Frog:
    """A Frog"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """Interact with some obstacle"""
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)


class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"


class FrogWorld:
    """The Frog World game"""

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------ Frog World ------"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()
