import sys
# from Painter.py import paint

if len(sys.argv) < 2:
    print("Usage: python main.py [pattern name]")
    print("See README for list of patterns")
elif len(sys.argv) is 2:
    print("Default pattern printing...")
    # paint()
elif len(sys.argv) is 3:
    print(sys.argv[2] + " printing...")
    # paint(sys.argv[2])
