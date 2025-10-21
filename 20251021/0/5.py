from itertools import itertools
def raw ()
    s = 0
    for i in itertools.count(1):
    s += 1/ i**2
    yield s

