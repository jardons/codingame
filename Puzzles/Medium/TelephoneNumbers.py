import sys
import math

r, root = 0, {}
for i in range(int(input())):
    node = root
    for c in (c for c in input()):
        if c not in node:
            node[c] = {}
            r += 1
        node = node[c]

# The number of elements (referencing a number) stored in the structure.
print(r)