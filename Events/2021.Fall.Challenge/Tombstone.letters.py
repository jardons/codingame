# Sample letters data :
# WETYDGWEUFGYITQFGHEJGFEQWHKJHDIQWEFQWEKJHKDHKHJQWEGHFDGWEJLJGCFQWEICGEQKJGWEL

from json import dumps, loads
from typing import List


def compute():
    '''

    Args:

        - letters (str): A string containing letters

    Returns:

        The list of moves to apply to the headstone
    '''

    m = { 'E': 'UP', 'G': 'DOWN' }

    r = []
    for c in letters:
        if c in m:
            r.append(m[c])
    return r
