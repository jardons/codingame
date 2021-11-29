import sys
import math

DIRECTIONS = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def getNeigboors(n):
    for d in DIRECTIONS:
        c = (n[0] + d[0], n[1] + d[1], n[2] + d[2])
        if (c[0] >= 0 and c[1] >= 0 and c[2] >= 0 and c[0] < lines and c[1] < rows and c[2] < columns):
            yield c

# Generate map
lines, rows, columns = (int(i) for i in input().split())
m, floor, start, end = [], [], None, None
for line in (input() for i in range(int(input()))):
    if line == '':
        floor = []
        m.append(floor)
    else:
        floor.append([c for c in line])

        if 'A' in line: start = (len(m)-1, len(floor)-1, line.index('A'))
        if 'S' in line: end = (len(m)-1, len(floor)-1, line.index('S'))

# Calculate distances
queue, distances = [ start ], { start: 0 }
while queue:
    n = queue.pop(0)
    if n == end:
        print(distances[n])
        break

    d = distances[n] + 1
    for c in (c for c in getNeigboors(n) if c not in distances and m[c[0]][c[1]][c[2]] != '#'):
        distances[c] = d
        queue.append(c)
else:
    print('NO PATH')