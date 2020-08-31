import turtle


angles = [0, 120, 240]
colors = ["red", "blue", "magenta"]

def draw_equi_triang(t, size):

    for i in range(3):
        t.forward(size)
        t.left(120)


def shift_turtle(t, size, angle):

    # moves turtle to correct location to begin next triangle

    t.left(angle)
    t.penup()
    t.forward(size)
    t.pendown()
    t.right(angle)

def sierpinski(t, order, size, colorChangeDepth = -1):

    if order == 0:
        draw_equi_triang(t, size)


    else:
        if colorChangeDepth == 0:

            for (ind, angle) in enumerate(angles):
                t.color(colors[ind])
                sierpinski(t, order-1, size/2, colorChangeDepth-1)
                shift_turtle(t, size/2, angle)

        else:
            for angle in angles:
                sierpinski(t, order-1, size/2, colorChangeDepth-1)
                shift_turtle(t, size/2, angle)


t = turtle.Turtle()


t.speed(0)
sierpinski(t, 4, 200, 0)

turtle.done()