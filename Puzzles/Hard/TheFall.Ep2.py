# Current solution is an intermediate resolution, still ignoring the rocks from the 2 last tests cases.

import sys
import math
import itertools

# Constants
TOP, LEFT, RIGHT, DOWN, FLIP, KEEP = 'TOP', 'LEFT', 'RIGHT', 'DOWN', 'FLIP', 'KEEP'

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

# Index of available rotations allowing to change case orientation.
ROTATIONS = [
    {},
    {},
    { LEFT: 3, RIGHT: 3 },
    { LEFT: 2, RIGHT: 2 },
    { LEFT: 5, RIGHT: 5 },
    { LEFT: 4, RIGHT: 4 },
    { LEFT: 9, RIGHT: 7, FLIP: 8 },
    { LEFT: 6, RIGHT: 8, FLIP: 9 },
    { LEFT: 7, RIGHT: 9, FLIP: 6 },
    { LEFT: 8, RIGHT: 6, FLIP: 7 },
    { LEFT: 13, RIGHT: 11, FLIP: 12 },
    { LEFT: 10, RIGHT: 12, FLIP: 13 },
    { LEFT: 11, RIGHT: 13, FLIP: 10 },
    { LEFT: 12, RIGHT: 10, FLIP: 11 },
]

# Dictionary used for directions reversion.
REVERSE = { DOWN: TOP, RIGHT: LEFT, LEFT: RIGHT, TOP: DOWN, FLIP: FLIP, KEEP: KEEP }

class Grid:
    def __init__(self, grid):
        self._grid = [[Room(self, x, y, int(grid[y][x])) for x in range(len(grid[y]))] for y in range(len(grid))]
    
    def get(self, x, y):return self._grid[y][x]

class Room:
    def __init__(self, grid, x, y, c):
        c = int(c)
        self._grid = grid
        self.x, self.y = x, y
        self.roomId, self.canRotate = abs(c), c > 1
        self.template = ROOMS[self.roomId]

    def goThrough(self, origin):
        change = DIRECTION[self.template[origin]]
        return self._grid.get(self.x + change[1], self.y + change[0])

    def getRotations(self, origin):

        def leadInGrid(template):
            change = DIRECTION[template[origin]]
            x, y = self.x + change[1], self.y + change[0]
            return (x >= 0 and y >= 0 and x < w and y < h) and self._grid.get(x, y).roomId != 0

        if origin in ROOMS[self.roomId] and leadInGrid(self.template):
            yield KEEP

        if self.canRotate:
            for d in ROTATIONS[room.roomId].keys():
                rotatedRoomTemplate = ROOMS[ROTATIONS[room.roomId][d]]
                if origin in rotatedRoomTemplate and leadInGrid(rotatedRoomTemplate):
                    yield d
    
    def canEnter(self, origin):
        if origin not in self.template or self.goThrough(origin).roomId == 0:
            return False

        return self.isFinal()

    def rotate(self, direction):
        if direction != KEEP:
            self.roomId = ROTATIONS[self.roomId][direction]
            self.template = ROOMS[self.roomId]

    def isFinal(self): return self.x == ex and self.y == h-1

# w: number of columns. h: number of rows.
w, h = (int(i) for i in input().split())

# represents lines in the grid and contains W integers. Each integer represents one room of a given type.
grid = Grid([[c for c in input().split()] for i in range(h)])

# the coordinate along the X axis of the exit.
ex = int(input())
operations = None

# game loop
while True:
    inputs = input().split()
    xi, yi, pos = int(inputs[0]), int(inputs[1]), inputs[2]
    
    # the number of rocks currently in the grid.
    for i in range(int(input())):
        inputs = input().split()
        xr, yr, posr = int(inputs[0]), int(inputs[1]), inputs[2]

    if operations is None:
        firstRoom = grid.get(xi, yi)
        room, entrance = firstRoom.goThrough(pos), REVERSE[firstRoom.template[pos]]

        # Compute operations
        stack = [ [room, entrance, room.getRotations(entrance), KEEP] ]
        while not stack[-1][0].isFinal():
            room, entrance, rotations, _ = stack[-1]

            direction = next(rotations, None)
            if direction is None:
                stack.pop()
                op = stack[-1]
                # Rollback the rotation.
                op[0].rotate(REVERSE[op[3]])
                op[3] = KEEP
                continue

            # Execute rotation
            room.rotate(direction)
            stack[-1][3] = direction

            # Look for next node.
            room, exit = room.goThrough(entrance), REVERSE[room.template[entrance]]
            stack.append( [room, exit, room.getRotations(exit), KEEP] )
        
        # Remove KEEP orders
        operations = [(o[0], o[3]) for o in stack if o[3] != KEEP]
    
    # One line containing on of three commands: 'X Y LEFT', 'X Y RIGHT' or 'WAIT'
    if len(operations) == 0:
        print("WAIT")
    else:
        op = operations.pop(0)
        if op[1] == FLIP:
            # Flip need to be split in 2 rotations.
            print(f"{op[0].x} {op[0].y} {LEFT}")
            operations.insert(0, (op[0], LEFT))
        else:
            print(f"{op[0].x} {op[0].y} {op[1]}")

    # Write an action sing print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)