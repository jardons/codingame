import itertools

CHANGES = [(0,1),(1,0),(0,-1),(-1,0)]
A, Y = ord('a'), ord('y')

m = [[ord(c) for c in input()] for _ in range(int(input()))]

kept = [ ['-' for _ in m[0]] for _ in m]

def recursion(i, j, stack, kept, m):
    current = m[i][j]
    for k, l in ((i + k, j + l) for k, l in CHANGES):
        # Check if inbound.
        if not (0 <= k < len(m) and 0 <= l < len(m[0])): continue

        # Check next letter.
        if m[k][l] != current + 1: continue

        # Go deeper.
        stack.append((k, l))

        if current == Y:
            for a, b in stack: kept[a][b] = chr(m[a][b])
        else:
            recursion(k, l, stack, kept, m)

        stack.pop(-1)

for i, j in itertools.product(range(len(m)), range(len(m[0]))):
    # Only start on 'a'.
    if m[i][j] != A or kept[i][j] != '-': continue

    recursion(i, j, [(i,j)], kept, m)

print('\n'.join(''.join(line) for line in kept))
