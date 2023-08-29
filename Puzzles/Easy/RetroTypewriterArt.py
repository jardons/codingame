MAPPING = { 'sp': ' ', 'bS': '\\', 'sQ': '\'', 'nl': '\n' }

result = []

for l in input().split():
    end = len(l) - 1
    while end > 0 and not l[0:end].isnumeric(): end -= 1

    count, c = int(l[0:end]) if end > 0 else 1, l[end::]
    for _ in range(count):
        result.append(MAPPING.get(c, c))

print(''.join(result))
