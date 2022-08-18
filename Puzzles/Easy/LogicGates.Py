BIT_ZERO = '_'
BIT_ONE = '-'

n, m = int(input()), int(input())

# Load data
data = {name: signal for name, signal in (input().split() for _ in range(n))}

# Operations Dictionary
operations = {
    'AND': lambda v1, v2: ''.join(map(lambda t: BIT_ONE if BIT_ONE == t[0] == t[1] else BIT_ZERO, zip(v1, v2))),
    'OR': lambda v1, v2: ''.join(map(lambda t: BIT_ONE if BIT_ONE in t else BIT_ZERO, zip(v1, v2))),
    'XOR': lambda v1, v2: ''.join(map(lambda t: BIT_ONE if t[0] != t[1] else BIT_ZERO, zip(v1, v2))),
    'NAND': lambda v1, v2: ''.join(map(lambda t: BIT_ZERO if BIT_ONE == t[0] == t[1] else BIT_ONE, zip(v1, v2))),
    'NOR': lambda v1, v2: ''.join(map(lambda t: BIT_ZERO if BIT_ONE in t else BIT_ONE, zip(v1, v2))),
    'NXOR': lambda v1, v2: ''.join(map(lambda t: BIT_ZERO if t[0] != t[1] else BIT_ONE, zip(v1, v2)))
}

# Compute operations
for i in range(m):
    name, type, input1, input2 = input().split()

    data[name] = operations[type](data[input1], data[input2])

    print(f"{name} {data[name]}")
