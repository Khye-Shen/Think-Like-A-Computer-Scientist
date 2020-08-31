import turtle



def draw_equi_triang(t, size):

    for i in range(3):
        t.forward(size)
        t.left(120)


def shift_turtle(t, size, angle):

    t.left(angle)
    t.penup()
    t.forward(size)
    t.pendown()
    t.right(angle)


def sierpinski(t, order, size):

    if order == 0:
        draw_equi_triang(t, size)

    else:

        for angle in [0, 120, 240]:
            sierpinski(t, order-1, size/2)
            shift_turtle(t, size/2, angle)


t = turtle.Turtle()


t.speed(0)
sierpinski(t, 4, 200)
