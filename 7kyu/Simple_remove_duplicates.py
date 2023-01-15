"""
Remove the duplicates from a list of integers, keeping the last ( rightmost )
occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]

More examples can be found in the test cases.

Good luck!
"""


def solve(arr):
    arr = arr[::-1]
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result[::-1]
