import sys
import math

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = (int(i) for i in input().split())

m = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    m[n1] = m.get(n1, []);m[n1].append(n2)
    m[n2] = m.get(n2, []);m[n2].append(n1)

# the index of a gateway node
exits = [int(input()) for i in range(e)]

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    q, done = [si], []
    while q:
        current = q.pop(0)
        closest = next( (n for n in m[current] if n in exits), None)
        if closest is not None:
            print(f"{current} {closest}")
            m[current].remove(closest)
            m[closest].remove(current)
            break

        done.append(current)
        for n in (n for n in m[current] if n not in done):
            q.append(n)