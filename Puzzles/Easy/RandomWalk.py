X_MOVES = [0,0,1,-1]
Y_MOVES = [1,-1,0,0]

a, b, m = (int(input()) for _ in range(3))
x, y, d = 0, 0, 0

count = 0
while count == 0 or x != 0 or y != 0:
    d = (a * d + b) % m
    direction = d % 4
    x += X_MOVES[direction]
    y += Y_MOVES[direction]

    count += 1

print(count)
