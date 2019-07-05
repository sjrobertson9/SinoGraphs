#  takes in list of functions
#  for each function, calculates 50 x,y points
#  stores each point in a matrix
import math

def getPoints(functions):
    funcPoints = {}
    for func in functions:
        if "sin" in func:
            points = parseFunc(func, "sin")
        elif "cos" in func:
            points = parseFunc(func, "cos")
        else:
            raise Exception("No function name found")
        funcPoints[func] = points
    return funcPoints

# EX: sin(x) + 5
def parseFunc(func, type):
    func_split = func.partition(type)
    # EX: [] [sin] [(x)+5]
    # AMPLITUDE
    if func_split[0] is "":
        a = 1
    else:
        if func_split[0].startswith("-"):
            if func_split[0].strip("-") is "":
                a = -1
            else:
                a = int(func_split[0].strip("-")) * -1
        else:
            a = int(func_split[0])
    # PERIOD
    b_split = func_split[2].split("x")
    # EX: [(, )+5]
    if b_split[0].strip("(") is "":
        b = 1
    else:
        b = b_split[0].strip("(")
        if b.startswith("-"):
            if b.strip("-") is '':
                b = -1
            else:
                b = int(b.strip("-")) * -1
        else:
            b = int(b)
    # HORIZONTAL SHIFT
    c_split = b_split[1].partition(")")
    # EX: [] [)] [+5]
    if c_split[0] is "":
        c = 0
    else:
        c = c_split[0].strip(")")
        if c_split[0].startswith("-"):
            c = int(c.strip("-")) * -1
        else:
            c = int(c_split[0])
    # VERTICAL SHIFT
    if c_split[2].startswith("-"):
        d = int(c_split[2].strip("-")) * -1
    elif c_split[2].startswith("+"):
        d = int(c_split[2].strip("+"))
    else:
        d = 0
    points = []
    # TODO: calculate 50 values given the a b c and d values
    for x in range(0, 50, 5):
        points.append(a * math.sin(b * x + c) + d)
    return points

# def main():
#     funcs = ["sin(x)", "-sin(x)", "-4sin(x)", "4sin(x)", "8sin(x)",
#              "-8sin(x)", "cos(x)", "-cos(x)", "50sin(x)", "-50sin(x)"]
#     pointz = getPoints(funcs)
#     for func, points in pointz.items():
#         print(func, ":", points)
#
# main()


