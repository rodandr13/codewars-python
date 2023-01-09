"""
Please write a function that will take a string as input and return a hash.
The string will be formatted as such. The key will always be a symbol
and the value will always be an integer.

"a=1, b=2, c=3, d=4"
This string should return a hash that looks like

{ 'a': 1, 'b': 2, 'c': 3, 'd': 4}
"""
"""
from re import findall
def str_to_hash(st): 
    return {i:int(j)for i,j in findall(r'(\w+)=(\d+)',st)}
"""


def str_to_hash(st):
    if not st:
        return {}
    items = st.split(", ")
    result = {}
    for item in items:
        key, value = item.split("=")
        result[key] = int(value)
    return result
