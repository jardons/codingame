import sys
import math

NOTES = ['G', 'F', 'E', 'D', 'C', 'B', 'A']

w, h = (int(i) for i in input().split())
text = input().split()

# trim first and last empty lines
if text[0] == 'W': text[1] = int(text[1]) % w
if text[-2] == 'W': text[-1] = int(text[-1]) % w

# Parse image as table
# Once we have defined our structural grid, we won't need the full table in memory.
# Next optimisation would be to load one line per note once the grid structure is identified.
img = []
for i in range(0, len(text), 2):
    c = ' ' if text[i] == 'W' else '#'
    l = int(text[i+1])

    while l > 0:
        last = len(img[-1]) if len(img) > 0 else w
        if last < w:
            img[-1] = img[-1] + [ c ] * min(l, w - last)
            l -= w - last
        else:
            img.append([ c ] * min(l, w))
            l -= w

# Get start and end columns
start = next(i for i in range(w) if any(row[i] == '#' for row in img))
end = next(i for i in range(w-1, 0, -1) if any(row[i] == '#' for row in img))

# Calculate line positions
grid = []
tmp = None
for i, r in enumerate(img):
    if r[start] != '#' and tmp is not None:
        tmp[1] = i-1
        tmp = None
    elif r[start] == '#' and tmp is None:
        tmp = [i, None]
        grid.append(tmp)

# mark end of last line if nothing below. (no note bellow E)
if grid[-1][1] is None: grid[-1][1] = len(img) - 1

# add virtual first C line to grid.
grid.append((grid[-1][0] * 2 - grid[-2][0], grid[-1][1] * 2 - grid[-2][1]))

# Calculate note size
size = (grid[1][0] - grid[0][1]) + (grid[0][1] - grid[0][0]) + 1

# Go through score for notes.
i = start
result = []
while i < end:
    for k in range(12):

        # Selection of a predefined fix point in the note to detect it.
        # Note presence will always be checked on the upper left of the note,
        # allowing us to ignore any test on the tail as, when the tail is on the left,
        # it's always directed downside and the challenge don't require to parse chords with multiple notes.
        j = grid[k//2][0] - 1 if k % 2 == 1 else grid[k//2][0] - size // 2

        if j >= 0 and j < len(img) and img[j][i] == '#':
            # Check color in the horizontal center of the note.
            noteType = 'Q' if img[j][i + size // 2] == '#' else 'H'
            result.append(f'{NOTES[k%7]}{noteType}')

            # Skip full note as no simultanate note are possible.
            i += size 
            break

    i += 1

# Write result
print(' '.join(result))