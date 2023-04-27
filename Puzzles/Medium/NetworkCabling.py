n = int(input())
m = [[int(j) for j in input().split()] for i in range(n)]

# First part : get horizontal distance from the first to the last.
horizontal = abs(max(o[0] for o in m) - min(o[0] for o in m))

# Second part, calculate distance starting from median house on vertical axis.
m = [i[1] for i in m]
m.sort()
vertical = sum(abs(m[n//2]-t) for t in m)

print(horizontal + vertical)
