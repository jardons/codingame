import sys
import math

# Constants
TOP = 'TOP'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
DOWN = 'DOWN'

DIRECTION = { TOP: (-1, 0), LEFT: (0, -1), RIGHT: (0, 1), DOWN: (1, 0) }

ROOMS = [
    {},
    { TOP: DOWN, LEFT: DOWN, RIGHT: DOWN },
    { LEFT: RIGHT, RIGHT: LEFT },
    { TOP: DOWN },
    { TOP: LEFT, RIGHT: DOWN },
    { TOP: RIGHT, LEFT: DOWN },
    { LEFT: RIGHT, RIGHT: LEFT },
    { TOP: DOWN, RIGHT: DOWN },
    { LEFT: DOWN, RIGHT: DOWN },
    { LEFT: DOWN, TOP: DOWN },
    { TOP: LEFT },
    { TOP: RIGHT },
    { RIGHT: DOWN },
    { LEFT: DOWN },
]

# w: number of columns. h: number of rows.
w, h = (int(i) for i in input().split())
grid = [[int(c) for c in input().split()] for i in range(h)] # represents lines in the grid and contains W integers. Each integer represents one room of a given type.
ex = input()  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    inputs = input().split()
    xi, yi, pos = int(inputs[0]), int(inputs[1]), inputs[2]

    change = DIRECTION[ROOMS[grid[yi][xi]][pos]]

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(f"{xi + change[1]} {yi + change[0]}")