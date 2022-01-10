import sys
import copy

FAIL_CONDITIONS = [(1, 2), (2, 3)]
MOVES = [[0], (0, 3), (0, 2), (0, 1)]

stack = [[[b == 'L' for b in input().split()]]]
target = [b == 'L' for b in input().split()]

result, endDepth = [], -1
while stack and len(stack[0]) != endDepth:
    s = stack.pop(0)

    if all(target[i] == b for i, b in enumerate(s[-1])):
        result.append("\n".join(" ".join(map(lambda k: 'L' if k else 'R', l)) for l in s))
        endDepth = len(s) + 1

    for m in MOVES:
        newStep = copy.copy(s[-1])
        for i in m: newStep[i] = not newStep[i]

        if all(newStep[i] != newStep[j] or newStep[0] == newStep[j] for i, j in FAIL_CONDITIONS):
            stack.append(s + [newStep])

result.sort()

print(result[0])