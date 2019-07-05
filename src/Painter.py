#  Takes in an image name
#  Constructs a Canvas object
#  Also constructs a PhotoImage?
#  TODO: figure out what library is best suited for graphing
#  Image name corresponds to file in data folder that contains
#   number and nature of functions required to draw folder
#  Draws functions on canvas
#  well uh... bada bing bada boom...
from tkinter import Canvas, Tk, PhotoImage, mainloop
from Function import getPoints


def paint(pattern="jank"):
    functions = getPoints(parseFile(pattern))
    print(functions)
    # win = Tk()
    # photo = PhotoImage(width=350, height=350)
    # canvas = Canvas(win, width=350, height=350, bg="#ffffff")
    # canvas.pack()
    # canvas.create_image((350/2, 350/2), image=photo, state="normal")
    

def parseFile(patternFile):
    functions = []
    f = open(patternFile)
    for line in f:
        functions.append(line)
    return functions
