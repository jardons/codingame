for l in (input() for _ in range(int(input()))):

    count, flood = 0, 0
    for c in l:
        if flood > 0:
            flood -=1
            continue

        if c == 'f':
            count += 1
            flood = 2

    print(count)
