""" This is where we set global defaults that need to be consistent across
    files. Equivalent to #define.
"""

#collsion bitmasks

BITMASK_COLL_CLICK = 1
BITMASK_COLL_MOUSE = 2

#UI text render positions #XXX we need to deprecate this

UITEXT_MOUSE_COORD = 1
UITEXT_WIN_SIZE = 2
UITEXT_UUID = 3

#Transport stuff, ports for network comm

CONNECTION_PORT = 55565  # for racket-mode I will move my ports
DATA_PORT = 55566

#TODO local ports!

