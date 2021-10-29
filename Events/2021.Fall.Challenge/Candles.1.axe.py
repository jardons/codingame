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

    # "This axe belonged to ##################, first-cousin to the grandson of the only child of ####################
    # Her only regret was not having more than one child."

    # Keep female with only one child. At least one parent is needed for the rest of validation.
    for n in filter(lambda x: x['gender'] == 'F' and len(x['childIds']) == 1 and (x['fatherId'] != -1 or x['motherId'] != -1), nodes):
 
        # Load all grand parents
        grandParents = []
        for i in (n['fatherId'], n['motherId']):
            if i in dic:
                grandParents.append(dic[i]['fatherId'])
                grandParents.append(dic[i]['motherId'])

        # ignore grand-parent that could not provide a cousin
        validGrandParents = []
        for i in filter(lambda x: x in dic and len(dic[x]['childIds']) >= 2, grandParents):
            # Search only grand parents that are only child.
            if not any((j in dic and len(dic[j]['childIds']) == 1 for j in (dic[i]['fatherId'], dic[i]['motherId']))):
                continue

            validGrandParents.append(i)

        if len(validGrandParents) != 0:
            return n['name']

    return None