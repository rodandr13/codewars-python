"""
You are given an initial 2-value array (x).
You will use this to calculate a score.

If both values in (x) are numbers, the score is the sum of the two.
If only one is a number, the score is that number. If neither is a number,
return 'Void!'.

Once you have your score, you must return an array of arrays. Each sub array
will be the same as (x) and the number of sub arrays should be equal
to the score.
"""
"""
def explode(arr):  
    numbers = [n for n in arr if type(n) == int]
    return [arr] * sum(numbers) if numbers else "Void!"
"""


def explode(arr):
    a, b = arr
    is_a_int = isinstance(a, int)
    is_b_int = isinstance(b, int)
    if is_a_int and is_b_int:
        return [arr] * (a + b)
    elif is_a_int or is_b_int:
        if is_a_int:
            return [arr] * a
        else:
            return [arr] * b
    else:
        return "Void!"


assert explode(['a', 3]) == [['a', 3], ['a', 3], ['a', 3]]
assert explode([6, 'c']) == [[6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c']]
assert explode(['a', 'b']) == 'Void!'
