import sys
from Painter import paint
from Patterns import patterns

print("main reached")
# if len(sys.argv) > 3:  # ils ont ratte
#     print("Usage: python main.py [pattern name]")
#     print("See README for list of patterns")
# elif len(sys.argv) is 2:  # no pattern name given
#     print("Default pattern printing...")
#     paint(patterns)
# elif len(sys.argv) is 3:  # pattern name given
#     print(sys.argv[2] + " printing...")
#     paint(patterns, sys.argv[2])
paint(patterns)
