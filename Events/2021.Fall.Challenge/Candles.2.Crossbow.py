from json import dumps, loads
from typing import List

# Sample Data

# [
#   {
#     "id": 10,
#     "name": "Thaddeus Wick",
#     "fatherId": -1,
#     "motherId": -1,
#     "spouseId": 22,
#     "gender": "M",
#     "childIds": []
#   },
#   {
#     "id": 20,
#     "name": "Brooke Wetherby",
#     "fatherId": 7,
#     "motherId": 8,
#     "spouseId": -1,
#     "gender": "F",
#     "childIds": [ 30, 31 ]
#   }
# ]

# recursively calculate the descendants count.
def getDescendants(n, dic):
    if 'descendants' not in n:
        if len(n['childIds']) == 0:
            n['descendants'] = 0
        else:
            n['descendants'] = len(n['childIds']) + sum( (getDescendants(dic[i], dic) for i in n['childIds']) )

    return n['descendants']


def compute(nodes: List[dict]):
    '''

    Args:

        - nodes (List[dict]): Each node represents a member of this family. Described by their name, parents, children and spouse.

As you might expect, this medieval document only acknowledges male/female, and father/mother family units.
    '''

    # Quick access index for navigation
    dic = {}
    for n in nodes:
        dic[n['id']] = n

    # The text on this plaque is practically illegible:

    # This crosbow belonged to ##############
    # Buried #####################
    # ############################

    # ########################### family tree ##################
    # ###### the fact that the total number of his descendants
    # is equal to 48, the exact age at which he ######

    # loop through person with 48 descendants.
    for n in filter(lambda x: x['gender'] == 'M' and getDescendants(x, dic) == 48, nodes):
        return n['name']

    return None