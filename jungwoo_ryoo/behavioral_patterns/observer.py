"""
Observer Pattern
- Define a one-to-many dependency between objects so that when one object changes state,
all its dependents are notified and updated automatically.

Solution:
    - Subject - maintains a list of observers, facilitates adding or removing observers
        - Attach: adds a new observer to the list
        - Detach: removes an observer from the list
        - Notify: sends a message to all observers when its state changes
    - Observer - provides a update interface for objects that need to be notified of a Subject's changes of state
    - ConcreteSubject - broadcasts notifications to observers on changes of state, stores the state of ConcreteObservers
    - ConcreteObserver - stores a reference to the ConcreteSubject, implements an update interface for the Observer to ensure state is consistent with the Subject's
"""


class Subject(object):  # Represents what is being 'observed'
    def __init__(self):
        # This is where references to all observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # For all the observers in the list, don't notify the one who is actually updating the temperature

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):  # Inherits from the Subject class
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # Set the name of the core
        self._temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:
    def update(self, subject):  # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print(f"Temperature Viewer: {subject._name} has Temperature {subject._temp}")


if __name__ == "__main__":
    # Let's create our subjects
    c1 = Core("Core 1")
    c2 = Core("Core 2")

    # Let's create our observers
    v1 = TempViewer()
    v2 = TempViewer()

    # Let's attach our observers to the first core
    c1.attach(v1)
    c1.attach(v2)

    # Let's change the temperature of our first core
    c1.temp = 80
    c1.temp = 90
