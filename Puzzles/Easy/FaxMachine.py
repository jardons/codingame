COLORS = '* '

w, h = int(input()), int(input())

line, current = '', 0
for i in (int(i) for i in input().split()):
    while i > 0:

        c = i if i + len(line) < w else w - len(line)
        line += COLORS[current] * c
        i -= c

        if len(line) >= w:
            print(f'|{line}|')
            line = ''

    current = (current + 1) % 2
