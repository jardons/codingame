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

# Calculate gates leading to exits
gates = { i : len([e for e in m[i] if e in exits]) for i in m }

# Execute the link closure.
def cutLink(gate, exit):
    print(f"{gate} {exit}")
    m[gate].remove(exit)
    m[exit].remove(gate)
    gates[gate] -= 1

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # For all nodes, calculates the number of extra operation left after closing all exit during shortest path.
    q, paths = [si], { si: (1 - gates[si], [si]) }
    while q:
        current = q.pop(0)
        distance, path = paths[current]

        for n in (n for n in m[current] if n not in exits and n not in path):
            newDist = distance + 1 - gates.get(n, 0)
            if newDist >= paths.get(n, (99999999, None))[0]:
                continue
            
            if n not in q:
                q.append(n)
            
            newPath = list(path);newPath.append(n)
            paths[n] = (newDist, newPath)

    # Once we calculated the number of operations left after closing all exit from each node,
    # We can select the one to close in priority.
    # Priority is given to :
    # 1) The lowest action count left on the path to the node.
    # 2) The closest node amongst the one previously selected.
    priority = next(n for n in sorted(((key, paths[key][0], paths[key][1]) for key in paths.keys() if gates[key] > 0), key= lambda k: (k[1], k[2]) ))[0]

    cutLink(priority, next(n for n in m[priority] if n in exits))