import sys
import math

# Read input.
l, c, n = (int(i) for i in input().split())
line = [int(input()) for i in range(n)]

def getCalculatedFrom(start):
    count, i = 0, start
    # Loop condition need to ensure we don't load twice the same person if the line is smaller that the passenger size.
    while line[i] + count <= l and (i != start or count == 0):
        count += line[i]
        i = (i + 1) % n
    return (i, count)

# Precalculate the load for each starting gruop as the order never change.
precalculated = [getCalculatedFrom(i) for i in range(len(line))]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Operate the RollerCoaster
cash, pos = 0, 0
for i in range(c):
    pos,count = precalculated[pos]
    cash += count

print(cash)