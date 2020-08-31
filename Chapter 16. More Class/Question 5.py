class Point:


    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y


class Rectangle:


    def __init__(self, posn, w, h):

        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):

        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):

        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def flip(self):

        (self.width, self.height) = (self.height, self.width)

    def contains(self, point):

        if (0 <= point.x < 10) and (0 <=  point.y < 5):

            return True

        else:

            return False

    def overlap(self, p3, p4):



        if (self.corner.x >= p4.x and p3.x >= (self.corner.x - self.width)):
            return False


        if (self.corner.y <= p4.y and p3.y <= (self.corner.y - self.height)):
            return False

        return True

r = Rectangle(Point(0, 10), 10, 10)

print(r.overlap(Point(5, 5), Point(15, 0)))