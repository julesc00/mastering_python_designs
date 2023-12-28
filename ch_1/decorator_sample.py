
def decorator(func):
    def wrapper():
        print("Extra functionality")
        func()
    return wrapper


@decorator
def initial_function():
    print("Initial functionality")


if __name__ == "__main__":
    initial_function()


class House:
    """
    Specifically, you can define three methods for a property:

        A getter - to access the value of the attribute.
        A setter - to set the value of the attribute.
        A deleter - to delete the instance attribute.
    """
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price
