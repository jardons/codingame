from json import dumps, loads
from typing import List


def gear_balance(n_gears: int, connections: List[List[int]]) -> List[int]:
    '''

    Args:

        - n_gears (int): An integer representing the number of gears in the system (numbered from 0 to N-1).
        - connections (List[List[int]]): An array representing all pairs of gears connected together.

    Returns:

        An array of two integers representing the number of gears rotating clockwise and counterclockwise respectively, or [-1, -1] if the configuration is invalid.
    '''

    d = {}
    for i, j in connections:
        if i not in d: d[i] = []
        d[i].append(j)
        if j not in d: d[j] = []
        d[j].append(i)

    clockwise, counter = set(), set()
    clockwise.add(0)

    q = [0]

    while q:
        o = q.pop()

        same = clockwise if o in clockwise else counter
        other = counter if o in clockwise else clockwise

        for tgt in d[o]:
            if tgt in same: return [-1, -1]
            if tgt in other: continue

            other.add(tgt)
            q.append(tgt)

    return [len(clockwise), len(counter)]

# Ignore and do not change the code below


def try_solution(output: List[int]):
    '''
    Try a solution

    Args:

        - List[int] (List[int]): An array of two integers representing the number of gears rotating clockwise and counterclockwise respectively, or [-1, -1] if the configuration is invalid.
    '''
    json = output
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = gear_balance(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
