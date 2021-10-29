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

def compute(clans: List[dict]) -> str:
    '''

    Args:

        - clans (List[dict]): All the clan names and their crests from the windows.

    Returns:

        The name on the panel you wish to press.
    '''

	# name of the current castle  is available on the image.
	# the name is missing the 7 first characters and end with a 'y'.
	# The following letters are present on the floor and probably fell from the castle name above.
    groundLetters = ['e', 'b', 's', 'r']

    for c in clans:
        name = c["name"]
        if len(name) == 8 and name[-1] == 'y' and all(e in name.lower() for e in groundLetters):
            return name

    return None