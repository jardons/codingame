from json import dumps, loads
from typing import List
import numpy

# Sample Wall data :

#                                        
#                        _               
#                      _| |_             
#                    _|     |_       _   
#      _   _       _|         |_   _| |_ 
#_   _| |_| |_   _|             |_|     |
# |_|         |_|                        
#                                        
#                                        

# data provided as a single string with '\n'

def compute(wall: str) -> str:
	'''

	Args:

        - wall (str): A string containing the wall and the magical path

	Returns:

        The move to apply to the headstone
	'''

    w = wall.split('\n')
    r = [''] * (len(w[0]) // 2)
    for s in w:
        previous = ' '
        for i, c in enumerate(s):
            if c == '|':
                r[i // 2] = 'UP' if previous == '_' else 'DOWN'
            previous = c

    return r