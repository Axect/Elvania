from jitpy import setup
setup('/home/rakhan/Documents/Python/pypy')
from jitpy.wrapper import jittify

@jittify([int, float], float)
def func(count, no):
    s = 0
    for i in range(count):
        s += no
    return s

func(100000, 1.2)
