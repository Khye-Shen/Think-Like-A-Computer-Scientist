
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

        return(gradient)

def distance(p1,p2):

    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


p1 = Point(5, 5)
p2 = Point(6,9)


print(Point(4, 10).slope_from_origin())