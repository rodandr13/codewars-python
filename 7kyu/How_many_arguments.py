"""
Create a function args_count, that returns the count of passed arguments
"""


def args_count(*args, **kwargs):
    return len(args) + len(kwargs)


assert args_count(100) == 1
assert args_count(100, 2, 3) == 3
assert args_count(32, a1=12) == 2
