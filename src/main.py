import sys
from Painter import paint
from Patterns import patterns

# TODO: fix whole elif connundrom
if len(sys.argv) is 1:
    print("Printing default pattern...")
    paint(patterns)
elif len(sys.argv) is 2:
    print("Printing", sys.argv[1], "...")
    paint(patterns, sys.argv[1])
elif len(sys.argv) > 2:
    print("Too many arguments provided")
    print("Usage: main.py [PATTERN_NAME]")
