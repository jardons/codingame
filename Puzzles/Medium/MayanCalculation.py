import sys
import math

OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,
    '*': lambda a, b: a * b
}

def parseNumber(n):
    v = 0
    for i in range(0, len(n), l):
        v *= 20
        node = graph
        for j in range(l):
            node = node[n[i+j]]
        v += node
    return v

# Read grid from inputs
l, h = (int(i) for i in input().split())
grid = [input() for i in range(h)]

# Parse the grid as a graph.
graph = {}
for i in range(0, len(grid[0]), l):
    node = graph

    # Store graph navigation for all level except last one.
    for j in range(len(grid)-1):        
        key = grid[j][i:i+l]
        if key not in node: node[key] = {}
        node = node[key]
    
    # Store value in last node.
    node[grid[len(grid)-1][i:i+l]] = i // l

# Parse inputs
n1 = parseNumber([input() for i in range(int(input()))])
n2 = parseNumber([input() for i in range(int(input()))])
operation = input()

# Calculate
r = OPERATIONS[operation](n1, n2)

# Transform the result to base 20 in order to calculate.
output = [0] if r == 0 else []
while r != 0:
    u, r = (r % 20) * l, r // 20
    output.insert(0, u)

# Display prepared result.
for u in output:
    print(u, file=sys.stderr, flush=True)
    for i in range(len(grid)):
        print(grid[i][u:u+l])