import sys
from Painter import paint

if len(sys.argv) < 2: # they fucked up
    print("Usage: python main.py [pattern name]")
    print("See README for list of patterns")
elif len(sys.argv) is 2: # no pattern name given
    print("Default pattern printing...")
    paint()
elif len(sys.argv) is 3: # pattern name given
    print(sys.argv[2] + " printing...")
    paint(sys.argv[2])

# So here's what I'm going to do.
# I'll have a list of keywords that correspond to
# lists which contain a bunch of functions
# ou peut-etre une dictionaire? On pourrait avoir une
# dictionaire qui contient le nom du dessin et
# tout les fonctions dedans
