"""
Given a string containing a list of integers separated by commas,
write the function string_to_int_list(s) that takes said string and returns a new list containing all integers present in the string, preserving the order.

For example, give the string "-1,2,3,4,5", the function string_to_int_list()
should return [-1,2,3,4,5]
"""


def string_to_int_list(s):
    return [int(x) for x in s.split(',') if x]
