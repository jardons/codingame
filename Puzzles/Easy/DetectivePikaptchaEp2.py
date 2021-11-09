import sys
import math
import itertools

CHANGES = [(0,1),(1,0),(0,-1),(-1,0)]
DIRECTIONS = { '>': 0, 'v': 1, '<': 2, '^': 3 }

def isWall(map, c):
    return c[0] < 0 or c[1] < 0 or c[0] >= height or c[1] >= width or map[c[0]][c[1]] == '#'
    
def createNextNode(origin, d):
    d %= 4
    return ((origin[0] + CHANGES[d][0], origin[1] + CHANGES[d][1]), d)

def moveToNext(map, previous, direction, rotation):
    return next( ( t for t in ( createNextNode(previous, i) for i in range(direction, direction + 4 * rotation, rotation) ) if not isWall(map, t[0]) ), None)

# Read inputs
width, height = (int(i) for i in input().split())
map = [[c for c in input()] for i in range(height)]
rotation = -1 if input() == 'R' else 1

# Initialize
start = next((c for c in itertools.product(range(height), range(width)) if map[c[0]][c[1]] in DIRECTIONS))
direction = DIRECTIONS[map[start[0]][start[1]]]

# Start simulation
first = moveToNext(map, start, direction, rotation)

if first is None:
    # replace start char per 0 as no move are possible.
    map[start[0]][start[1]] = '0' 
else:
    # as soon as we moved once, we set the start point to 1.
    map[start[0]][start[1]] = '1'
    
    current,direction = first

    while current != start:
        map[current[0]][current[1]] = str(int(map[current[0]][current[1]])+1)

        # Check direction on the correct side first. (not the front one)
        current,direction = moveToNext(map, current, (direction + 4 - rotation) % 4, rotation)

for i in range(height):
    print(''.join(map[i]))