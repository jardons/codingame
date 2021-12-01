import sys
import math

# Build the graph in reverse direction.
_, v, dic = input(), int(input()), {}
for p, l, r in ((int(j) for j in input().split()) for _ in range(int(input()))):
    dic[l], dic[r] = ('Left', p), ('Right', p)

# Follow the path from v to root.
r = []
while v in dic:
    r.insert(0, dic[v][0])
    v = dic[v][1]

print(' '.join(r) if r else 'Root')