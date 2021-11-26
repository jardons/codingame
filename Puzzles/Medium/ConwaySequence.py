import sys
import math

previous, l = [input()], int(input())

for i in range(l-1):
    table, count, current = [], 0, None

    for c in previous:
        if c == current:
            count += 1
        else:
            if current is not None:
                table.append(str(count))
                table.append(current)

            current, count = c, 1

    # Add last values
    table.append(str(count))
    table.append(current)

    previous = table

print(" ".join(previous))