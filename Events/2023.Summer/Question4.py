import sys
from json import dumps, loads
from typing import List

DIRECTIONS = [ (1, 0), (0, -1), (-1, 0), (0, 1) ]
ACTIONS = ['FORWARD', 'BACK', 'TURN LEFT', 'TURN RIGHT']

def simulate(instructions: List[str], target: List[int]) -> bool:
    pos, direction = (0, 0), 0

    for i in instructions:
        if i == 'FORWARD':
            diff = DIRECTIONS[direction]
            pos = (pos[0] + diff[0], pos[1] + diff[1])
        elif i == 'BACK':
            diff = DIRECTIONS[direction]
            pos = (pos[0] - diff[0], pos[1] - diff[1])
        elif i == 'TURN LEFT':
            direction = (direction + 3) % 4
        elif i == 'TURN RIGHT':
            direction = (direction + 1) % 4
        else:
            print(f'Invalid action {a}', file=sys.stderr, flush=True)

    return pos[0] == target[0] and pos[1] == target[1]

def find_correct_path(instructions: List[str], target: List[int]) -> str:
    '''

    Args:

        - instructions (List[str]): The list of instructions as memorized by the mutant.
        - target (List[int]): The coordinates (x, y) of the target.

    Returns:

        A string respecting the given format to fix the mutant's path.
    '''

    for i in range(len(instructions)):
        action = instructions[i]
        for a in ACTIONS:
            if action == a: continue
            instructions[i] = a
            if simulate(instructions, target):
                s = f"Replace instruction {i+1} with {a}"
                print(s, file=sys.stderr, flush=True)
                return s

        instructions[i] = action

    return "Not found"

# Ignore and do not change the code below


def try_solution(recipe: str):
    '''
    Try a solution

    Args:

        - str (str): A string respecting the given format to fix the mutant's path.
    '''
    json = recipe
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = find_correct_path(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
