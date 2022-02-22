# Clean a found value from all unfinished combinations.
def CleanValues(values, cleanedValue):
    for k in (k for k in values.keys() if len(values[k]) > 1 and cleanedValue in values[k]):
        values[k].remove(cleanedValue)

        # This cleaning process can trigger additional recursive cleaning if it allow to identify new values.
        if len(values[k]) == 1:
            CleanValues(values, values[k][0])

# Read Inputs.
n, t = (int(i) for i in input().split())

# Create table of possible values. (at start, all combinations)
values = { i*2+1 :[j*2+2 for j in range(n)] for i in range(n) }

for i in range(t):
    # Isolate values between odd and even type.
    odd, even = [], []
    for j in (int(j) for j in input().split()):
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    
    for e in even:
        # Odds values cannot be on other side of visible even.
        for o in (o for o in odd if e in values[o]):
            values[o].remove(e)
            # Once we have one possibility left, we can remove the found value from all other combination.
            if len(values[o]) == 1:
                CleanValues(values, values[o][0])

# convert dictionary to string result table.
result = []
for k in sorted(values.keys()):
    result.append(str(values[k][0]))

print(" ".join(result))