import sys
from Painter import paint
from Patterns import patterns


if len(sys.argv) == 1:
    print("Printing default pattern...")
    paint(patterns)
elif len(sys.argv) == 2:
    if sys.argv[1] not in patterns:
        print("Invalid pattern. Please choose from the following list:")
        for p in patterns:
            print(p)
        exit()
    print("Printing", sys.argv[1], "...")
    paint(patterns, sys.argv[1])
elif len(sys.argv) == 3:
    print("Printing", sys.argv[1], "in", sys.argv[2], "...")
    paint(patterns, sys.argv[1], sys.argv[2])
elif len(sys.argv) > 3:
    print("Too many arguments provided")
    print("Usage: main.py [PATTERN_NAME] [COLOR]")
