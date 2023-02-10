"""
This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function
represents the right operand
Division should be integer division. For example, this should return 2,
not 2.666666...:
eight(divided_by(three()))
"""


def zero(func=None):
    return 0 if not func else func(0)


def one(func=None):
    return 1 if not func else func(1)


def two(func=None):
    return 2 if not func else func(2)


def three(func=None):
    return 3 if not func else func(3)


def four(func=None):
    return 4 if not func else func(4)


def five(func=None):
    return 5 if not func else func(5)


def six(func=None):
    return 6 if not func else func(6)


def seven(func=None):
    return 7 if not func else func(7)


def eight(func=None):
    return 8 if not func else func(8)


def nine(func=None):
    return 9 if not func else func(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y

