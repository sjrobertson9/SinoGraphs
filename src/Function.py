#  takes in list of functions
#  for each function, calculates 50 x,y points
#  stores each point in a list within a dictionary
import math


def getPoints(functions):
    funcPoints = {}
    for func in functions:
        if "sin" in func:
            points = parseFunc(func, "sin")
        elif "cos" in func:
            points = parseFunc(func, "cos")
        elif "tan" in func:
            points = parseFunc(func, "tan")
        else:
            raise Exception("No function name found")
        funcPoints[func] = points
    return funcPoints


# TODO: make this work with fractions :(
# EX: sin(1/2x) + 5
def parseFunc(func, type):
    # print("func:", func)
    func_split = func.partition(type)
    # EX: [1/2] [sin] [(1/2x)+5]
    # AMPLITUDE
    if func_split[0] is "":
        a = 1
    elif "/" in func_split[0]:
        a_split = func_split[0].partition("/")
        num = a_split[0]
        denom = a_split[2]
        a = float(num) / float(denom)
    else:
        if func_split[0].startswith("-"):
            if func_split[0].strip("-") is "":
                a = -1
            else:
                # print("func_split:",func_split)
                a = int(func_split[0].strip("-")) * -1
        else:
            a = int(func_split[0])
    # PERIOD
    b_split = func_split[2].split("x")
    # EX: [(1/2, )+5]
    if b_split[0].strip("(") is "":
        b = 1
    elif "/" in b_split[0]:  # FRACTION ALERT
        b_strip = b_split[0].strip("(")
        b_strip_split = b_strip.partition("/")
        num = b_strip_split[0]
        denom = b_strip_split[2]
        b = float(num) / float(denom)
        # print(b)
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
    for x in range(-50, 50, 1):
        if type is "sin":
            points.append(a * math.sin(b * x + c) + d)
        elif type is "cos":
            points.append(a * math.cos(b * x + c) + d)
        else:
            points.append(a * math.tan(b * x + c) + d)
    return points


# def main():
#     funcs = ["tan(1/3x)", "tan(-1/3x)", "tan(1/4x)", "tan(-1/4x)",
#                 "3tan(1/3x)", "-3tan(1/3x)", "3tan(1/4x)", "-3tan(1/4x)",
#                 "3tan(1/4x)", "-3tan(1/4x)", "2sin(1/2x)", "-2sin(1/2x)"]
#     pointz = getPoints(funcs)
#     for func, points in pointz.items():
#         print(func, ":", points)
#
#
# main()
