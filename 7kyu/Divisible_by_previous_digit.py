"""
Take a number and check each digit if it is divisible by the digit on its left
checked and return an array of booleans.

The booleans should always start with false becase there is no digit before
the first one.
"""
"""
def divisible_by_last(n):
    l = list(map(int, f"0{n}"))
    return [x and not y%x for x,y in zip(l, l[1:])]
"""


def divisible_by_last(n):
    numbers = [int(i) for i in list(str(n))]
    result = [False]
    for i in range(1, len(numbers)):
        try:
            if numbers[i] % numbers[i-1] == 0:
                result.append(True)
            else:
                result.append(False)
        except ZeroDivisionError:
            result.append(False)
    return result
