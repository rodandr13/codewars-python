"""
["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"
"""


def print_array(arr):
    return ",".join([str(x) for x in arr])
