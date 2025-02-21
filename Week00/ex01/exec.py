import sys


def exec():
    print(" ".join(sys.argv[1:])[::-1].swapcase())


exec()
