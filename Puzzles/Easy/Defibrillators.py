import sys
import math

def rad(degree):
    # Codingame don't provide any regional settings with a ',' separator, we need to use replace instead.
    return float(degree.replace(',', '.')) * math.pi / 180.0

lon, lat, closest = rad(input()), rad(input()), None

for i in range(int(input())):
    defib = input().split(';')

    latB, lonB = rad(defib[5]), rad(defib[4])
    x, y = (lonB - lon) * math.cos((lat+latB)/2), latB - lat
    d = ((x*x + y*y) ** 0.5) # The 6371 of the formula can be ignored as it's just a unit change.

    if closest is None or closest[1] > d:
        closest = (defib[1], d)

print(closest[0])