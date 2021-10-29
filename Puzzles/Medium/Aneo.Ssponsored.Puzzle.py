import sys
import math

# Parse inputs
speed,light_count = int(input()),int(input())
l = [[int(j) for j in input().split()] for i in range(light_count)]

# Go from fastest speed and go backward until we can pass all traffic lights.
for i in range(speed, 0, -1):
    d = 36 / (i * 10)
    if all(((t[0] * d) % (t[1] * 2)) < t[1] for t in l):
        print(i)
        break