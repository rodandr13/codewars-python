"""
Looks like some hoodlum plumber and his brother has been running around
and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before
you receive any more complaints.

Pipes list is correct when each pipe after the first index is greater (+1)
than the previous one, and that there is no duplicates.
"""
"""
def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))
"""
"""
def pipe_fix(num):
    return range(min(num), max(num)+1)
"""


def pipe_fix(nums):
    nums.sort()
    return [x for x in range(nums[0], nums[-1] + 1)]
