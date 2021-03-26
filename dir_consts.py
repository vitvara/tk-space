DIR_STILL = 0
DIR_CONTINUE = -1
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_OFFSET = {
    DIR_STILL: (0, 0),
    DIR_UP: (0, -1),
    DIR_RIGHT: (1, 0),
    DIR_DOWN: (0, 1),
    DIR_LEFT: (-1, 0),
}

DIR_RC_OFFSET = {
    DIR_STILL: (0, 0),
    DIR_UP: (-1, 0),
    DIR_RIGHT: (0, 1),
    DIR_DOWN: (1, 0),
    DIR_LEFT: (0, -1),
}