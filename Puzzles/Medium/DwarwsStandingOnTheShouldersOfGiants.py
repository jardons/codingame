import sys
import math

n = int(input())  # the number of relationships of influence
m = {}
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = (int(j) for j in input().split())

    # Fill graph
    if y not in m: m[y] = [1, []]
    if x not in m: m[x] = [1, []]
    m[y][1].append(x)

    # Propagate length
    q = [y]
    while q:
        y = q.pop(0)
        for x in m[y][1]:
            if m[y][0]+1 > m[x][0]:
                m[x][0] = max(m[x][0], m[y][0]+1)
                q.append(x)

# The number of people involved in the longest succession of influences
print(max( (o[0] for o in m.values()) ))