"""
Bridge pattern is used when we need to decouple an abstraction from its implementation so that
the two can vary independently.

The bridge uses encapsulation, aggregation, and can use inheritance to separate responsibilities into different classes.
The bridge pattern helps untangle unnecessary class hierarchy complexity.
"""


class DrawingAPIOne:
    def draw_circle(self, x, y, radius):
        print(f"API 1 drawing a circle at ({x}, {y}) with radius {radius}")


class DrawingAPITwo:
    def draw_circle(self, x, y, radius):
        print(f"API 2 drawing a circle at ({x}, {y}) with radius {radius}")


class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent


if __name__ == "__main__":
    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    circle1.draw()

    circle2 = Circle(2, 3, 4, DrawingAPITwo())
    circle2.draw()
    circle2.scale(2)
    circle2.draw()