# Final solution for this problem will stay a work in progress, all test case for The Fall - episode 2 are covered.
# Additional refining of the algorithm will still be needed, but included in the episode 3 that will provide the final resolution.

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
    def __init__(self, grid, endX):
        self._grid = [[Room(self, x, y, int(grid[y][x]), endX) for x in range(len(grid[y]))] for y in range(len(grid))]
        self.rocks = []
        self.time = 1
    
    def get(self, x, y): return self._grid[y][x]

    def updateRocks(self, rocks):
        hasFoundNew = False
        for r in rocks:
            room, pos = self.get(int(r[0]), int(r[1])), r[2]

            if not any(r for r in self.rocks if r.isIn(room, self.time)):
                self.rocks.append(Rock(room, pos, self.time))
                hasFoundNew = True

        return hasFoundNew

class Room:
    def __init__(self, grid, x, y, c, endX):
        c = int(c)
        self._grid = grid
        self.x, self.y, self.isFinal = x, y, x == endX and y == h-1
        self.roomId, self.canRotate = abs(c), c > 1
        self.template = ROOMS[self.roomId]
        self.time = -1

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

    def rotate(self, direction):
        if direction != KEEP:
            self.roomId = ROTATIONS[self.roomId][direction]
            self.template = ROOMS[self.roomId]

class Rock:
    def __init__(self, room, e, t):
        self.baseTime = t
        self.timeLine = [ (room, e, t) ]
        self.breakTime = None if room.time == -1 else room.time 
        self.isDangerous = False

    def isIn(self, room, t):
        return t - self.baseTime < len(self.timeLine) and self.timeLine[t - self.baseTime][0] == room
    
    def toFuture(self):
        room, e, t = self.timeLine[-1]
        if self.breakTime is not None: return # Already destroyed.

        newRoom = room.goThrough(e)
        template = ROOMS[newRoom.roomId]
        if e not in template or newRoom.isFinal:
            self.breakTime = t + 1 # Rock as nowhere to go, hit a wall
        elif newRoom.time < t:
            self.timeLine.append((newRoom, REVERSE[template[e]], t + 1))
        else:
            self.breakTime, self.isDangerous = newRoom.time, True # Hit Indie, will need to avoid

    def getLastChance(self):
        return [o for o in self.timeLine if o[0].canRotate][-1]

def createOperationFromStack(stack):
    operations, flips = [], []

    for o in reversed(stack):
        op = (o[0], o[3], o[0].time)
        if op[1] == FLIP:
            flips.append( (op[0], LEFT, op[2] - 1) )
            op = (op[0], LEFT, op[2])
        elif op[1] == KEEP and len(flips) > 0:
            op = flips.pop()

        operations.insert(0, op)

    return operations

# w: number of columns. h: number of rows.
w, h = (int(i) for i in input().split())

# represents lines in the grid and contains W integers. Each integer represents one room of a given type.
grid = Grid([[c for c in input().split()] for i in range(h)], int(input()))

operations = None

# game loop
while True:
    inputs = input().split()
    xi, yi, pos = int(inputs[0]), int(inputs[1]), inputs[2]
    
    grid.updateRocks( (input().split() for i in range(int(input()))) )

    if operations is None:
        firstRoom = grid.get(xi, yi)
        firstRoom.time = grid.time
        room, entrance = firstRoom.goThrough(pos), REVERSE[firstRoom.template[pos]]
        room.time = grid.time

        # Compute operations
        time, stack = grid.time + 1, [ [room, entrance, room.getRotations(entrance), KEEP] ]

        while not stack[-1][0].isFinal:
            room, entrance, rotations, _ = stack[-1]

            direction = next(rotations, None)
            if direction is None:
                stack.pop()
                op = stack[-1]
                # Rollback the rotation.
                op[0].rotate(REVERSE[op[3]])
                op[3], op[0].time = KEEP, -1
                continue

            # Execute rotation
            room.rotate(direction)
            room.time = time
            stack[-1][3] = direction

            # Look for next node.
            room, exit = room.goThrough(entrance), REVERSE[room.template[entrance]]
            time += 1
            stack.append( [room, exit, room.getRotations(exit), KEEP] )
        
        # Convert stack to operations list.
        operations = createOperationFromStack(stack)

    # Calculate rocks path up to rocks colisions.
    # We can ignore any re-evaluation of the main path as all test case allow simple rock interception.
    for r in grid.rocks:
        while r.breakTime is None: r.toFuture()
        if r.isDangerous:
            op = r.getLastChance()
            operations.append(op)
            op[0].rotate(op[1])
            r.isDangerous = False
    
    grid.time += 1
    operations.sort(key= lambda o: o[2])
    operations = [o for o in operations if o[1] != KEEP]

    # One line containing on of three commands: 'X Y LEFT', 'X Y RIGHT' or 'WAIT'
    if operations:
        room, direction, turn = operations.pop(0)
        if direction == KEEP:
            print("WAIT")
        else:
            print(f"{room.x} {room.y} {direction}")
    else:
        print("WAIT")
