from Function import getPoints
from Patterns import mults
import turtle
import random


def paint(patterns, pattern="city"):
    functions = getPoints(patterns[pattern])
    xmult = 3.1
    ymult = mults[pattern]
    # print(functions)
    turtle.showturtle()
    turtle.speed(0)
    for func in functions:
        turtle.color(getColor())
        turtle.pu()
        x = -125
        for i in range(50):
            turtle.goto(x*xmult, functions[str(func)][i]*ymult)
            x += 5
            turtle.pd()
        turtle.pu()
    turtle.done()


def getColor():
    red = ["maroon", "darkorange", "mistyrose", "chocolate", "tomato",
           "coral", "darksalmon", "sienna"]
    blue = ["skyblue", "slategrey", "teal", "paleturquoise", "royalblue",
             "lavender", "lightsteelblue", "cornflowerblue"]
    return red[random.randint(0, 7)]
