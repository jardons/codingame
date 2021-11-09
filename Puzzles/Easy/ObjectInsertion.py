import sys
import math
import itertools

a, b = [int(i) for i in input().split()]
o = [[c for c in input()] for i in range(a)]
masks = [i for i in itertools.product(range(a), range(b)) if o[i[0]][i[1]] == '*']

c, d = [int(i) for i in input().split()]
map = [[c for c in input()] for i in range(c)]

r = [i for i in itertools.product(range(c - a + 1), range(d - b + 1)) if all((map[i[0]+mask[0]][i[1]+mask[1]] == '.' for mask in masks))]

print(len(r))
if len(r) == 1:

    for x, y in ((r[0][0]+mask[0], r[0][1]+mask[1]) for mask in masks):
        map[x][y] = '*'

    for i in range(len(map)):
        print(''.join(map[i]))