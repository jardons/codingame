for i in range(int(input())):
    x = input()
    r, q, i = '(', set(), x
    while i not in q:
        if i == 1:
            r = ')'
            break
        q.add(i)
        s, i = str(i), 0
        for c in s:
            i += int(c) * int(c)

    print(f"{x} :{r}")