"""
Take an array and remove every second element from the array. Always keep the
first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""


def remove_every_other(my_list):
    # Your code here!
    return [my_list[x] for x in range(len(my_list)) if x % 2 == 0]

