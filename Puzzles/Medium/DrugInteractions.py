import sys
import math

def areCompatibleDrugs(w1, w2):
    charCount = 0
    for k in (k for k in drugsDictionary[w1].keys() if k in drugsDictionary[w2]):
        charCount += min(drugsDictionary[w1][k], drugsDictionary[w2][k])
        if charCount >= 3:
            return False
    return True

def getBiggestGroup(drugs, selected, currentMax):
    selectedCount = len(selected)
    if not drugs: return selectedCount
    if len(drugs) + selectedCount <= currentMax: return currentMax
   
    for i, d in enumerate(drugs):
        if len(compatibilities[d]) > currentMax and all(d in compatibilities[o] for o in selected):
            selected.append(d)
            currentMax = max(currentMax, getBiggestGroup([o for o in compatibilities[d] if o in drugs[i+1:]], selected, currentMax))
            selected.pop()

    return currentMax

# Parse Input.
drugs = [input().lower() for _ in range(int(input()))]

# Create comparison dictionary.
drugsDictionary = {s: {c: s.count(c) for c in s} for s in drugs}

# Create compatibilities map.
compatibilities = {d: [] for d in drugs}
for i, d1 in enumerate(drugs):
    for d2 in (d for d in drugs[i:] if areCompatibleDrugs(d, d1)):
        compatibilities[d1].append(d2)
        compatibilities[d2].append(d1)

# Navigate through list, starting with the node with the less dependencies to improve early exit.
# This order will allow a faster diminution of the recursive calls ranges.
print(getBiggestGroup(sorted(drugs, key=lambda k: len(compatibilities[k])), [], 0))