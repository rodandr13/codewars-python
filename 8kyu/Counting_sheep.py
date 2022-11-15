"""
Consider an array/list of sheep where some sheep may be missing from the
place. We need a function that counts the number of sheep present in the array
(true means present).
"""

"""
def count_sheeps(sheep):
    sum = 0
    for value in sheep:
        if value:
            sum += 1
    return sum
"""


def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
