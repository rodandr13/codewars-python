"""
Closure Counter
Define the function counter that returns a function that returns
an increasing value.
The first value should be 1.
You're going to have to use closures.
Example:
const newCounter = counter();
newCounter() // 1
newCounter() // 2
"""


def counter():
    n = 0

    def inner():
        nonlocal n
        n = n + 1
        return n
    return inner
