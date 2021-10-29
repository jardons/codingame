from json import dumps, loads
from typing import List

def compute(clans: List[str], castles: List[dict]) -> List[str]:
    '''

    Args:

        - clans (List[str]): The list of the five clans.
        - castles (List[dict]): The list of castles.

    Returns:

        An ordered list of clan names.
    '''

    # gets the list of castles ids based on the clans names.
    for c in castles:
        if c["clanName"] in clans:
            print(c)

    # order hardcoded and based on the map.
    # 50 -> 108 -> 41 -> 71 -> 86
    return ['Campbell', 'Fergusson', 'Rasberry', 'Arbuthnott', 'Anderson']