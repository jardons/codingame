import sys
import math
import itertools

def getPath(start, end, s):
    return [ start ] if s == 0 else range(start, end, s)

def placePath(map, t, s, nextTeeings):
    for d in DIRECTIONS:
        end = (t[0]+d[0]*s, t[1]+d[1]*s)
        
        # Ensure end stay in table
        if end[0] < 0 or end[1] < 0 or end[0] >= len(map) or end[1] >= len(map[0]):
            continue

        r = [i for i in itertools.product(getPath(t[0], end[0], d[0]), getPath(t[1], end[1], d[1]))]
 
        # Confirm we don't cross anything
        if any(i != t and map[i[0]][i[1]] not in VALID_PATH for i in r) or map[end[0]][end[1]] not in VALID_END:
            continue

        backup = {}
        for x,y in r:
            backup[(x,y)] = map[x][y]
            map[x][y] = d[2]
        
        if map[end[0]][end[1]] == 'H':
            map[end[0]][end[1]] = 'U' # Flag as used, will be emptied at the end, but keep case unusable.

            if placeNode(map, nextTeeings): return True

            # Rollback invalid path
            map[end[0]][end[1]] = 'H'
        elif s > 1 and placePath(map, end, s-1, nextTeeings):
            return True
        
        # Restore empty cases.
        for x,y in r:
            map[x][y] = backup[(x,y)]

    return False

def placeNode(map, teeings):
    if len(teeings) == 0: return True
    t = teeings[0]
    s = int(map[t[0]][t[1]])
    return placePath(map, t, s, teeings[1:])

# Constants
DIRECTIONS = [ (0,1,'>'), (1,0,'v'), (0,-1,'<'), (-1,0,'^') ]
VALID_PATH = [ '.', 'X' ]
VALID_END = [ '.', 'H' ]

# Prepare inputs
width, height = (int(i) for i in input().split())
map = [[c for c in input()] for i in range(height)]
teeings = [i for i in itertools.product(range(height), range(width)) if map[i[0]][i[1]].isnumeric()]

# Evaluate
# Implementation has been done using recursive calls, memory waste could be limited by removing the recursivity, but all tests case are valid without this improvment.
placeNode(map, teeings)

# Render result
for i in range(len(map)):
    print(''.join(map[i]).replace('X', '.').replace('U', '.'))