import sys
import math

n, c = int(input()), int(input())

oods = [int(input()) for i in range(n)]
oods.sort()

r = []

while oods:
    if oods[0] * len(oods) > c:
        # Share amongst remaining one once the cap is reached.
        numberOods = len(oods)
        giftValue = c // numberOods

        # Check rounding loss
        missing = c - giftValue * numberOods

        gift = [giftValue] * (numberOods - missing) + [giftValue + 1] * missing

        r.extend(gift)
        c = 0
        break
    
    # Poorest Oods give everything
    o = oods.pop(0)
    c -= o
    r.append(o)

if c == 0:
    for o in r:
        print(o)
else:
    print("IMPOSSIBLE")
