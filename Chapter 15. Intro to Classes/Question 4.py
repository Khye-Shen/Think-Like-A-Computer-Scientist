
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


