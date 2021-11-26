import sys
import math
import itertools

CHANGES = [(0,1),(1,0),(0,-1),(-1,0)]

# Read inputs
width, height = (int(i) for i in input().split())
map = [[c for c in input()] for i in range(height)]

def getCase(i, j):
    if i < 0 or j < 0 or i >= height or j >= width:
        return 0
    
    return 0 if map[i][j] == '#' else 1

for i, j in itertools.product(range(height), range(width)):
    if map[i][j] != '#':
        map[i][j] = str(sum( [getCase(i+c[0], j+c[1]) for c in CHANGES] ))

for l in map:
    print("".join(l))