from Function import getPoints
import turtle

# TODO: add multipliers to each list ([0, 1])

def paint(patterns, pattern="city"):
    functions = getPoints(patterns[pattern])
    # print(functions)
    turtle.showturtle()
    turtle.speed(10)
    for func in functions:
        turtle.pu()
        x = -125
        for i in range(50):
            turtle.goto(x*3, functions[str(func)][i]*2)
            x += 5
            turtle.pd()
        turtle.pu()
    turtle.done()
