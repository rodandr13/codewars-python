"""
Task
Given array of integers, for each position i, search among the previous
positions for the last (from the left) position that contains a smaller
value. Store this value at position i in the answer.
If no such value can be found, store -1 instead.

Example
For items = [3, 5, 2, 4, 5], the output should be [-1, 3, -1, 2, 4].
"""
"""
def array_previous_less(arr):
    out = []

    for i, n in enumerate(arr):
        x = -1
        for m in arr[:i][::-1]:
            if m < n:
                x = m
                break
        out.append(x)

    return out
"""


def array_previous_less(arr):
    result = [-1]
    for i in range(1, len(arr)):
        temp = arr[:i]
        while len(temp) != 0:
            last = temp.pop()
            if last < arr[i]:
                result.append(last)
                break
        else:
            result.append(-1)

    return result
