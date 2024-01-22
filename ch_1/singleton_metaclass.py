
class Singleton(type):
    """Metaclass that creates a Singleton base class when called."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Return the same instance of the class every time it is called."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print("Loading database")


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
