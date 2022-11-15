"""
Your task is to sum the differences between consecutive pairs
in the array in descending order.
"""

"""
def sum_of_differences(arr):
    if len(arr) > 1:
        result = 0
        arr.sort(reverse=True)
        return sum([arr[i] - arr[i+1] for i in range(len(arr) - 1)])
    return 0
"""


def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0
