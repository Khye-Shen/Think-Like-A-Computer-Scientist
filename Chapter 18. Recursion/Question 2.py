import turtle

t = turtle.Turtle()
t.speed(0)

def Cesaro(t, order, size):

    if order == 0:
        t.forward(size)

    else:
        for angle in [-85, 170, -85, 0]:
            Cesaro(t, order-1, size/3)
            t.left(angle)

for i in range(4):

    Cesaro(t, 3, 1000)
    t.right(90)

turtle.done()
