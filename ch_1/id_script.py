
class A:
    """Factory method sample, example from page 10"""
    pass


if __name__ == "__main__":
    a = A()
    b = A()
    print(id(a) == id(b))
    print(a, b)
