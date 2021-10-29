from json import dumps, loads
from typing import List

def compute(graves: List[dict]) -> str:
    '''

    Args:

        - graves (List[dict]): The list of graves registered here.

    Returns:

        The name on the candle you wish to place in this candle holder.
    '''
	
	# int is available on the cemetary image and can be linked to a missing tomb on the map.
    return list(filter(lambda x: x['number'] == 894, graves))[0]['name']