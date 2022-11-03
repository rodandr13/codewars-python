"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
"""

"""
def high_and_low(numbers):
    maximum = max(map(int, numbers.split()))
    minimum = min(map(int, numbers.split()))
    return str(maximum) + ' ' + str(minimum)
"""


def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split()]
    numbers.sort()
    return f'{numbers[-1]} {numbers[0]}'


assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
assert high_and_low("1 2 3") == "3 1"
