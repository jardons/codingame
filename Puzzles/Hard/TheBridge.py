import sys

m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive
road = [input()+'.'*99 for _ in range(4)]
d = len(road[0])-99

print(f'Distance is {d}', file=sys.stderr, flush=True)
for r in road:print(r[0:d], file=sys.stderr, flush=True)

def Jump(state):
    speed = state[0]
    bikes = []
    for b in state[1]:
        x = b[0] + speed
        y = b[1]
        if road[y][x]=='.':
            bikes.append((x, y))
    return (speed, bikes)

def Move(state, s, m):
    speed = state[0] + s

    if speed < 1:
        return (speed,[])

    bikes = []
    for b in state[1]:
        x = b[0] + speed
        y = b[1] + m
        if 0<=y<4 and len([p for p in road[y][b[0]+1:x+1] if p!='.']) == 0 and len([p for p in road[b[1]][b[0]:x] if p!='.']) == 0:
            bikes.append((x, y))

    return (speed, bikes)

ACTIONS = {
    'SPEED': lambda state:Move(state, 1, 0),
    'JUMP': Jump,
    'SLOW': lambda state:Move(state, -1, 0),
    'UP': lambda state:Move(state, 0, -1),
    'DOWN': lambda state:Move(state, 0, 1),
    'WAIT': lambda state:Move(state, 0, 0),
}

def Calculate(state):
    for action in ACTIONS:
        new_state = ACTIONS[action](state)
        if len(new_state[1]) >= v:
            if new_state[1][0][0] >= d:
                return action

            if Calculate(new_state):
                return action
    return None

# game loop
while True:
    speed = int(input())  # the motorbikes' speed

    # x: x coordinate of the motorbike
    # y: y coordinate of the motorbike
    # a: indicates whether the motorbike is activated "1" or detroyed "0"
    bikes = [b for b in [[int(j) for j in input().split()] for _ in range(m)] if b[2]]

    state = (speed, bikes)

    # In order to get all achievments, first attempt try to save all bikes if possible.
    # This is a lazy solution as we could change propagation in order to search optimal path instead of stopping on first one.
    v, temp = len(bikes), v
    a = Calculate(state)

    if not a:
        # If all bikes cannot be saved, stay in line with objective provided in input.
        v = temp
        a = Calculate(state)

    # A single line containing one of 6 keywords: SPEED, SLOW, JUMP, WAIT, UP, DOWN.
    print(a)
