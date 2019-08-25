from Function import getPoints
from Patterns import mults
import turtle


def paint(patterns, pattern="city"):
    functions = getPoints(patterns[pattern])
    xmult = 3.1
    ymult = mults[pattern]
    # print(functions)
    turtle.showturtle()
    turtle.speed(0)
    for func in functions:
        turtle.pu()
        x = -125
        for i in range(50):
            turtle.goto(x*xmult, functions[str(func)][i]*ymult)
            x += 5
            turtle.pd()
        turtle.pu()
    turtle.done()
