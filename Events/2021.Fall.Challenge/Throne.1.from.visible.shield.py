from json import dumps, loads
from typing import List

# Sample clans data :

#[
#  {
#    "name": "Abercrombie",
#    "corners": [
#      { "color": "blue", "symbolType": "none", "symbolColor": "none", "symbolAmount": 0 },
#      { "color": "white", "symbolType": "stripe", "symbolColor": "orange", "symbolAmount": 2 },
#      { "color": "white", "symbolType": "stripe", "symbolColor": "orange", "symbolAmount": 2 },
#      { "color": "blue", "symbolType": "none", "symbolColor": "none", "symbolAmount": 0 }
#    ]
#  },
#  {
#    "name": "Livingston",
#    "corners": [
#      { "color": "blue", "symbolType": "crescent", "symbolColor": "red", "symbolAmount": 1 },
#      { "color": "red", "symbolType": "key", "symbolColor": "blue", "symbolAmount": 2 },
#      { "color": "black", "symbolType": "star", "symbolColor": "green", "symbolAmount": 3 },
#      { "color": "green", "symbolType": "rectangle", "symbolColor": "black", "symbolAmount": 4 }
#    ]
#  }
#]

# Constraints :
# clans[].corners[].color = blue | orange | green | red | black | white
# clans[].corners[].symbolType = disc | star | cross | rectangle | stripe | rose | crescent | lily | crown | key | none
# 0 <= clans[].corners[].symbolAmount <= 5
# clans[].corners[].symbolColor = blue | orange | green | red | black | none

def compute(clans: List[dict]) -> str:
    '''

    Args:

        - clans (List[dict]): All the clan names and their crests from the windows.

    Returns:

        The name on the panel you wish to press.
    '''

    for c in clans:
        # shield is visible when entering the room.
        corner = c['corners'][0]
        if not (corner['color'] == 'blue' and corner['symbolType'] == 'none'):
            continue

        corner = c['corners'][1]
        if not (corner['color'] == 'white' and corner['symbolType'] == 'disc' and corner['symbolAmount'] == 3 and corner['symbolColor'] == 'orange'):
            continue

        return c['name']

    return None