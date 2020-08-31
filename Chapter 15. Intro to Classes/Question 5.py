
import math


class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def reflect_x(self):
        new_y = self.y * -1

        return (self.x, new_y)


    def slope_from_origin(self):



        gradient = float(self.y / self.x)

        return gradient


    def get_line_to(self, end):

        a = (end.y - self.y) / (end.x - self.x)

        b = self.y - (a * self.x)

        return (a, b)


    def midpoint_circle(self, p1, p2, p3):

        D = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y-p2.y))

        center_x = ((p1.x ** 2 + p1.y ** 2)*(p2.y - p3.y) + (p2.x ** 2 + p2.y ** 2)*(p3.y - p1.y) + (p3.x ** 2 + p3.y ** 2)*(p1.y - p2.y)) / D

        center_y = ((p1.x ** 2 + p1.y ** 2)*(p3.x - p2.x) + (p2.x ** 2 + p2.y ** 2)*(p1.x - p3.x) + (p3.x ** 2 + p3.y ** 2)*(p2.x - p1.x)) / D

        return (center_x, center_y)

def distance(p1,p2):

    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


p1 = Point(2, 3)
p2 = Point(5,0)
p3 = Point(8,3)


print(Point(4, 10).slope_from_origin())

print(Point(4, 11).get_line_to(Point(6, 15)))

print(Point(5, 6).midpoint_circle(p1, p2, p3))