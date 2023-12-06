
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
