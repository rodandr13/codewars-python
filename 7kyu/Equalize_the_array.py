"""
No description!!!

Input :: [10,20,25,0]

Output :: ["+0", "+10", "+15", "-10"]

Show some love, rank and upvote!
"""
"""
def equalize(arr):
    return ["{:+d}".format(i-arr[0]) for i in arr]
"""
"""
def equalize(arr):
    return [f"{n - arr[0]:+d}" for n in arr]
"""


def equalize(arr):
    result = []
    for i in range(len(arr)):
        temp = arr[i] - arr[0]
        if temp >= 0:
            result.append(f"+{temp}")
        else:
            result.append(f"{temp}")
    return result
