from Function import getPoints
import turtle


# TODO: well, make it so that this shit draws shit
def paint(patterns, pattern="test"):
    print("paint reached")
    functions = getPoints(patterns[pattern])
    print(functions)
    turtle.showturtle()
    for func in functions:
        turtle.penup()
        for x in range(20):
            turtle.pd()
            turtle.goto(x*30, functions[str(func)][x]*30)
            turtle.pu()
    turtle.done()
