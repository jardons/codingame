import sys
import math

n, previous, worst = int(input()), -1, 0
for v in (int(i) for i in input().split()):
    if v > previous:
        previous = v
    else:
        worst = min(worst, v - previous)

print(worst)