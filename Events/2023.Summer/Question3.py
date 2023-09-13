from json import dumps, loads
from typing import List


def merge_files(file_contents: List[str]) -> str:
    '''

    Args:

        - file_contents (List[str]): A list of strings, where each string represents the contents of a file.

    Returns:

        The contents of the merged file.
    '''

    r = {}

    for f in (l.split('\n') for l in file_contents):
        
        for l in f:
            data = { d[0]: d[1] for d in (d.split('=') for d in l.split(';') ) }
            name = data["Name"]
            del data["Name"]

            if name in r:
                old_data = r[name]
                for k in data:
                    old_data[k] = data[k]
            else:
                r[name] = data

    result = []

    for k in sorted(r.keys()):
        local_data = r[k]
        data = ';'.join(f'{data_key}={local_data[data_key]}' for data_key in sorted(local_data.keys()))
        if data:
            result.append(f'Name={k};{data}')
        else:
            result.append(f'Name={k}')

    return "\n".join(result)

# Ignore and do not change the code below


def try_solution(merged_file: str):
    '''
    Try a solution

    Args:

        - str (str): The contents of the merged file.
    '''
    json = merged_file
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = merge_files(
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
