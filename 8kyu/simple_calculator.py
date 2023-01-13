"""
You are required to create a simple calculator that returns the result
of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation
to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the
list above a message "unknown value" must be returned.

Example:
calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"
"""


def calculator(x, y, op):
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y
    }
    if op not in operators or not isinstance(x, int) or not isinstance(y, int):
        return "unknown value"

    return operators[op](x, y)
