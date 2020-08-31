import turtle

t = turtle.Turtle()


def koch(t, order, size):

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

for i in range(3):
    koch(t, 2, 300)
    t.right(120)

turtle.done()